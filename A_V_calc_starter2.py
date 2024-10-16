# Max Molnar 100746162
# TPRG 2131 Assignment 1 October 15th 2024

#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the web or other sources is properly cited, giving
#full credit to the oringinal author(s).

# This program is a simple area/volume calculator with a prompt for a calculated view (with formula)
# or default view (without formula) with 5 different calculation options to choose from. Prompt the options
# with an input of 1 - 5. Requisite measurments to be prompted in cm, area in cm squared, volume in cm cubed.

import math
print("\nA/V Caclulator Menu \n\nEnter Q/q to quit - Select either will gracefully close the \napplication and cancel the calculated view"
"option if set")

def Rec_area(length, width):
    ''' Function to calculate area of a rectangle '''
    area = length * width #Area of a rectangle formula
    round_area = round(area, 2) #Round to 2 decimal places
    return round_area

def Rec_volume(length, width, height):
    '''Function to calculate volume of a rectangle'''
    volume = length * width * height #Volume of a rectangle formula
    round_volume = round(volume, 2) #Round to 2 decimal places
    return round_volume

def sphere_volume(radius):
    '''Function to calculate volume of a sphere'''
    volume = (4/3) * math.pi * (radius ** 3) #Volume of a sphere formula
    round_volume = round(volume, 2) #Round to 2 decimal places
    return round_volume

def circle_area(radius):
    '''Function to calculate the area of a circle'''
    area = math.pi * (radius **2) #Area of a circle formula
    round_area = round(area, 2) #Round to 2 decimal places
    return round_area

def triangle_area(base, height):
    '''Function to calculate the area of a triangle'''
    area = 0.5 * (base * height) # Area of a triangle formula
    round_area = round(area, 2) #Round to 2 decimal places
    return round_area

#Main loop:
def main_program():
    mode = input("\nEnter V/v to change the calculated view, or D/d for deafault view.") #User input for calculated or default view
    if mode == "Q" or mode == "q": #If user enters Q/q quit the program
        print("\nYou have quit the program. ")
        exit()
    while True:
        try:     # Input Choices: Area of rectangle, volume of rectangle, volume of sphere, Area of circle, area of triangle
            choice_1 = input("\n1. Rectangular Area* Caclulation \n2. Rectangular Volume* Caclulation \n3. Sphereical Volume* Calculation"
                    "\n4. Circular Area* Caclulation \n5. Triangular area* Caclulation " )
            if choice_1 == "1": #User input choice 1
                rlength = float(input("\nWhat is the length in cm ? ")) #Promt user for input
                rwidth = float(input("What is the width in cm ? "))     # ''
                rarea = Rec_area(rlength, rwidth) #Call up area of rectangle function
                if mode == "V" or mode == "v": #Calculated view with formula units in cm provided
                    print("\n", rlength, "\u339D", "*", rwidth, "\u339D",  " = ", rarea, "\u33A0", "(l * w = a)")
                elif mode == "D" or mode == "d": #Default view units in cm provided
                    print("\n", rlength, "\u339D", "*", rwidth, "\u339D", " = ", rarea, "\u33A0")
            elif choice_1 == "2": #User input choice 2
                rlengthv = float(input("\nWhat is the length in cm ? ")) #Prompt user for input
                rwidthv = float(input("What is the Width in cm ? "))     # ''
                rheightv = float(input("What is the height in cm ? "))   # ''
                rvolume = Rec_volume(rlengthv, rwidthv, rheightv) #Call up Rectangle volume function
                if mode == "V" or mode == "v": #Calculated view with formula units in cm provided
                    print("\n", rlengthv, "\u339D", "*", rwidthv, "\u339D", "*", rheightv, "\u339D", "=", rvolume, "\u33A4", "(l * w * h = v)")
                elif mode == "D" or mode == "d": #Default view units in cm provided
                    print("\n", rlengthv, "\u339D", "*", rwidthv, "\u339D", "*", rheightv, "\u339D", "=", rvolume, "\u33A4")
            elif choice_1 == "3": #User input choice 3
                sphere_radius = float(input("\nWhat is the radius in cm ? ")) #Prompt user for input
                svolume = sphere_volume(sphere_radius) #Call up volume of a sphere function
                if mode == "V" or mode == "v": #Calculated view with formula units in cm
                    print("\n4/3 * \u03c0 * ", sphere_radius, "\u339D", "^3 = ", svolume, "\u33A4", "(4/3 * \u03c0 * r^3 = v)")
                elif mode == "D" or mode == "d": #Default view units in cm
                    print("\n4/3 * \u03c0 * ", sphere_radius, "\u339D", "^3 = ", svolume, "\u33A4")
            elif choice_1 == "4": #User input choice 4
                cradius = float(input("\nWhat is the radius in cm ? ")) #Prompt user for input
                carea = circle_area(cradius) #Call up area of a circle function
                if mode == "V" or mode == "v": #Calculated view with formula units in cm
                    print("\n\u03c0", cradius, "\u339D", "^2 = ", carea, "\u33A0",  "(\u03c0 * r ^2 = a)")
                elif mode == "D" or mode == "d": #Default view units in cm
                    print("\n\u03c0", cradius, "\u339D", "^2 = ", carea, "\u33A0")
            elif choice_1 == "5": #User input choice 5
                tbase = float(input("\nWhat is the base in cm ? ")) #Prompt user for input
                theight = float(input("What is the height in cm ? ")) # ''
                tarea = triangle_area(tbase, theight) #Call up are of a triangle function
                if mode == "V" or mode == "v": #Calculated view with formula units in cm
                    print("\n1/2 * ", tbase, "\u339D", "*", theight, "\u339D", "=", tarea, "\u33A0", "(1/2 * b * h = a)")
                elif mode == "D" or mode == "d": #Default view units in cm
                    print("\n1/2 * ", tbase, "\u339D", "*", theight, "\u339D", "=", tarea, "\u33A0")
            elif choice_1 == "Q" or choice_1 == "q": #User input Q/q - Quit the program
                print("\nYou have quit the program. ")
                exit()
    
        except ValueError: #If input is not a number
            print('\nThat is not a number')
            
if __name__ == "__main__":#Main guard for unit testing
    main_program()