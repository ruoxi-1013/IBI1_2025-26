#store the heart rate values
heart_rate = [72,60,126,85,90,59,76,131,88,121,64]
#calculate the average value of heart rate
average=round(sum(heart_rate)/len(heart_rate),2)
print("The number of patients is "+str(len(heart_rate))+" and the average heart rate is "+str(average))
#count the number in each category
low=0
normal=0
high=0
for hr in heart_rate:
    if hr<60:
        low+=1
    elif hr>120:
        high+=1
    else:
        normal+=1
categories=["Low","Normal","High"]
count=[low,normal,high]
max_category = categories[count.index(max(count))]
print("Numbers of patients in category:Low:"+str(low)+", Normal:"+str(normal)+", High:"+str(high))
print(f"The most common heart rate category is: {max_category} (n={max(count)})")

#create a pie chart
import matplotlib.pyplot as plt
labels = ["Low", "Normal", "High"]
sizes = [low, normal, high]
colors = ["red", "blue", "yellow"]
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%', startangle=90)
plt.title("disturbance of resting heart rate categories")
plt.tight_layout()
plt.show()