#store input values
initial_infected=int(input("Enter the initial number of infected students:"))
growth_rate=float(input("Enter the daily growth rate:"))
current_infected=initial_infected
#store the number of days
day=1
#continue while the number fewer than 91 students are infected
while current_infected<91: #continue when the number of infected students less than 91
    current_infected=current_infected*(1+growth_rate)#Calculate thenumber of infected students
    day+=1
    if current_infected>91: #the number of infected students must not exceed 91
        current_infected=91
    print(f"Day{day}:{current_infected:.0f}") #print daily infected numbers
    
print(f"All students infected in {day-1} days.")#final results