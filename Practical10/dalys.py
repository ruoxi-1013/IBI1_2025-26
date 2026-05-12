import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/23321/Desktop/IBI/IBI1_2025-26/IBI1_2025-26/Practical10")

print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show first 5 rows
print("\nFirst 5 rows:")
print(dalys_data.head(5))

# Show dataframe info
print("\nDataframe info:")
dalys_data.info()

# Show descriptive statistics
print("\nData description:")
print(dalys_data.describe())

# Show first 10 rows, Year (column 2) and DALYs (column 3)
print("\nFirst 10 rows: Year and DALYs")
print(dalys_data.iloc[0:10, [2, 3]])

# Max DALYs in Afghanistan's first 10 years
afghanistan_first10 = dalys_data.iloc[0:10, [2, 3]]
max_year_afg = afghanistan_first10.loc[afghanistan_first10.iloc[:, 1].idxmax()]
print("\nAfghanistan first 10 years max DALYs year:", max_year_afg["Year"])

zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print("\nZimbabwe data (first 5 rows):")
print(zimbabwe_data.head())

# First and last year for Zimbabwe
first_year_zim = zimbabwe_data["Year"].min()
last_year_zim = zimbabwe_data["Year"].max()
print("\nZimbabwe data range: from", first_year_zim, "to", last_year_zim)

recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_country = recent_data.loc[recent_data["DALYs"].idxmax()]["Entity"]
min_country = recent_data.loc[recent_data["DALYs"].idxmin()]["Entity"]

print("\n2019 Max DALYs country:", max_country)
print("2019 Min DALYs country:", min_country)

# Plot country with maximum DALYs in 2019
country_max = dalys_data.loc[dalys_data["Entity"] == max_country]

plt.figure(figsize=(10, 5))
plt.plot(country_max["Year"], country_max["DALYs"], 'bo-', linewidth=2, markersize=6)
plt.title(f"DALYs over time in {max_country}")
plt.xlabel("Year")
plt.ylabel("DALYs (per capita / all causes)")
plt.xticks(country_max["Year"], rotation=-90)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Question: Which countries had DALYs < 18000 in any single year?
low_dalys = dalys_data.loc[dalys_data["DALYs"] < 18000]
low_dalys_countries = low_dalys["Entity"].unique()
# Print results
print("Countries with DALYs less than 18,000 in at least one year:")
for country in low_dalys_countries:
    print("-", country)

# Show the actual records for verification
print("\nFull records with DALYs < 18000:")
print(low_dalys[["Entity", "Year", "DALYs"]])