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

def edit_trip():
    """Edits an existing trip in the trips.json file."""
    file_path = "trips.json"
    trips = load_data(file_path)

    trip_id = input("Enter the Trip ID to edit: ")

    if trip_id in trips:
        print("Editing trip details. Leave blank to keep the current value.")
        destination = input(f"Enter new destination (current: {trips[trip_id]['destination']}): ") or trips[trip_id]['destination']
        start_date = input(f"Enter new start date (current: {trips[trip_id]['start_date']}): ") or trips[trip_id]['start_date']
        end_date = input(f"Enter new end date (current: {trips[trip_id]['end_date']}): ") or trips[trip_id]['end_date']

        trips[trip_id] = {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date
        }

        save_data(file_path, trips)
        print("Trip updated successfully!")
    else:
        print("Trip ID not found.")

def delete_trip():
    """Deletes a trip from the trips.json file."""
    file_path = "trips.json"
    trips = load_data(file_path)

    trip_id = input("Enter the Trip ID to delete: ")

    if trip_id in trips:
        del trips[trip_id]
        save_data(file_path, trips)
        print("Trip deleted successfully!")
    else:
        print("Trip ID not found.")

# --- Itinerary Management Functions ---
def manage_itinerary_menu():
    """Displays the menu for managing the itinerary."""
    while True:
        print("\n--- Manage Itinerary ---")
        print("1. Add an Itinerary Item")
        print("2. View Itinerary")
        print("3. Edit an Itinerary Item")
        print("4. Delete an Itinerary Item")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            add_itinerary_item()
        elif choice == '2':
            view_itinerary()
        elif choice == '3':
            edit_itinerary_item()
        elif choice == '4':
            delete_itinerary_item()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

def add_itinerary_item():
    """Adds an itinerary item to the itinerary.json file."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    item_id = input("Enter item ID: ")
    trip_id = input("Enter the Trip ID: ")
    date = input("Enter date (YYYY-MM-DD): ")
    activity = input("Enter activity: ")

    new_item = {
        "trip_id": trip_id,
        "date": date,
        "activity": activity
    }

    itinerary[item_id] = new_item
    save_data(file_path, itinerary)
    print("New itinerary item added successfully!")

def view_itinerary():
    """Displays all itinerary items."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    if not itinerary:
        print("No itinerary items found.")
    else:
        print("\n--- Itinerary ---")
        for item_id, details in itinerary.items():
            print(f"Item ID: {item_id}")
            print(f"Trip ID: {details['trip_id']}")
            print(f"Date: {details['date']}")
            print(f"Activity: {details['activity']}")
            print("")

def edit_itinerary_item():
    """Edits an existing itinerary item."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    item_id = input("Enter the Item ID to edit: ")

    if item_id in itinerary:
        print("Editing itinerary item details. Leave blank to keep the current value.")
        trip_id = input(f"Enter new Trip ID (current: {itinerary[item_id]['trip_id']}): ") or itinerary[item_id]['trip_id']
        date = input(f"Enter new date (current: {itinerary[item_id]['date']}): ") or itinerary[item_id]['date']
        activity = input(f"Enter new activity (current: {itinerary[item_id]['activity']}): ") or itinerary[item_id]['activity']

        itinerary[item_id] = {
            "trip_id": trip_id,
            "date": date,
            "activity": activity
        }

        save_data(file_path, itinerary)
        print("Itinerary item updated successfully!")
    else:
        print("Item ID not found.")

def delete_itinerary_item():
    """Deletes an itinerary item."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    item_id = input("Enter the Item ID to delete: ")

    if item_id in itinerary:
        del itinerary[item_id]
        save_data(file_path, itinerary)
        print("Itinerary item deleted successfully!")
    else:
        print("Item ID not found.")

# --- Expenses Management Functions ---
def manage_expenses_menu():
    """Displays the menu for managing expenses."""
    while True:
        print("\n--- Manage Expenses ---")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Edit an Expense")
        print("4. Delete an Expense")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            edit_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

def add_expense():
    """Adds a new expense to the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    expense_id = input("Enter expense ID: ")
    trip_id = input("Enter the Trip ID: ")
    amount = input("Enter the amount: ")
    category = input("Enter the category (e.g., food, transport): ")
    description = input("Enter a description: ")

    new_expense = {
        "trip_id": trip_id,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses[expense_id] = new_expense
    save_data(file_path, expenses)
    print("New expense added successfully!")
