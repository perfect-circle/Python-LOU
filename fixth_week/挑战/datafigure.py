import pandas as pd
import matplotlib.pyplot as plt


def data_plot():
    with open('user_study.json') as f_ob:
        data = pd.read_json(f_ob)

    df = data.groupby('user_id').sum()
    ax = df.plot.line(title='StudyData')
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    plt.savefig('tu.png')
    return ax


if __name__ == "__main__":
    data_plot()
