w=int(input("enter your weight in kg"))
h=float(input("enter your height in m"))
H=float(h*h)
BMI=w/H
print("your BMI is:", BMI)
if BMI < 18.5 :
    print("you are in the UNDER WEIGHT range")
elif 18.5<=BMI<=24.9:
     print("you are in the NORMAL range")
elif 25<=BMI<=29.9:
   print("you are in the OVER WEIGHT range")
else :
   print("you are in the OBESE range")





