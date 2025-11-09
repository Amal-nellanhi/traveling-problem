# ✈️Travel Cost & Distance Calculator

This repository is part of a Git Workshop demonstration.  
It contains a simple Python program that calculates travel cost based on distance and vehicle type.

## 📒Problem Statement

Write a program to:
- Input passenger name, distance (in km), and vehicle type (1 → Bike, 2 → Car, 3 → Bus)
- Calculate total cost using the following rates:

| Distance (km) | Bike (₹/km) | Car (₹/km) | Bus (₹/km) |
|---------------|--------------|-------------|-------------|
| 0–50          | 5            | 10          | 8           |
| 51–200        | 4            | 9           | 7           |
| Above 200     | 3.5          | 8           | 6           |

## 🅰️Additional Conditions
- Apply a 5% discount if total cost > ₹1500  
- If distance > 500 km, show: *"It's better to travel by train or flight for long distances."*

## ✨Purpose
This repository is created to demonstrate Git and GitHub workflows during a hands-on workshop session.

## ⌨️Sample Input
```bash
Name of Passenger: Alice
Distance to travel (km): 240
Vehicle Type (1 for Bike, 2 for Car, 3 for Bus): 2
```

## 🔳Sample Output
```bash
Passenger Name: Alice
Vehicle Type: Car
Distance Traveled: 240 km
Base Fare: 1920
Discount: 96
Final Amount Payable: 1824
Travel Suggestion:
```
