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
def get_rate(vehicle, distance):
    if vehicle == 1:
        if distance <= 50:
            return 5
        elif distance <= 200:
            return 4
        else:
            return 3.5
    elif vehicle == 2:
        if distance <= 50:
            return 10
        elif distance <= 200:
            return 9
        else:
            return 8
    elif vehicle == 3:
        if distance <= 50:
            return 8
        elif distance <= 200:
            return 7
        else:
            return 6
    return 0

def travel_summary(name, distance, vehicle):
    vehicle_name = {1: "Bike", 2: "Car", 3: "Bus"}.get(vehicle, "Unknown")
    rate = get_rate(vehicle, distance)
    fare = distance * rate
    discount = fare * 0.05 if fare > 1500 else 0
    final = fare - discount
    print(f"Passenger Name : {name}")
    print(f"Vehicle Type   : {vehicle_name}")
    print(f"Distance       : {distance:.1f} km")
    print(f"Base Fare      : ₹{fare:.2f}")
    print(f"Discount (5%)  : ₹{discount:.2f}")
    print(f"Total Payable  : ₹{final:.2f}")
    if distance > 500:
        print("Suggestion  : It's better to travel by train or flight for long distances.")

name = input("Enter Passenger Name: ")
distance = float(input("Enter Distance (km): "))
vehicle = int(input("Enter Vehicle Type (1 for Bike, 2 for Car, 3 for Bus): "))
travel_summary(name, distance, vehicle)
