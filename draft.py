import pandas as pd

list_excel = pd.read_excel('change.xlsx')
format_str = str(list_excel)
delete_str = format_str.replace("Columns:",  "").replace("Empty DataFrame", "").replace("[", "").replace("]", "").replace("Index:", "")

print(delete_str)
