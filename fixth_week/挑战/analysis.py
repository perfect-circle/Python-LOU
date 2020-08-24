import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0

    with open(file) as f:
        data = pd.read_json(f)

    times = data[data['user_id'] == user_id]['minutes'].size
    minutes = data[data['user_id'] == user_id]['minutes'].sum()

    return times, minutes

if __name__ == "__main__":
    times, minutes = analysis('user_study.json', 199071)
    print(times)
    print(minutes)
