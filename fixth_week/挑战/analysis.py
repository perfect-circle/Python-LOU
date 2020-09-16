import json
import pandas as pd

def analysis(file,user_id):
    times = 0
    minutes = 0

    with open(file) as f:
        df = pd.read_json(f)

    times = df[df['user_id'] == user_id]['course'].count()
    minutes = df[df['user_id'] == user_id]['minutes'].sum()

    return times, minutes

if __name__ == "__main__":
    file_name = input("Please entry file name: ")
    user_id = int(input("Please entry user ID: "))
    times, minutes = analysis(file_name, user_id)
    print("学习次数：{} \n学习总时间：{}".format(times,minutes))
