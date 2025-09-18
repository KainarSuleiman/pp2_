weight = int(input("Enter weight in killograms: "))
height = int(input("Enter height in metres: "))
Body_Mass_Index = weight/height**2

if Body_Mass_Index < 1.85:
    print("Underweght")
elif Body_Mass_Index < 1.85 and Body_Mass_Index < 24.9:
    print("Normal weight")
elif Body_Mass_Index < 24.9: