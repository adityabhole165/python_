import pandas as pd
import numpy as np
# df_titanic=pd.read_csv("book2.csv")
# print(df_titanic)
# print(df_titanic.head())
# print(df_titanic["name"].str.lower())
# print(df_titanic["name"].str.contains("Mrs"))
# df_titanic["bool_Mrs"]=df_titanic["name"].str.contains("Mrs")
# print(df_titanic)
# print(df_titanic["bool_Mrs"].mean())
# gender_count=df_titanic["sex"].value_counts()
# print(gender_count)

# df_numeric=df_titanic[["age","fare"]]
# print(df_numeric)
# df_numeric["ceil_fare"]=df_numeric.fare.apply(np.ceil)
# print(df_numeric)

df = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['A', 'B', 'C'])
print(df)