import pandas as pd

df = pd.read_csv("diabetes_dataset(in).csv")

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.size)
# print(df.shape)

print(df.isna().sum())

col_with_null_values = [i for i in df.columns if df[i].isna().sum() > 0]

for i in col_with_null_values:
    # print(f"{i}: {df[i].dtype}")
    
    if df[i].dtype in ['int64', 'float64']:
        df[i].fillna(df[i].mean(), inplace=True)
    else:
        # df[i] = df[i].astype(str)
        if not df[i].mode().empty:
            df[i] = df[i].fillna(df[i].mode()[0])
        else:
            df[i] = df[i].fillna("Unknown")

print()
print()
print()
print()
print()
print(df.isna().sum())


# mode = df["Alcohol_Consumption"].mode()[0]
# df["Alcohol_Consumption"] = df["Alcohol_Consumption"].fillna(mode)
# print(df.isna().sum())

