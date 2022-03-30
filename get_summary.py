import pandas as pd
#load data and assign it
surveys_df = pd.read_csv("surveys.csv")

desc_weight = surveys_df["weight"].describe()
print(desc_weight)

