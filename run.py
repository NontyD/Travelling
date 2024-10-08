import json
import os

def main_menu():
    """Displays the main menu and routes to different modules."""
    while True:
        print("\n--- Travel Itinerary Planner ---")
        print("1. Manage Trips")
        print("2. Manage Itinerary")
        print("3. Track Expenses")
        print("4. Manage Packing List")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            manage_trips_menu()
        elif choice == '2':
            manage_itinerary_menu()
        elif choice == '3':
            manage_expenses_menu()
        elif choice == '4':
            manage_packing_menu()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")
