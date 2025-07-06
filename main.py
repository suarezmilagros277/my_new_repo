import pandas as pd


my_list = ["Joli", "Alicia", "Francisco", "Chico"]

df = pd.DataFrame(my_list, columns=["Names"])

print(df)