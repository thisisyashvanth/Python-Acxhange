# # Series - One-Dimensional Labeled Data.
# # DataFrame - Table with Rows + Columns.

import pandas as pd
import numpy as np

# # NUMPY

# marks = np.array([90, 80, 70])
# print(marks)
# print(type(marks))
# print()


# # PANDAS

# Series
# yashvanth = ["Yashvanth", 100, 90, 80, "Pass"]
# yashvanth_series = pd.Series(yashvanth, name="Yashvanth Data")
# print(yashvanth_series)
# print()

# ismail = ["Ismail", 90, 80, 100, "Pass"]
# ismail_series = pd.Series(ismail, name="Ismail Data")
# print(ismail_series)
# print()

# yashvanth_series_with_index = pd.Series(yashvanth, name="Yashvanth Data with Index", index=["Name", "Maths", "Science", "English", "Result"])
# print(yashvanth_series_with_index)
# print()

# ismail_series_with_index = pd.Series(ismail, name="Ismail Data with Index", index=["Name", "Maths", "Science", "English", "Result"])
# print(ismail_series_with_index)
# print()

# # Using Dict gives auto index using Key's
# yashvanth_dict = {
#     "Name": "Yashvanth",
#     "Maths": 100,
#     "Science": 90,
#     "English": 80,
#     "Result": "Pass"
# }
# yashvanth_dict_series = pd.Series(yashvanth_dict, name="Series from Dictionary")
# print(yashvanth_dict_series)
# print()


# DataFrame
data = {
    "Name": ["Yashvanth", "Ismail"],
    "Maths": [100, 90],
    "Science": [90, 100],
    "English": [80, 90],
    "Result": ["Pass", "Pass"]
}

dataframe = pd.DataFrame(data)
print(dataframe)
print()

# print(dataframe[["Maths", "Science", "English"]].max())
# print()
# print(dataframe[["Maths", "Science", "English"]].mean())
# print()

dataframe["Average"] = dataframe[["Maths", "Science", "English"]].mean(axis=1)
print(dataframe)
print()

def assign_grades(avg):
    return round(avg/10)

dataframe["Grade"] = dataframe["Average"].apply(assign_grades)
print(dataframe)
print()