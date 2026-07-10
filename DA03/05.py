import pandas as pd

# Convert a DataFrame
df = pd.read_csv("test.csv")

df.to_excel("convert_file.xlsx")
df.to_json("convert_file.json")
df.to_xml("convert_file.xml")