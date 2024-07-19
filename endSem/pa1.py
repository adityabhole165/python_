import pandas as pd

df_grades=pd.read_csv("book1.csv")

# print(df_grades.shape)
# print(df_grades.tail(3))
# print(df_grades)
# print(df_grades.head(3))
# print(df_grades.dtypes)
# print(df_grades.columns)
# print(df_grades.index)
# print(df_grades[["name","mini_exam1","participatipon"]])
# data=df_grades["name"]
# print(data)
# print(df_grades.name[4:7]) #contigious slide
# print(df_grades.name[7]) #sigle element
# print(df_grades.name[[1,3,6]]) # arbitary slice
# print(df_grades.loc[0,:])
print(df_grades.head())




