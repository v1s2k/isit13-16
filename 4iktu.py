
import pandas as pd
x_train=pd.read_csv('http://azuremlsamples.azureml.net/templatedata/PM_train.txt')
x_train.to_csv('train.csv',index=None)
x_train=pd.read_csv('train.csv', sep=" ", header=None)
# train_df = pd.read_csv('train.csv', sep=" ", header=None)
# train_df.drop(train_df.columns[[26, 27]], axis=1, inplace=True)
# train_df.columns = ['id', 'cycle', 'setting1', 'setting2', 'setting3', 's1', 's2', 's3',
#                      's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
#                      's15', 's16', 's17', 's18', 's19', 's20', 's21']

x_train.drop([27,26], inplace=True, axis=1)


x_test=pd.read_csv('http://azuremlsamples.azureml.net/templatedata/PM_train.txt')
x_test.to_csv('test.csv',index=None)
x_test=pd.read_csv('test.csv', sep=" ", header=None)

x_test.drop([27,26], inplace=True, axis=1)


x_truth=pd.read_csv('http://azuremlsamples.azureml.net/templatedata/PM_train.txt')
x_truth.to_csv('true.csv',index=None)
x_truth=pd.read_csv('true.csv', sep=" ", header=None)

x_truth.drop([27,26], inplace=True, axis=1)