# BMI CALCULATOR

print("BMI CALCULATOR\n")

w = float(input("Enter a weight in 'kilogram' unit :- "))
h = float(input("Enter a height in 'meter' unit :- "))

#BMI CALCULATION - BMI = Weight (in kg)/(Height (in meter))**2

BMI = w/(h**2)
print(f"Your BMI value is :- {BMI:.2f}")


#Now Compare the BMI Categories
if BMI<18.5:
	print("You are Underweight.")
	
elif 18.5<=BMI<=24.9:
	print("You are Normal weight.")
	
elif 25<=BMI<=29.9:
	print("You are Overweight.")

elif 30<=BMI<=34.9:
	print("You are Obese (Class I).")
	
elif 35<=BMI<=39.9:
	print("You are Obese (Class II).")

else:
	print("You are Obese (Class III).")