import math

import pandas as pd


def data(need_data1, need_data2, middle):  # 数据处理，得到前四十个周期每个0.2s的间隔
    time = []
    y = list(range(need_data1, need_data2, middle))  # 度数
    for i in range(len(y)):
        time.append(y[i] / 10)
    return time


def competion(need_data):
    answer = []
    for i in need_data:  # 将所得运动方程转化为编程语言求解
        result = -0.112 * math.sin(math.radians(i * 1.4005)) + 0.021 * math.cos(math.radians(i * 1.4005))
        answer.append(result)
    # 求解振子时，只需要将运动方程改变即可
    return answer


def data_storage(name_list):
    # list转dataframe
    finally_anwser = pd.DataFrame(name_list, columns=['浮子速度'])

    # 保存到本地excel
    finally_anwser.to_excel("浮子_速度.xlsx", index=False)


def main():
    time_list = data(0, 1793, 2)
    finally_anwser = competion(time_list)
    data_storage(finally_anwser)


if __name__ == '__main__':
    main()
