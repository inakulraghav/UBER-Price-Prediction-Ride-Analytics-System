import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from sqlalchemy import create_engine
import warnings 
warnings.filterwarnings("ignore")



# data load and basic walkthrough
df=pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\raw data\ncr_ride_bookings.csv")
# print(df.head().transpose())
# df.info(memory_usage="deep")
# print(df.duplicated().sum())
# print(df.isnull().sum())
# print(df.describe())



#  for checking which status has which type of nan
status=df["Booking Status"].unique()
# for i in status:
#     print("\n")
#     print(i+" "+"details" )
#     print(df.loc[df["Booking Status"]==i].transpose())
#     print("\n")
#     df.loc[df["Booking Status"]==i].info()
#     print("\n")



# after understanding type i fill the nan values and removing extra columns
reasons_column =["Reason for cancelling by Customer","Driver Cancellation Reason","Incomplete Rides Reason"]
df["Cancel_Reason"]="Ride Completed"
df.loc[df["Booking Status"]=="No Driver Found",["Cancel_Reason"]]="Driver Not Found"

for i in reasons_column:
    df.loc[df[i].notna(),["Cancel_Reason"]]=df[i]

df.drop(columns=["Cancelled Rides by Driver","Cancelled Rides by Customer","Incomplete Rides"],inplace=True)
df.drop(columns=reasons_column,inplace=True)

# print(df.isnull().sum())
# print(df["Cancel_Reason"].value_counts())

# for No driver found condition
numericcolumnss= ["Avg VTAT","Avg CTAT","Booking Value","Ride Distance","Driver Ratings","Customer Rating"]
for i in numericcolumnss:
    df.loc[(df["Booking Status"]=="No Driver Found") & (df[i].isna()),i]=0 
df.loc[(df["Booking Status"]=="No Driver Found") & (df["Payment Method"].isna()) ,["Payment Method"]]="Ride is cancelled"

# for Incomplete ride condition
df.loc[(df["Booking Status"]=="Incomplete") & (df["Driver Ratings"].isna()),["Driver Ratings"]]=0 
df.loc[(df["Booking Status"]=="Incomplete") & (df["Customer Rating"].isna()),["Customer Rating"]]=0 

# for cancelled by driver condition
numericcolumns= ["Avg CTAT","Booking Value","Ride Distance","Driver Ratings","Customer Rating"]
for i in numericcolumns:
    df.loc[(df["Booking Status"]=="Cancelled by Driver") & (df[i].isna()) ,i]=0 
df.loc[(df["Booking Status"]=="Cancelled by Driver") & (df["Payment Method"].isna()) ,["Payment Method"]]="Ride is cancelled"

# for cancelled by customer condition
numericcolumns= ["Avg CTAT","Booking Value","Ride Distance","Driver Ratings","Customer Rating"]
for i in numericcolumns:
    df.loc[(df["Booking Status"]=="Cancelled by Customer")& (df[i].isna()),i]=0 
df.loc[(df["Booking Status"]=="Cancelled by Customer")& (df["Payment Method"].isna()),["Payment Method"]]="Ride is cancelled"



# after filling the values check data types 
for i in numericcolumnss:
    df[i]=pd.to_numeric(df[i],downcast="float")

categorycolumn =["Booking Status","Vehicle Type","Payment Method","Cancel_Reason","Pickup Location","Drop Location"]
for i in categorycolumn:
    df[i]=df[i].astype(dtype="category")

df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
df["Time"]=pd.to_datetime(df["Time"],format="%H:%M:%S")
df.columns = df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
df["customer_id"]=df["customer_id"].str.replace('"',' ')
df["booking_id"]=df["booking_id"].str.replace('"',' ')
df["customer_id"]=df["customer_id"].str.strip()
df["booking_id"]=df["booking_id"].str.strip()



# saving the dataset for dashboard 
# engine = create_engine("mysql+mysqlconnector://root:Raghav%401234@localhost:3306/IICS")
# conn = engine.connect()
# print("Connected ✅")
# df.to_sql(name="data", con=engine, if_exists="replace", index=False)



# exploring the dataset for kpis
total_rides= df["booking_id"].nunique()
# print(df["booking_id"].duplicated().sum())

df["booking_id"]=df["booking_id"].drop_duplicates()
df.dropna(subset="booking_id",axis=0,inplace=True)

total_customers=df["customer_id"].nunique()
# print(df["customer_id"].duplicated().sum())

completed_rides=df[df["booking_status"]=="Completed"]["booking_id"].count()
reason=["Cancelled by Driver","Cancelled by Customer"]
cancelled_ride=df[df["booking_status"].isin(reason)]["booking_id"].count()
incomplete_ride=df[df["booking_status"]=="Incomplete"]["booking_id"].count()
driver_not_found=df[df["booking_status"]=="No Driver Found"]["booking_id"].count()
# print(f"total ride: {total_rides} \ntotal customer: {total_customers} \ncompleted rides:{completed_rides}\ncancelled rides:{cancelled_ride}\nincompleted rides: {incomplete_ride}\ndriver not found: {driver_not_found}")

cancellation_rate=cancelled_ride/total_rides*100
dnf_rate=driver_not_found/total_rides*100
incomplete_rate=incomplete_ride/total_rides*100
complete_rate=completed_rides/total_rides*100
# print(f"cancellation rate :{cancellation_rate}\ndriver not found rate:{dnf_rate}\nincomplete ride rates:{incomplete_rate}\ncomplete ride rate:{complete_rate}")

# print(df["cancel_reason"].value_counts())

cancel_rate_cust=df[df["booking_status"]=="Cancelled by Customer"]["booking_id"].count()/cancelled_ride*100
cancel_rate_dri=df[df["booking_status"]=="Cancelled by Driver"]["booking_id"].count()/cancelled_ride*100
# print(f"driver cancel rate :{cancel_rate_dri}\ncustomer cancel rate :{cancel_rate_cust}")

# paymentmethodcount=df["payment_method"].value_counts()
# print(df.groupby("vehicle_type")["booking_value"].sum())

print(f"Data Range Between {df["date"].min()} to {df["date"].max()}")
print(df.head().transpose())
df.info(memory_usage="deep")



