import math
import pandas as pd
import openpyxl

answer_move = []
answer_victory = []
def data(need_data1, need_data2, middle):
    time = []
    y = list(range(need_data1, need_data2, middle))  # 度数
    for i in range(len(y)):
        time.append(y[i] / 10)
    return time
    # 求sin()

def competion(data):
    tem1=0.01
    tem2=0.054

    for i in data:
        result = tem1*math.sin(math.radians(i*1.4005))+tem2*math.cos(math.radians(i*1.4005))
        answer_move.append(result)#位移
    #for x in data:
        #result1 =tem1*math.cos(math.radians(x*1.4005))+(-tem2*math.sin(math.radians(x*1.4005)))
        #answer_victory.append(result1)#速度



def deal(company_name_list,list2 ):
    # 列表


    # list转dataframe
    df = pd.DataFrame(company_name_list, columns=['3-1-浮子'])

    # 保存到本地excel
    df.to_excel("3-1--浮子_位移.xlsx", index=False)

    #bf = pd.DataFrame(list2, columns=['3-1-振子'])

    # 保存到本地excel
    #bf.to_excel("3-1-振子_速度.xlsx", index=False)


def main():

    time_list=data(0, 1793, 2)
    competion(time_list)
    deal(answer_move,answer_victory)


if __name__ == '__main__':
    main()
