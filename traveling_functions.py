# GIT WORKSHOP PROBLEM

'''Problem Statement: “Travel Cost & Distance Calculator”
Objective

Write a program to calculate the total travel cost and provide useful travel-related feedback based on the-
distance (in kilometers) a person plans to travel.
Use if - else conditions effectively to handle different distance ranges and rate conditions.

Requirements
The program should input:
Name of the passenger
Distance to travel (in kilometers)
Vehicle type:

1 → Bike
2 → Car
3 → Bus

Use the following rate per kilometer:
________________________________________________________________
| Distance Range (km) | Bike (₹/km) |	Car (₹/km)| Bus (₹/km) |
================================================================
|      0 - 50	      |       5	    |     10      |     8      |
|      51 - 200	      |       4	    |     9       | 	7      |
|     Above 200	      |      3.5	|     8	      |     6      |
================================================================

****Apply additional rules:****

If the total cost exceeds ₹1500, apply a 5% discount.

If the distance exceeds 500 km, display a suggestion:
“It's better to travel by train or flight for long distances.”

Display:

Passenger name
Vehicle type
Distance traveled
Base fare
Discount (if any)
Final amount payable
Any travel suggestion

'''
#==================================================================
#  SAMPLE INPUT
# Enter Passenger Name: Alan 
# Enter Distance (km): 620
# Enter Vehicle Type (1 for Bike, 2 for Car, 3 for Bus): 2

#===================================================================

# SAMPLE OUTPUT
# Passenger Name : Alan 
# Vehicle Type: Car 
# Distance : 620.0 km 
# Base Fare: 4960.00 
# Discount (5%) : 248.00
# Total Amount Payable : ₹4712.00
# Suggestion: It's better to travel by train or flight for long distances.
#=========================================================================

def find_type(vehicle):
    if vehicle == 1:
        return 'Bike'
    elif vehicle == 2:
        return 'Car'
    elif vehicle == 3:
        return 'Bus'
def findFare (vehicle):
    if(vehicle == 1):
        if 0<= distance <= 50:
            rate = 5
        elif 51<= distance <= 200:
            rate = 4
        elif distance > 200:
            rate = 3.5
        fare = distance * rate

    elif(vehicle == 2):
        if 0<= distance <= 50:
            rate = 10
        elif 51<= distance <= 200:
            rate = 9
        elif distance > 200:
            rate = 8
        fare = distance * rate
    elif(vehicle == 3):
        if 0<= distance <= 50:
            rate = 8
        elif 51<= distance <= 200:
            rate = 7
        elif distance > 200:
            rate = 6
        fare = distance * rate
    return fare


name = input("Enter passenger Name:")
distance = float(input("Enter Distance (km)"))
vehicle = int(input("Enter Vehicle Type (1 for Bike, 2 for Car, 3 for Bus):"))
type = find_type(vehicle)
fare = findFare(vehicle)
if distance > 500:
    flag = 1
if fare > 1500:
    discount = fare * 0.05
    t_fare = fare - discount
print(f"Passenger Name : {name} ") 
print(f"Vehicle Type: {type}")
print(f"Distance: {distance} km") 
print(f"Base Fare: {fare}") 
print(f"Discount (5%) : {discount}")
print(f"Total Amount Payable :₹{t_fare}")
if flag == 1:
    print("Suggestion: It's better to travel by train or flight for long distances.")