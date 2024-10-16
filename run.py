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
        print_error("Invalid trip ID or trip ID already exists. Please try again.")

    # Validate destination
    destination = input("Enter destination: ").strip()
    while not destination:
        print_error("Destination cannot be empty.")
        destination = input("Enter destination: ").strip()

    # Validate start date
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        if validate_date_format(start_date):
            break
        print_error("Invalid date format. Please enter the date as YYYY-MM-DD.")

    # Validate end date
    while True:
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        if validate_date_format(end_date):
            if validate_date_order(start_date, end_date):
                break
            else:
                print_error("End date must be after the start date.")
        else:
            print_error("Invalid date format. Please enter the date as YYYY-MM-DD.")

    # Validate budget
    while True:
        budget = input("Enter budget amount: ").strip()
        try:
            budget = float(budget)
            if budget >= 0:
                break
            else:
                print_error("Budget must be a non-negative number.")
        except ValueError:
            print_error("Invalid input. Please enter a valid number for the budget.")

    # Create new trip
    new_trip = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "budget": budget
    }

    trips[trip_id] = new_trip
    save_data(file_path, trips)
    print_success("New trip added successfully!")

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
        print_warning("No trips found.")
    else:
        console.print("\n--- All Trips ---", style="bold cyan")
        for trip_id, details in trips.items():
            console.print(f"Trip ID: {trip_id}", style="cyan")
            console.print(f"Destination: {details['destination']}", style="cyan")
            console.print(f"Start Date: {details['start_date']}", style="cyan")
            console.print(f"End Date: {details['end_date']}", style="cyan")
            budget = details.get('budget', 'N/A')
            console.print(f"Budget: {budget}", style="cyan")
            console.print("")

def edit_trip():
    """Edits an existing trip in the trips.json file with input validation."""
    file_path = "trips.json"
    trips = load_data(file_path)

    if not trips:
        print_warning("No trips found.")
        return

    trip_id = input("Enter the trip ID you want to edit: ").strip()
    if trip_id not in trips:
        print_error("Trip ID not found.")
        return

    # Display current trip details
    trip = trips[trip_id]
    console.print("\n--- Current Trip Details ---", style="bold cyan")
    console.print(f"Destination: {trip['destination']}", style="cyan")
    console.print(f"Start Date: {trip['start_date']}", style="cyan")
    console.print(f"End Date: {trip['end_date']}", style="cyan")
    console.print(f"Budget: {trip.get('budget', 'N/A')}", style="cyan")

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
            print_error("Invalid budget. Please enter a valid number.")

    trips[trip_id] = trip
    save_data(file_path, trips)
    print_success("Trip updated successfully!")

def delete_trip():
    """Deletes a trip from the trips.json file."""
    file_path = "trips.json"
    trips = load_data(file_path)

    trip_id = input("Enter the Trip ID to delete: ")

    if trip_id in trips:
        del trips[trip_id]
        save_data(file_path, trips)
        print_success("Trip deleted successfully!")
    else:
        print_error("Trip ID not found.")

# --- Itinerary Management Functions ---
def manage_itinerary_menu():
    """Displays the menu for managing itineraries."""
    while True:
        print_success("\n--- Manage Itineraries ---")
        print("1. Add an Itinerary Entry")
        print("2. View All Itineraries")
        print("3. Edit an Itinerary Entry")
        print("4. Delete an Itinerary Entry")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_itinerary_entry()
        elif choice == '2':
            view_itineraries()
        elif choice == '3':
            edit_itinerary_entry()
        elif choice == '4':
            delete_itinerary_entry()
        elif choice == '5':
            break
        else:
            print_warning("Invalid option. Please choose again.")

