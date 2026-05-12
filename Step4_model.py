from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import (RandomForestRegressor, GradientBoostingRegressor)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np


# data load 
df=pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Projects\IICS\Feature engineering\Model.csv")


# split the data 
x= df.drop("booking_value", axis=1)
y = df["booking_value"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


# standardization
ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)


# Models
# models = {"Linear Regression": LinearRegression(),
#           "Decision Tree": DecisionTreeRegressor(random_state=42),
#           "Random Forest": RandomForestRegressor(n_estimators=100,random_state=42),
#           "KNN": KNeighborsRegressor(),
#           "xgb booster": XGBRegressor(),
#           "Gradient Boosting": GradientBoostingRegressor(random_state=42)}

# results = []

# for name, model in models.items():
#     model.fit(x_train, y_train)
#     y_pred = model.predict(x_test)
#     mse = mean_squared_error(y_test, y_pred)
#     rmse = np.sqrt(mse)
#     mae = mean_absolute_error(y_test, y_pred)
#     r2 = r2_score(y_test, y_pred)
#     results.append({"Model": name,
#                     "MSE": round(mse, 2),
#                     "RMSE": round(rmse, 2),
#                     "MAE": round(mae, 2),
#                     "R2 Score": round(r2, 4)
#     })

# results_df = pd.DataFrame(results)

# results_df = results_df.sort_values(by="R2 Score",ascending=False)
# print(results_df)



model=LinearRegression()
model.fit(x_train,y_train)


# y_pred=model.predict(x_train)
# print(r2_score(y_train,y_pred))

# plt.plot(y_train,y_train)
# plt.scatter(y_train,y_pred)
# plt.show()

# pred_y=model.predict(x_test)
# print(r2_score(y_test,pred_y))

# plt.plot(y_test,pred_y)
# plt.scatter(y_test,y_test)
# plt.show()



# Save model
joblib.dump(model, 'uber_model.pkl')
joblib.dump(ss, 'scaler.pkl')
joblib.dump(x.columns.tolist(), 'features_list.pkl')



