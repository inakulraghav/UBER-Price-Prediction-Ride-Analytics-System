import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings("ignore")

# Data import from mysql server
engine = create_engine(
    "mysql+pymysql://root:Raghav%401234@localhost/IICS"
)
query = "SELECT * FROM data"
df = pd.read_sql(query, engine)


# basic data type change 
df["date"]=pd.to_datetime(df["date"])
df["time"] = df["time"].astype(str).str.split().str[-1]
df["time"]=pd.to_datetime(df["time"])
df["hour"]=df["time"].dt.hour

# filter the dataframe
df=df[df["booking_status"]=="Completed"]
# for i in df.columns:
#     print(df[i].unique())


# finding relation
# sns.scatterplot(x=df["ride_distance"], y=df["booking_value"])
# sns.scatterplot(x=df["avg_ctat"], y=df["booking_value"])
# sns.scatterplot(x=df["avg_vtat"], y=df["booking_value"])
# plt.show()
# print(df[["ride_distance","booking_value"]].describe())



# sns.scatterplot(x=df["ride_distance"], y=df["booking_value"])
# sns.boxplot(df["booking_value"])
# sns.kdeplot(df["booking_value"])
# sns.heatmap(df[["ride_distance","booking_value","hour","avg_ctat"]].corr())
# sns.heatmap(df[["booking_value","ride_distance"]].corr())
# sns.histplot(df["booking_value"])
# plt.show()
# print(df["booking_value"].skew())

# temp=df[df["vehicle_type"]=="Uber XL"]
# temp.info()
# print(temp[["ride_distance","booking_value"]])


# features 
df=df[["vehicle_type","avg_vtat","avg_ctat","booking_value","ride_distance","hour"]]
df = pd.get_dummies(df,columns=["vehicle_type"],drop_first=True)
# df.info()

# for i in df.columns:
#     sns.boxplot(df[i])
#     plt.title(f"{i} details")
#     plt.show()


# df.to_csv("Model.csv",index=False)













