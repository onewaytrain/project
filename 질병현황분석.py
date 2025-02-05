import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')

def data_open(): 

    path = 'pythonDataAnalysis/data/'
    file_list = os.listdir(path)

    df = pd.DataFrame()

    keywords = ['감기', '눈병', '천식', '피부염']

    for i in file_list: 
        if i.endswith('_시도.csv'):
            data = pd.read_csv(path+i, encoding='EUC-KR')

            for key in keywords: 
                if key in i: 
                    data['구분']=key
                    break

            df = pd.concat([df, data])

    sido = pd.read_csv('pythonDataAnalysis\data\시도지역코드.csv', encoding='EUC_kr')

    return df, sido

def datapreprocessing(df, sido):
    data_merge = pd.merge(df, sido, how='left', on='시도지역코드')
    data_merge['년/월'] = data_merge['날짜'].str[:7]
    dfdata = data_merge[data_merge['지역명'] != '전국']
    dfdata.dropna(axis=0,how='any',inplace=True)
    yearmonthdf = data_merge.groupby(['년/월', '구분'], as_index=False)[['발생건수(건)']].mean()

    return yearmonthdf

def visualization(yearmonthdf):

    yearmonthin = input('조회 년/월 입력>> ')
    yearmonthsearch = yearmonthdf[yearmonthdf['년/월']==yearmonthin]

    yearmonthsearch.plot(kind='bar', x='구분', rot=0, title=yearmonthin+' 현황')

    plt.show()


if __name__ == '__main__':
    df, sido = data_open()
    yearmonthdf = datapreprocessing(df, sido)
    visualization(yearmonthdf)
