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

# --- Trip Management Functions ---
def manage_trips_menu():
    """Displays the menu for managing trips."""
    while True:
        print("\n--- Manage Trips ---")
        print("1. Add a New Trip")
        print("2. View All Trips")
        print("3. Edit a Trip")
        print("4. Delete a Trip")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            create_trip()
        elif choice == '2':
            view_trips()
        elif choice == '3':
            edit_trip()
        elif choice == '4':
            delete_trip()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

def create_trip():
    """Adds a new trip to the trips.json file."""
    file_path = "trips.json"
    trips = load_data(file_path)

    trip_id = input("Enter trip ID: ")
    destination = input("Enter destination: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    new_trip = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date
    }

    trips[trip_id] = new_trip
    save_data(file_path, trips)
    print("New trip added successfully!")

def view_trips():
    """Displays all trips saved in the trips.json file."""
    file_path = "trips.json"
    trips = load_data(file_path)

    if not trips:
        print("No trips found.")
    else:
        print("\n--- All Trips ---")
        for trip_id, details in trips.items():
            print(f"Trip ID: {trip_id}")
            print(f"Destination: {details['destination']}")
            print(f"Start Date: {details['start_date']}")
            print(f"End Date: {details['end_date']}")
            print("")