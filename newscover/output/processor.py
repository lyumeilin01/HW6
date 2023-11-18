import json
from pathlib import Path
import pandas as pd

def get_df(file_name):
  path1 = Path(__file__).parent / file_name
  source_name = []
  title = []
  description = []
  with open(path1, 'r') as file:
      data1 = json.load(file)
      #checked to see there are 100 articles in each file
      #print(len(data1))
      for i in range (0, 100):
          source_name.append(data1[i]["source"]["name"])
          title.append(data1[i]["title"])
          description.append(data1[i]["description"])
  df = pd.DataFrame({
      'src_name': source_name,
      'title': title,
      'description': description
  })
  return df

df1 = get_df("swift1.json")
df2 = get_df("swift2.json")
df3 = get_df("swift3.json")
df4 = get_df("swift4.json")
df5 = get_df("swift5.json")

final_df = pd.concat([df1,df2,df3,df4,df5], ignore_index=True)
print(final_df)

excel_file_path = 'output.xlsx'
final_df.to_excel(excel_file_path, index=False)