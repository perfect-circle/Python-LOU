import pandas as pd
import numpy as np
def co2():
    data = pd.read_excel("ClimateChange.xlsx",'Data')
    data = data[data["Series code"]=='EN.ATM.CO2E.KT'].set_index("Country code")
    data.dropna(how='all',inplace=True)
    data = data.iloc[:,5:]
    data.replace({'..':np.nan},inplace=True)
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill',axis=1)
    country = pd.read_excel('ClimateChange.xlsx',"Country"
            ).set_index('Country code')
    df = pd.concat([data.sum(axis=1),  country['Income group']],axis=1)
    sum_emissions = df.groupby('Income group').sum()
    sum_emissions.columns = ['Sum emissions']
    df[2] = country['Country name']
    highest_emissions = df.sort_values(0,ascending=False).groupby(
            'Income group').head(1).set_index('Income group')
    highest_emissions.columns = ["Highest emissions", 'Highest emission country']
    lowest_emissions = df[df[0]>0].sort_values(0).groupby("Income group"
            ).head(1).set_index('Income group')
    lowest_emissions.columns = ['Lowest emissions', 'Lowest emission country']
    results = pd.concat([sum_emissions, highest_emissions, lowest_emissions],axis=1)
    results = results.loc[:,['Sum emissions','Highest emission country',\
            'Highest emissions','Lowest emission country','Lowest emissions']]
    return results

if __name__ == "__main__":
    print(co2())
