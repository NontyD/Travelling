import json
import os
import re
from datetime import datetime
import pyfiglet
from rich.console import Console

# Create a single console instance for the entire module
console = Console()

def print_success(message):
    console.print(message, style="bold green")

def print_warning(message):
    console.print(message, style="bold yellow")

def print_error(message):
    console.print(message, style="bold red")

def display_heading():
    # Use the global console instance
    ascii_banner = pyfiglet.figlet_format("Travel Planner!", font="mini")
    console.print(f"\n✈ [bold blue]{ascii_banner}[/bold blue] ✈\n")

def main_menu():
    while True:
        display_heading()
        console.print("--- Main Menu ---", style="bold cyan")
        console.print("1. Manage Trips", style="cyan")
        console.print("2. Manage Itinerary", style="cyan")
        console.print("3. Track Expenses", style="cyan")
        console.print("4. Summary", style="cyan")
        console.print("5. Exit", style="cyan")
        choice = input("Choose an option: ")    

        if choice == '1':
            print_success("Navigating to Manage Trips Menu...")
            manage_trips_menu()
        elif choice == '2':
            print_success("Navigating to Manage Itinerary Menu...")
            manage_itinerary_menu()
        elif choice == '3':
            print_success("Navigating to Track Expenses Menu...")
            manage_expenses_menu()
        elif choice == '4':
            print_success("Navigating to Summary...")
        elif choice == '5':
            print_success("Exiting...")
            break
        else:
            print_error("Invalid option. Please choose again.")


# --- Trip Management Functions ---
def manage_trips_menu():
    """Displays the menu for managing trips."""
    while True:
        console.print("\n--- Manage Trips ---", style="bold cyan")
        console.print("1. Add a New Trip", style="cyan")
        console.print("2. View All Trips", style="cyan")
        console.print("3. Edit a Trip", style="cyan")
        console.print("4. Delete a Trip", style="cyan")
        console.print("5. Back to Main Menu", style="cyan")

        choice = input("Choose an option: ")

        if choice == '1':
            print_success("Adding a new trip...")
            create_trip()
        elif choice == '2':
            print_success("Viewing all trips...")
            view_trips()
        elif choice == '3':
            print_success("Editing a trip...")
            edit_trip()
        elif choice == '4':
            print_success("Deleting a trip...")
            delete_trip()
        elif choice == '5':
            print_success("Returning to Main Menu...")
            break
        else:
            print_error("Invalid option. Please choose again.")

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

    # Validate budget
    while True:
        budget = input("Enter budget amount: ").strip()
        try:
            budget = float(budget)
            if budget >= 0:
                break
            else:
                print("Budget must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the budget.")

    # Create new trip
    new_trip = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "budget": budget
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
            # Check if 'budget' exists; if not, show 'N/A'
            budget = details.get('budget', 'N/A')
            print(f"Budget: {budget}")
            print("")

def edit_trip():
    """Edits an existing trip in the trips.json file with input validation."""
    file_path = "trips.json"
    trips = load_data(file_path)

    if not trips:
        print("No trips found.")
        return

    trip_id = input("Enter the trip ID you want to edit: ").strip()
    if trip_id not in trips:
        print("Trip ID not found.")
        return

    # Display current trip details
    trip = trips[trip_id]
    print("\n--- Current Trip Details ---")
    print(f"Destination: {trip['destination']}")
    print(f"Start Date: {trip['start_date']}")
    print(f"End Date: {trip['end_date']}")
    print(f"Budget: {trip.get('budget', 'N/A')}")

    # Edit destination
    new_destination = input("Enter new destination (leave blank to keep current): ").strip()
    if new_destination:
        trip['destination'] = new_destination

    # Edit start date
    new_start_date = input("Enter new start date (YYYY-MM-DD) (leave blank to keep current): ").strip()
    if new_start_date and validate_date_format(new_start_date):
        trip['start_date'] = new_start_date

    # Edit end date
    new_end_date = input("Enter new end date (YYYY-MM-DD) (leave blank to keep current): ").strip()
    if new_end_date and validate_date_format(new_end_date) and validate_date_order(trip['start_date'], new_end_date):
        trip['end_date'] = new_end_date

    # Edit budget
    new_budget = input("Enter new budget (leave blank to keep current): ").strip()
    if new_budget:
        try:
            trip['budget'] = float(new_budget)
        except ValueError:
            print("Invalid budget. Please enter a valid number.")

    trips[trip_id] = trip
    save_data(file_path, trips)
    print("Trip updated successfully!")

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


    """Displays a summary of a specific trip including itinerary and costs."""
    
import pandas as pd

def show_summary():
    # Load the JSON data into DataFrames
    trips_df = pd.read_json('trips.json').T
    itinerary_df = pd.read_json('itinerary.json').T
    expenses_df = pd.read_json('expenses.json').T

    # Convert trip_id to string in all DataFrames to match the type
    trips_df.index = trips_df.index.astype(str)
    itinerary_df['trip_id'] = itinerary_df['trip_id'].astype(str)
    expenses_df['trip_id'] = expenses_df['trip_id'].astype(str)

    # Merge the DataFrames
    merged_df = pd.merge(trips_df, itinerary_df, left_index=True, right_on='trip_id', how='left')
    final_df = pd.merge(merged_df, expenses_df, on='trip_id', how='left')

    # Rename columns for clarity
    final_df.rename(columns={
        'trip_id': 'Trip ID',
        'destination': 'Destination',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'date': 'Activity Date',
        'activity': 'Activity',
        'amount': 'Expense Amount',
        'category': 'Expense Category',
        'description': 'Expense Description'
    }, inplace=True)

    # Convert 'Expense Amount' to numeric to enable calculations
    final_df['Expense Amount'] = pd.to_numeric(final_df['Expense Amount'], errors='coerce')

    # Display the summary in a vertical format
    print("\n--- Trip Summary ---")
    for trip_id, trip_data in trips_df.iterrows():
        print("\n------------------------------")
        print(f"Trip ID: {trip_id}")
        print(f"Destination: {trip_data['destination']}")
        print(f"Start Date: {trip_data['start_date']}")
        print(f"End Date: {trip_data['end_date']}")
        print(f"Budget: {trip_data['budget']}")

        # Filter expenses for the current trip
        trip_expenses = final_df[final_df['Trip ID'] == trip_id]

        # Calculate total expenses for the trip
        total_expenses = trip_expenses['Expense Amount'].sum()
        print(f"Total Expenses: {total_expenses}")

        # Compare total expenses with the budget
        if pd.notna(trip_data['budget']):
            remaining_budget = trip_data['budget'] - total_expenses
            print(f"Remaining Budget: {remaining_budget}")
        else:
            print("Budget: N/A")

        # Display each expense and activity
        for _, row in trip_expenses.iterrows():
            print("\nActivity Date: ", row['Activity Date'] if pd.notna(row['Activity Date']) else 'N/A')
            print("Activity: ", row['Activity'] if pd.notna(row['Activity']) else 'N/A')
            print("Expense Amount: ", row['Expense Amount'] if pd.notna(row['Expense Amount']) else 'N/A')
            print("Expense Category: ", row['Expense Category'] if pd.notna(row['Expense Category']) else 'N/A')
            print("Expense Description: ", row['Expense Description'] if pd.notna(row['Expense Description']) else 'N/A')

        print("------------------------------")

    print("\n")

if __name__ == "__main__":
    
    main_menu()
