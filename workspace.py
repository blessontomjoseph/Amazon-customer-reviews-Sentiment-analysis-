# from sentiment_analy.utils import load_data
# stop_data=load_data(r"C:\Users\USER\PycharmProjects\project_1\sentiment_analy\stopwords.txt")
# print(stop_data)
# OrderedDict()=stop_data
# for key, value in od.items():
#     print(key, value)

import pandas as pd
stop_words=['i']
s_W=pd.read_csv(r"C:\Users\USER\PycharmProjects\project_1\sentiment_analy\stopwords.txt")
for i in s_W['i']:
    stop_words.append(i)



def stop_words_import(path_data):
