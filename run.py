import json
import os
import re
from datetime import datetime

def load_data(file_path):
    """Loads data from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

def save_data(file_path, data):
    """Saves data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

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
    """Adds a new trip to the trips.json file with input validation."""
    file_path = "trips.json"
    trips = load_data(file_path)

    # Validate trip ID
    while True:
        trip_id = input("Enter trip ID: ").strip()
        if trip_id and trip_id not in trips:
            break
        print("Invalid trip ID or trip ID already exists. Please try again.")

    # Validate destination
    destination = input("Enter destination: ").strip()
    while not destination:
        print("Destination cannot be empty.")
        destination = input("Enter destination: ").strip()

    # Validate start date
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        if validate_date_format(start_date):
            break
        print("Invalid date format. Please enter the date as YYYY-MM-DD.")

    # Validate end date
    while True:
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        if validate_date_format(end_date):
            # Ensure the end date is after the start date
            if validate_date_order(start_date, end_date):
                break
            else:
                print("End date must be after the start date.")
        else:
            print("Invalid date format. Please enter the date as YYYY-MM-DD.")

    new_trip = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date
    }

    trips[trip_id] = new_trip
    save_data(file_path, trips)
    print("New trip added successfully!")

def validate_date_format(date_str):
    """Validates if the given date string matches the YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_date_order(start_date, end_date):
    """Validates that the end date is after the start date."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return end > start

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

def view_expenses():
    """Displays all the expenses saved in the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    if not expenses:
        print("No expenses found.")
    else:
        print("\n--- All Expenses ---")
        for expense_id, details in expenses.items():
            print(f"Expense ID: {expense_id}")
            print(f"Trip ID: {details['trip_id']}")
            print(f"Amount: {details['amount']}")
            print(f"Category: {details['category']}")
            print(f"Description: {details['description']}")
            print("")

def edit_expense():
    """Edits an existing expense in the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    expense_id = input("Enter the Expense ID to edit: ")

    if expense_id in expenses:
        print("Editing expense details. Leave blank to keep the current value.")
        trip_id = input(f"Enter new Trip ID (current: {expenses[expense_id]['trip_id']}): ") or expenses[expense_id]['trip_id']
        amount = input(f"Enter new amount (current: {expenses[expense_id]['amount']}): ") or expenses[expense_id]['amount']
        category = input(f"Enter new category (current: {expenses[expense_id]['category']}): ") or expenses[expense_id]['category']
        description = input(f"Enter new description (current: {expenses[expense_id]['description']}): ") or expenses[expense_id]['description']

        expenses[expense_id] = {
            "trip_id": trip_id,
            "amount": amount,
            "category": category,
            "description": description
        }

        save_data(file_path, expenses)
        print("Expense updated successfully!")
    else:
        print("Expense ID not found.")

def delete_expense():
    """Deletes an expense from the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    expense_id = input("Enter the Expense ID to delete: ")

    if expense_id in expenses:
        del expenses[expense_id]
        save_data(file_path, expenses)
        print("Expense deleted successfully!")
    else:
        print("Expense ID not found.")

# --- Packing List Management Functions ---
def manage_packing_menu():
    """Displays the menu for managing the packing list."""
    while True:
        print("\n--- Manage Packing List ---")
        print("1. Add an Item to Packing List")
        print("2. View Packing List")
        print("3. Update Packing Item Status")
        print("4. Delete a Packing Item")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            add_packing_item()
        elif choice == '2':
            view_packing_list()
        elif choice == '3':
            update_packing_status()
        elif choice == '4':
            delete_packing_item()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

def add_packing_item():
    """Adds a new item to the packing list."""
    file_path = "packing_list.json"
    packing_list = load_data(file_path)

    item_id = input("Enter item ID: ")
    trip_id = input("Enter the Trip ID: ")
    item_name = input("Enter the item name: ")
    status = input("Enter status (packed/not packed): ").lower()

    new_item = {
        "trip_id": trip_id,
        "item_name": item_name,
        "status": status
    }

    packing_list[item_id] = new_item
    save_data(file_path, packing_list)
    print("New item added to packing list successfully!")

def view_packing_list():
    """Displays all the items in the packing list."""
    file_path = "packing_list.json"
    packing_list = load_data(file_path)

    if not packing_list:
        print("No packing items found.")
    else:
        print("\n--- Packing List ---")
        for item_id, details in packing_list.items():
            print(f"Item ID: {item_id}")
            print(f"Trip ID: {details['trip_id']}")
            print(f"Item Name: {details['item_name']}")
            print(f"Status: {details['status']}")
            print("")

def update_packing_status():
    """Updates the status of a packing item."""
    file_path = "packing_list.json"
    packing_list = load_data(file_path)

    item_id = input("Enter the Item ID to update: ")

    if item_id in packing_list:
        status = input("Enter new status (packed/not packed): ").lower()
        packing_list[item_id]['status'] = status
        save_data(file_path, packing_list)
        print("Packing item status updated successfully!")
    else:
        print("Item ID not found.")

def delete_packing_item():
    """Deletes an item from the packing list."""
    file_path = "packing_list.json"
    packing_list = load_data(file_path)

    item_id = input("Enter the Item ID to delete: ")

    if item_id in packing_list:
        del packing_list[item_id]
        save_data(file_path, packing_list)
        print("Packing item deleted successfully!")
    else:
        print("Item ID not found.")

if __name__ == "__main__":
    main_menu()
