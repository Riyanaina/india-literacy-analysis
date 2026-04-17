import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#--> Load file (Literacy data)
df = pd.read_csv("2011_literacy_data.csv")
#print(df)

#------------> Literacy data analysis :-

# Removing unwanted columns
df = df.drop(columns=["1991 - Male","1991 - Female","1991 - Persons","2001 - Male","2001 - Female","2001 - Persons","2011 - Rural - Person","2011 - Urban - Persons"])
#print(df)

# Renaming columns 
df.columns = [
    "States",
    "Rural_male",
    "Rural_female",
    "Urban_male",
    "Urban_female"
]
#print(df)

# Removing unwanted states
remove_states =["All India",
                "A. and N. Islands",
                "D. and N. Haveli",
                "Daman and Diu",
                "Lakshadweep",
                "Puducherry"
                ]

df = df[~df["States"].isin(remove_states)]
#print(df)

#--> Graph (Total literacy)

df["Total"] = df["Rural_male"] + df["Rural_female"] + df["Urban_male"] + df["Urban_female"]
df = df[["States","Total"]]

plt.style.use('ggplot')
plt.figure(figsize=(14,7))

df.sort_values("Total", ascending=False).plot(x="States",y="Total",kind="bar",color="purple",legend=False)
plt.xticks(rotation=90, ha='right')
plt.title("Total literacy Rate by states", fontsize=14, fontweight='bold')
plt.xlabel("States", fontsize=12)
plt.ylabel("Literacy Rate", fontsize=12)
plt.tight_layout()
plt.show()

# Extra work [ differentiate between ] (not for project work, for learning)

#--> Graph (Rural vs urban literacy)

df["Rural"] = df["Rural_male"] + df["Rural_female"]
df["Urban"] = df["Urban_male"] + df["Urban_female"]
#print(df[["States","Rural","Urban"]])

plt.style.use('ggplot')
plt.figure(figsize=(14,7))

df.plot(x="States", y=["Rural","Urban"],kind="bar",legend=False)
plt.xticks(rotation=90)
plt.title("Rural vs Urban Literacy Rate in State-wise")
plt.xlabel("States")
plt.ylabel("Literacy rate")
plt.tight_layout()
plt.show()

#--> Graph (Male vs female literacy)

df["Male"] = df["Rural_male"] + df["Urban_male"]
df["Female"] = df["Rural_female"] + df["Urban_female"]
#print(df[["States","Male","Female"]])

plt.style.use('ggplot')
plt.figure(figsize=(14,7))

df.plot(x="States", y=["Male","Female"],kind="bar", legend=False)
plt.xticks(rotation=90)
plt.title("Male vs Female Literacy Rate in State-wise")
plt.xlabel("States")
plt.ylabel("Literacy rate")
plt.tight_layout()
plt.show()
