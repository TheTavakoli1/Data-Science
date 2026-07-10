import pandas as pd
# read a DataFrame

df = pd.read_csv("test.csv")
# df = pd.read_json("test.json")
# df = pd.read_xml("test.xml")
df = pd.read_excel("test.xlsx")
print(df)


