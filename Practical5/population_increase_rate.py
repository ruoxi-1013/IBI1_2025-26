#store the initial data
countries=["UK","China","Italy","Brazil","USA"]
p2020=[66.7,1426,59.4,208.6,331.6]
p2024=[69.2, 1410,58.9,212.0,340.1]
#calculate the percentage change of each population
percent_change=[]
for p20,p24 in zip(p2020,p2024):
    change = (p24 - p20) / p20 * 100
    percent_change.append(round(change, 2))
print("Percentage population changes for each countries:")
for country,change in zip(countries,percent_change):
    print(str(country)+":"+str(change))
#print in descending order
sort_change=sorted(zip(countries, percent_change), reverse=True)
print("Population changes of each countries in descending order:")
for country,change in zip(countries,sort_change):
    print(str(country)+":"+str(change)+"%")
max_inc_country = sort_change[0][0]
max_dec_country = sort_change[-1][0]
print("The country with the largest increase: "+str(max_inc_country))
print("The country with the largest decrease: "+str(max_dec_country))
#create the bar chart
import matplotlib.pyplot as plt
plt.bar(countries, percent_change, color="blue")
plt.xlabel("Countries")
plt.ylabel("Population change")
plt.title("population change for each country")
plt.show()