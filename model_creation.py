import pandas as pd
import numpy as n
from sklearn import preprocessing 

df1=pd.read_csv("s3://finalproject25/archive/z.csv/part-00000-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df2=pd.read_csv("s3://finalproject25/archive/z.csv/part-00001-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df3=pd.read_csv("s3://finalproject25/archive/z.csv/part-00002-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df4=pd.read_csv("s3://finalproject25/archive/z.csv/part-00003-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df5=pd.read_csv("s3://finalproject25/archive/z.csv/part-00004-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df6=pd.read_csv("s3://finalproject25/archive/z.csv/part-00005-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df7=pd.read_csv("s3://finalproject25/archive/z.csv/part-00006-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df8=pd.read_csv("s3://finalproject25/archive/z.csv/part-00007-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])
df9=pd.read_csv("s3://finalproject25/archive/z.csv/part-00008-9c6a1954-bb3b-4dbe-896c-c0f11787d68e-c000.csv",names=["flow_id","src_ip","src_port","dst_ip","dst_port","`timestamp`","flow_duration","tot_fwd_pkts","tot_bwd_pkts","totLen_fwd_pkts","totLen_bwd_pkts","fwd_pkts_per_s","bwd_pkts_per_s","label"])

df1=df1.append(df2)
del df2
df1=df1.append(df3)
del df3
df1=df1.append(df4)
del df4
df1=df1.append(df5)
del df5
df1=df1.append(df6)
del df6
df1=df1.append(df7)
del df7
df1=df1.append(df8)
del df8
df1=df1.append(df9)
del df9

df=df1
del df1

print(df.head())

label = preprocessing.LabelEncoder()
df["label"] = label.fit_transform(list(df["label"].values))

Y = df['label']
X = df.drop("label",axis=1).drop("`timestamp`",axis=1).drop("flow_id",axis=1).drop("src_ip",axis=1).drop("dst_ip",axis=1)
print(X.columns)
print(df.shape)
print(X.shape)
print(Y.shape)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train, y_train)

# print(y_test)
# print(x_test)


y_pred = model.predict(X_test)
print(y_pred)

print(label.inverse_transform(y_pred))

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("accuracy:",accuracy)

from sklearn.metrics import f1_score
f1_score(y_test, y_pred)


<<<<<<< HEAD
=======
import pickle
import boto3

s3_resource = boto3.resource('s3')
bucket='finalproject25'
key= 'final_model.pkl'
pickle_byte_obj = pickle.dumps(model)
s3_resource.Object(bucket,key).put(Body=pickle_byte_obj)
>>>>>>> f5f2ded3edade28ccd454634e42c78e089026c7c
