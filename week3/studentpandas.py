import pandas as pd

student={
    "rollno":[1,2,3],
    "name":["sait","wade","swami"],
    "age":[19,21,22],
    "maths":[99,91,87],
    "science":[91,71,87],
    "english":[69,71,67],
  
}
df=pd.read_csv("student.csv")

#total marks
df["total marks"]=df["maths"]+ df["science"]+ df["english"]
#percentage
df["percentage"]=df["total marks"]/3
print(df)

highest=df["total marks"].max()
print("highest marks:",highest)

lowest=df["total marks"].min()
print("lowest marks:",lowest)

average=df["total marks"].mean()
print("average mark",round(average,2))

#sAve csv
df.to_csv("Studentsresults.csv",index=False)
print("Results saved susseccfully")