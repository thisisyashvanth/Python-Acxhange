import pandas as pd

df = pd.read_csv("student_habits_performance(in).csv")



# Basics

# print(df.head(10))
# print()
# print(df.shape)
# print()
print(df.columns)
print()
print(df.describe(include="all"))
print()
# print(df["netflix_hours"].describe())
# print()
# print(df.info())
# print()
# print(df.isna().sum())
# print()




# Correlation

# Types: Default (Pearson) -> Linear Relationships, Spearman -> Monotonic (Rank Based, Handles Non-Linear Better), Kendall -> Similar to Spearman, Robust for Small Sata

# print(df.select_dtypes(include="number").corr() > 0.7)
# print(df["age"].corr(df["social_media_hours"]))



# Handling Missing Data

# Dropping Values
# df_dropped = df.copy()
# df_dropped.dropna(inplace=True)
# print(df_dropped.shape)

# # Filling Values
# # With Average (Numeric Columns)
# df_filled = df.copy()
# df_filled.fillna(df.mean(numeric_only=True), inplace=True)
# df_filled.fillna(df.mode().iloc[0], inplace=True)
# print(df_filled.isna().sum())