def add_itinerary_entry():
    """Adds a new itinerary entry to the itinerary.json file with input validation."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    # Validate itinerary ID
    while True:
        itinerary_id = input("Enter itinerary ID: ").strip()
        if itinerary_id.isdigit() and int(itinerary_id) > 0 and itinerary_id not in itinerary:
            break
        print_error("Invalid itinerary ID or ID already exists. Please try again.")

    # Validate trip ID
    trips = load_data("trips.json")
    while True:
        trip_id = input("Enter the Trip ID to associate: ").strip()
        if trip_id in trips:
            break
        print_error("Trip ID not found. Please enter an existing Trip ID.")

    # Fetch trip start and end dates for date validation
    trip_start_date = datetime.strptime(trips[trip_id]['start_date'], "%Y-%m-%d")
    trip_end_date = datetime.strptime(trips[trip_id]['end_date'], "%Y-%m-%d")

    # Validate date
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if validate_date_format(date):
            itinerary_date = datetime.strptime(date, "%Y-%m-%d")
            if trip_start_date <= itinerary_date <= trip_end_date:
                break
            print_error(f"Date must be within the trip duration ({trip_start_date.date()} to {trip_end_date.date()}).")
        else:
            print_error("Invalid date format. Please enter the date as YYYY-MM-DD.")

    # Validate activity
    activity = input("Enter activity: ").strip()
    while not activity:
        print_error("Activity cannot be empty.")
        activity = input("Enter activity: ").strip()

    # Create new itinerary entry
    new_entry = {
        "trip_id": trip_id,
        "date": date,
        "activity": activity
    }

    itinerary[itinerary_id] = new_entry
    save_data(file_path, itinerary)
    print_success("New itinerary entry added successfully!")

def edit_itinerary_entry():
    """Edits an existing itinerary entry in the itinerary.json file."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    if not itinerary:
        print_warning("No itineraries found.")
        return

    itinerary_id = input("Enter the Itinerary ID to edit: ").strip()
    if itinerary_id in itinerary:
        print_success("Editing itinerary details. Leave blank to keep the current value.")
        entry = itinerary[itinerary_id]
        trip_id = entry['trip_id']

        # Fetch trip start and end dates for date validation
        trips = load_data("trips.json")
        trip_start_date = datetime.strptime(trips[trip_id]['start_date'], "%Y-%m-%d")
        trip_end_date = datetime.strptime(trips[trip_id]['end_date'], "%Y-%m-%d")

        date = input(f"Enter new date (YYYY-MM-DD) (current: {entry['date']}): ").strip()
        if date:
            if validate_date_format(date):
                itinerary_date = datetime.strptime(date, "%Y-%m-%d")
                if trip_start_date <= itinerary_date <= trip_end_date:
                    entry['date'] = date
                else:
                    print_error(f"Date must be within the trip duration ({trip_start_date.date()} to {trip_end_date.date()}).")
                    return
            else:
                print_error("Invalid date format. Please enter the date as YYYY-MM-DD.")
                return

        activity = input(f"Enter new activity (current: {entry['activity']}): ").strip() or entry['activity']

        entry.update({"trip_id": trip_id, "date": entry['date'], "activity": activity})
        save_data(file_path, itinerary)
        print_success("Itinerary entry updated successfully!")
    else:
        print_error("Itinerary ID not found.")

def validate_date_format(date_str):
    """Validates if the given date string matches the YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def view_itineraries():
    """Displays all the itineraries saved in the itinerary.json file."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    if not itinerary:
        print_warning("No itineraries found.")
    else:
        print_success("\n--- All Itineraries ---")
        for itinerary_id, details in itinerary.items():
            print(f"Itinerary ID: {itinerary_id}")
            print(f"Trip ID: {details['trip_id']}")
            print(f"Date: {details['date']}")
            print(f"Activity: {details['activity']}")
            print("")

def delete_itinerary_entry():
    """Deletes an itinerary entry from the itinerary.json file."""
    file_path = "itinerary.json"
    itinerary = load_data(file_path)

    if not itinerary:
        print_warning("No itineraries found.")
        return

    itinerary_id = input("Enter the Itinerary ID to delete: ").strip()

    if itinerary_id in itinerary:
        del itinerary[itinerary_id]
        save_data(file_path, itinerary)
        print_success("Itinerary entry deleted successfully!")
    else:
        print_error("Itinerary ID not found.")

# --- Expenses Management Functions ---

