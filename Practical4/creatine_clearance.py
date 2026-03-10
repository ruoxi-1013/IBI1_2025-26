#store input values
age=int(input("Enter your age(year):"))
weight=float(input("Enter your weight(kg):"))
gender=input("Enter your gender:")
Cr=float(input("Enter your creatine concentration(μmol/L):"))
valid_test=True
if age>= 100:
    valid_test=False
    print("Age must be less than 100 years.")
if weight<=20 or weight>=80:
    valid_test=False
    print("Weight must be more than 20kg and less than 80kg.")
if Cr<=0 or Cr>=100:
    valid_test=False
    print("Creatine concentration must be more than 0 μmol/L and less than 100 μmol/L.")
if gender.lower() not in ["male","female"]:
    valid_test=False
    print("Gender must be either 'male' or 'female'.")

if valid_test:
    crcl=((140-age)*weight)/(72*Cr)
    if gender.lower()== "female":
        crcl*=0.85
    print("Creatine clearance(Crcl): "+ str(crcl) +"mL/min")