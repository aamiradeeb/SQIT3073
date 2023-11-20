import os
#mac 
os.system('clear') 
#window
#os.system('cls') 

import perimeter
import area
import volume

while True:
    print("1: Polygon Perimeter")
    print("2: Area")
    print("3: Volume")
    print("4: Quit")
    choice = input("Select an operation: ")

    if choice == '1':
        print("1: Rectangle")
        print("2: Square")
        print("3: Triangle")
        sub_choice = input("Select a shape: ")
        if sub_choice == '1':
            length = float(input("Enter length (cm): "))
            width = float(input("Enter width (cm): "))
            print("Perimeter:", perimeter.rectangle_perimeter(length, width))
        elif sub_choice == '2':
            side = float(input("Enter side (cm): "))
            print("Perimeter:", perimeter.square_perimeter(side))
        elif sub_choice == '3':
            a = float(input("Enter side a (cm): "))
            b = float(input("Enter side b (cm): "))
            c = float(input("Enter side c (cm): "))
            print("Perimeter:", perimeter.triangle_perimeter(a, b, c))

    elif choice == '2':
        print("1: Rectangle")
        print("2: Square")
        print("3: Triangle")
        sub_choice = input("Select a shape: ")
        if sub_choice == '1':
            length = float(input("Enter length (cm) : "))
            width = float(input("Enter width (cm) : "))
            print("Area:", area.rectangle_area(length, width))
        elif sub_choice == '2':
            side = float(input("Enter side (cm): "))
            print("Area:", area.square_area(side))
        elif sub_choice == '3':
            base = float(input("Enter base (cm): "))
            height = float(input("Enter height (cm) : "))
            print("Area:", area.triangle_area(base, height))

    elif choice == '3':
        print("1: Rectangular Prism")
        print("2: Cube")
        sub_choice = input("Select a shape: ")
        if sub_choice == '1':
            length = float(input("Enter length (cm): "))
            width = float(input("Enter width (cm): "))
            height = float(input("Enter height (cm) : "))
            print("Volume:", volume.rectangular_prism_volume(length, width, height))
        elif sub_choice == '2':
            side = float(input("Enter side (cm) : "))
            print("Volume:", volume.cube_volume(side))

    elif choice == '4':
        break

    else:
        print("Invalid choice. Try again.")

    input("Press enter to continue...")

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my