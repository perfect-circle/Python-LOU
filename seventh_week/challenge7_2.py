import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_clean():
    """清洗数据
    """
    df_data = pd.read_excel('ClimateChange.xlsx','Data')
    df_co2 = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT']\
            .set_index('Country code')
    df_gdp = df_data[df_data['Series code'] == 'NY.GDP.MKTP.CD']\
            .set_index('Country code')
    # 缺失值替换
    df_co2_nan = df_co2.iloc[:,5:].replace({'..':np.nan})
    df_gdp_nan = df_gdp.iloc[:,5:].replace({'..':np.nan})
    # 缺失值填充
    df_co2_fill = df_co2_nan.fillna(method='ffill',axis=1)\
            .fillna(method='bfill',axis=1)
    df_gdp_fill = df_gdp_nan.fillna(method='ffill',axis=1)\
            .fillna(method='bfill',axis=1)
    # 数据合并
    df_co2_fill['CO2-SUM'] = df_co2_fill.sum(axis=1)
    df_gdp_fill['GDP-SUM'] = df_gdp_fill.sum(axis=1)
    df_merge = pd.concat([df_co2_fill['CO2-SUM'],\
            df_gdp_fill['GDP-SUM']],axis=1)
    # 填充整排数值都为空值的国家,填充值为0
    df_merge_fill = df_merge.fillna(value=0)

    return df_merge_fill

def co2_gdp_plot():
    """绘制统计图
    """
    df_clean = data_clean()
    # 归一化处理
    df_max_min = (df_clean - df_clean.min()) /\
            (df_clean.max() - df_clean.min())
    # 返回中国的数据
    china = []
    df_china = df_max_min.loc['CHN']
    for i in df_china.values:
        china.append(np.round(i,3))

    # 创建需要绘制的x轴标签的国家
    countries_labels = ['CHN','USA','GBR','FRA','RUS']
    # 创建绘标签的国家和对应的x轴坐标
    sticks_labels = []
    labels_position =[]
    # 添加国家和对应位置
    for i in range(len(df_max_min)):
        if df_max_min.index[i] in countries_labels:
            sticks_labels.append(df_max_min.index[i])
            labels_position.append(i)

    # 把df_max_min绘制成统计图
    fig = plt.subplot()
    df_max_min.plot(
            kind='line',
            title='GDP-CO2',
            ax=fig
            )
    plt.xlabel('Countries')
    plt.ylabel('Values')

    # 在x轴显示列表中的国家
    plt.xticks(labels_position,sticks_labels,rotation='vertical')
    plt.show
    return fig, china

if __name__=="__main__":
    co2_gdp_plot()
