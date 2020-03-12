import pandas as pd
import re
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


def find_na(mainD):
    #drop the discription col
    for col in mainD.columns.values:
        if re.findall("DOCUMENT", col):
            mainD = mainD.drop(col, axis=1)

    #check types of data
    # print(mainD.dtypes)
    # print(mainD.dtypes.value_counts())

    # #check for na data
    # print(mainD.columns)
    # print(mainD.isnull().any())
    # print(mainD.columns[mainD.isnull().any() == True])

    #count total rows
    numOfRows = mainD.shape[0]

    #find all column with N.A value
    list_na_col = mainD.columns[mainD.isnull().any()]

    # find top x perc,  N.A column
    # na_count = {}
    # for col in list_na_col:
    #     na_count[col] = (mainD[col].isna().sum()/numOfRows)*100
    # # categ_na_count = sorted(categ_na_count.items(),key=lambda  item:item[1])
    # na_count = sorted(na_count.items(), key=lambda item: item[1],reverse=True)
    # print(na_count)
    # for lili personal read  -> lamda的意义
    # 这里的d.items()实际上是将d变成iterate 数据，items()方法将字典的元素转化为了array，
    # 而这里key参数对应的lambda表达式的意思则是选取array的第二个元素(value)作为比较参数
    # 如果写作key=lambda item:item[0]的话则是选取第一个元素(key)作为比较对象.
    # lambda x:y中x表示输出参数，y表示lambda函数的返回值
    # 所以采用这种方法可以对字典的value进行排序。注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。


    #split data into different datatype
    #categories
    categ_df = mainD.select_dtypes(include=['object']).copy()

    # for col in categ_df:
    #     print(categ_df[col].value_counts(),'\n')
    categ_df_dummies = pd.get_dummies(categ_df)

    # Place the DataFrames side by side
    new_df = pd.concat([mainD, categ_df_dummies], axis=1)
    mainD = new_df.drop(categ_df, axis=1)

    # idea: 1 change the na with some number
    mainD = mainD.fillna(mainD.mean())
    # mainD.to_csv (r'/Users/leanne/year2sem2/TBA2104/HCG_Dataset/application_train_1.csv', index = False, header=True)
    # print(mainD.head())
    # print(mainD.corr())
    # median = df['NUM_BEDROOMS'].median()

    col_corr = set()  # Set of all the names of deleted columns
    corr_matrix = mainD.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            # if (corr_matrix.iloc[i, j] >= 0.8) and (corr_matrix.columns[j] not in col_corr):
            if corr_matrix.iloc[i, j] >= 0.5 and (corr_matrix.columns[j] not in col_corr):
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
                if colname in mainD.columns:
                    del mainD[colname]  # deleting the column from the dataset

    print(col_corr)
    print(mainD.head())

    #numerical
    num_df = mainD.select_dtypes(include=['number']).copy()
    list_num = num_df.columns[num_df.isnull().any()]
    # print(list_num)

def main():
    #determine the dataframe
    data_dir = '/Users/leanne/year2sem2/TBA2104/HCG_Dataset/application_train.csv'
    HCG_df = pd.read_csv(data_dir, low_memory=False)

    # print(type(HCG_df))
    find_na(HCG_df)
if __name__ == '__main__':
    main()


