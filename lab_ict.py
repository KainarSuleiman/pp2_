#task 1

weight= int(input("Enter weight in killograms: "))
height= float(input("Enter height in meters: "))
Body_Mass_Index = weight/ height**2
print(Body_Mass_Index)

print("======================")

if Body_Mass_Index < 1.85:
    print("Body_Mass_Index is underweight")
elif Body_Mass_Index > 1.85 and Body_Mass_Index < 24.9:
    print("Body_Mass_Index is Normal Weight")
elif Body_Mass_Index > 25 and Body_Mass_Index < 29.9:
    print("Body_Mass_Index is Overweight")
else:
    print("Body_Mass_Index is Obesity")