def manage_expenses_menu():
    """Displays the menu for managing expenses."""
    while True:
        console.print("\n--- Manage Expenses ---", style="bold green")
        console.print("1. Add an Expense", style="bold")
        console.print("2. View All Expenses", style="bold")
        console.print("3. Edit an Expense", style="bold")
        console.print("4. Delete an Expense", style="bold")
        console.print("5. Back to Main Menu", style="bold")

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
            console.print("[red]Invalid option. Please choose again.[/red]")

def add_expense():
    """Adds a new expense to the expenses.json file."""
    file_path = "expenses.json"
    trips_path = "trips.json"
    expenses = load_data(file_path)
    trips = load_data(trips_path)

    # Validate expense ID
    while True:
        try:
            expense_id = int(input("Enter expense ID (must be greater than 0): ").strip())
            if expense_id > 0 and str(expense_id) not in expenses:
                break
            console.print("[red]Invalid expense ID or ID already exists. Please try again.[/red]")
        except ValueError:
            console.print("[red]Invalid input. Please enter a numeric ID greater than 0.[/red]")

    # Validate trip ID
    while True:
        trip_id = input("Enter the Trip ID: ").strip()
        if trip_id in trips:
            break
        console.print("[red]Trip ID not found. Please enter a valid Trip ID that already exists.[/red]")

    # Validate amount
    while True:
        try:
            amount = float(input("Enter the amount: ").strip())
            if amount >= 0:
                break
            console.print("[red]Amount must be a non-negative number.[/red]")
        except ValueError:
            console.print("[red]Invalid input. Please enter a valid number for the amount.[/red]")

    # Validate category
    category = input("Enter the category (e.g., food, transport): ").strip()
    while not category:
        console.print("[red]Category cannot be empty.[/red]")
        category = input("Enter the category (e.g., food, transport): ").strip()

    # Validate description
    description = input("Enter a description: ").strip()
    while not description:
        console.print("[red]Description cannot be empty.[/red]")
        description = input("Enter a description: ").strip()

    new_expense = {
        "trip_id": trip_id,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses[str(expense_id)] = new_expense
    save_data(file_path, expenses)
    print_success("New expense added successfully!")

def view_expenses():
    """Displays all the expenses saved in the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    if not expenses:
        print_warning("No expenses found.")
    else:
        console.print("\n--- All Expenses ---", style="bold green")
        for expense_id, details in expenses.items():
            console.print(f"Expense ID: {expense_id}", style="bold")
            console.print(f"Trip ID: {details['trip_id']}")
            console.print(f"Amount: {details['amount']}")
            console.print(f"Category: {details['category']}")
            console.print(f"Description: {details['description']}\n")

def edit_expense():
    """Edits an existing expense in the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    expense_id = input("Enter the Expense ID to edit: ").strip()

    if expense_id in expenses:
        console.print("Editing expense details. Leave blank to keep the current value.", style="bold yellow")
        trip_id = input(f"Enter new Trip ID (current: {expenses[expense_id]['trip_id']}): ").strip() or expenses[expense_id]['trip_id']
        amount = input(f"Enter new amount (current: {expenses[expense_id]['amount']}): ").strip()
        if amount:
            try:
                amount = float(amount)
            except ValueError:
                print_error("Invalid input. Keeping the current amount.")
                amount = expenses[expense_id]['amount']
        else:
            amount = expenses[expense_id]['amount']

        category = input(f"Enter new category (current: {expenses[expense_id]['category']}): ").strip() or expenses[expense_id]['category']
        description = input(f"Enter new description (current: {expenses[expense_id]['description']}): ").strip() or expenses[expense_id]['description']

        expenses[expense_id] = {
            "trip_id": trip_id,
            "amount": amount,
            "category": category,
            "description": description
        }

        save_data(file_path, expenses)
        print_success("Expense updated successfully!")
    else:
        print_error("Expense ID not found.")

def delete_expense():
    """Deletes an expense from the expenses.json file."""
    file_path = "expenses.json"
    expenses = load_data(file_path)

    expense_id = input("Enter the Expense ID to delete: ").strip()

    if expense_id in expenses:
        del expenses[expense_id]
        save_data(file_path, expenses)
        print_success("Expense deleted successfully!")
    else:
        print_error("Expense ID not found.")


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
