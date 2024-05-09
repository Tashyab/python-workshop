import pandas as pd

df = pd.read_excel(r"C:\Users\Acer\Downloads\Copy of csn_version2_imported_tashyab.xlsx")

# links = df.iloc[:, 5].values
# with open("duplicate_links.txt", "+w") as f:
#     for link in links:
#         f.write(link + "\n")

with open("duplicate_links.txt") as f:
    link_text = f.read()
import re
duplicate_list = []
link_list = df.iloc[: , 5].values

for i, link in enumerate(link_list):
    x = re.findall(link, link_text)
    if len(x)>1:
       duplicate_list.append(i+2)

print(duplicate_list)
print(re.findall(link_list[1001], link_text))

    
