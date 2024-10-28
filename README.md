# Travel Planner
![Travel Planner](/assets/images/landing.png)

As a person who loves traveling, managing trips, itineraries, and expenses can become overwhelming. This app was created to simplify that process, providing a streamlined way to plan, organize, and track all travel details. Whether it's managing multiple trips, keeping track of activities, or monitoring travel expenses, this application offers an all-in-one solution for travel enthusiasts and planners alike. By keeping everything in one place, users can focus more on enjoying their travels and less on the logistical details.

The deployed project live link is [HERE](https://travellingplanner-f3f27e55bd6d.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Contents

- [Introduction](#introduction)
- [Project](#project)
    - [User stories:](#user-stories)
- [Pre development](#pre-development)
    - [Flow chart](#flow-chart)
- [Development](#development)
    - [User Guide](#user-guide)
- [Features](#features)
  - 
- [Technologies Used](#technologies-used)
- [Resources](#resources)
  - [Libraries](#libraries)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction

This app is designed to help users manage their travel plans effortlessly. It allows users to create and organize trips, track itineraries, and log expenses all in one place. Users can add details like trip destinations, dates, budgets, activities, and categories for expenses, making it easy to plan and monitor every aspect of their journey. With intuitive features for adding, editing, and reviewing travel details, the app ensures that users can keep their trips organized and stay within budget, all while having quick access to important travel information.

## Project 

The aim of the project is to create a comprehensive and user-friendly travel management application that simplifies trip planning and organization. By integrating features for managing itineraries, tracking expenses, and storing key trip details, the project seeks to provide travelers with a centralized tool to efficiently plan, manage, and review their journeys. The ultimate goal is to enhance the travel experience by offering an organized, accessible, and easy-to-use platform for both casual travelers and travel enthusiasts alike.


### User stories:

1. As a User, **I want to create a new trip**

Description:
As a user, I want to be able to create a new trip by providing the trip's destination, start date, end date, and budget, so I can keep track of my upcoming travel plans.

Acceptance Criteria:
A new trip ID is generated.
The user is prompted to enter the destination, start date, end date, and budget.
The trip is saved in the trips.json file.

2. As a User, **I want to edit an existing trip**

Description:
As a user, I want to be able to edit the details of an existing trip, such as the destination, start and end dates, and budget, so I can update my travel plans if anything changes.

Acceptance Criteria:
The user can choose an existing trip by its ID.
The user can edit one or more fields and leave others unchanged.
The updates are saved in the trips.json file.

3. As a User, **I want to view a summary of my trips**

Description:
As a user, I want to view a detailed summary of all my trips, including itinerary and expenses, so I can get an overview of my travel plans and spending.

Acceptance Criteria:
A summary of all trips is displayed.
For each trip, details of the itinerary and total expenses are included.
The summary shows if the trip is under or over budget.

4. As a User, **I want to create a new itinerary entry for a trip**

Description:
As a user, I want to be able to add activities to the itinerary for a specific trip, so I can plan my schedule for each day of the trip.

Acceptance Criteria:
The user can select an existing trip by its ID.
The user can add activities with a date.
The itinerary entry is saved in the itinerary.json file.

5. As a User, **I want to edit an itinerary entry**

Description:
As a user, I want to edit the details of an itinerary entry, such as the activity or the date, so I can adjust my schedule as needed.

Acceptance Criteria:
The user can select an itinerary entry by its ID.
The user can edit the date or activity for the selected entry.
The changes are saved in the itinerary.json file.

6. As a User, **I want to add an expense to a trip**

Description:
As a user, I want to be able to record expenses for a trip, such as transportation, accommodation, or food, so I can track my spending during the trip.

Acceptance Criteria:
The user can select a trip by its ID.
The user can add an expense with the amount, category, and description.
The expense is saved in the expenses.json file.

7. As a User, **I want to edit an expense for a trip**

Description:
As a user, I want to be able to edit the details of a recorded expense, such as the amount, category, or description, so I can correct any mistakes or update my records.

Acceptance Criteria:
The user can select an expense by its ID.
The user can modify the amount, category, or description.
The updates are saved in the expenses.json file.

8. As a User, **I want input validation to prevent errors**

Description:
As a user, I want the system to validate my input (e.g., dates, budget, expense amount) to ensure that the data I enter is valid and accurate.

Acceptance Criteria:
Input for fields like dates and budget must be validated.
The system provides error messages if the input is invalid (e.g., incorrect date format, negative budget).
The user is prompted to correct invalid input before proceeding.

### Site owner goals

* **Enhance User Experience:**
Create a user-friendly interface that simplifies the process of managing travel plans, making it easy for users to navigate the app and access its features.

* **Promote Travel Planning:**
Encourage users to plan and organize their trips efficiently, helping them to maximize their travel experiences and minimize stress.

* **Encourage Financial Management:**
Provide tools for users to track their travel budgets and expenses, fostering responsible financial habits and enabling them to stay within their financial limits.

* **Support User Engagement:**
Foster a community of travel enthusiasts by encouraging feedback, suggestions, and sharing experiences, which can help improve the app and build a loyal user base.

* **Continuous Improvement:**
Regularly update and enhance the app's features based on user feedback and evolving travel trends, ensuring that the application remains relevant and valuable to users.

* **Secure Data Management:**
Ensure that all user data, including trip details and expenses, is stored securely, maintaining user privacy and building trust in the application.

* **Facilitate Travel Inspiration:**
Incorporate features that inspire users to explore new destinations and activities, making the app not just a planning tool but also a source of travel ideas.

* **Monitor App Performance:**
Track usage statistics and user engagement metrics to identify areas for improvement and optimize the overall performance of the application.

* **Expand User Base:**
Develop marketing strategies to attract new users and grow the application's audience, making it a go-to platform for travel management.

### Pre development

#### Flow charts

#### Main menu

![Main menu](/assets/images/main-menu-flowchart.png)

#### Trip management

![Trip management](/assets/images/trip-management.png)

#### Itinerary management

![Itinerary management](/assets/images/itinerary-management.png)

#### Expense management

![Expense management](/assets/images/expense-management.png)

### Development


## User Guide

1. **Starting the App**

![Main menu](/assets/images/main-menu.png)

* The app automatically opens with main menu after the instructions.
* Select the option you need from the main menu.
* You can click RUN PROGRAM anytime you want to reset back to main menu.

2. **Trip Management**

![Trip management](/assets/images/manage-trips.png)

* ***Create a New Trip:***
* Select the "Create Trip" option from the main menu.
* Enter the Trip ID (a positive number that hasn't been used before).
* Enter the destination for your trip (e.g., Paris, Tokyo).
* Provide the start date in the format YYYY-MM-DD. Ensure it's today or a future date.
* Enter the end date in the same format. Make sure it’s on or after the start date.
* Enter a budget (a positive number) for your trip.
* If all information is valid, the new trip will be saved successfully.
* ***Edit a Trip:***
* Choose the "Edit Trip" option from the main menu.
* Enter the Trip ID of the trip you want to edit.
* Update any of the following details: destination, start date, end date, or budget.
* Leave any field blank to keep the current value.
* The trip details will be updated if all information is valid.
* Delete a Trip:
* Select the "Delete Trip" option from the main menu.
* Enter the Trip ID of the trip you want to remove.
* Confirm deletion when prompted. The trip will be permanently deleted from the records.

3. **Itinerary Planning**

![Itinerary management](/assets/images/manage-itinerary.png)

* ***Add an Itinerary Entry:***
* Choose "Add Itinerary Entry" from the main menu.
* Enter the Trip ID for which the activity is planned.
* Provide the date of the activity (in the format YYYY-MM-DD). Ensure it falls within the trip duration.
* Enter a brief description of the activity (e.g., museum visit, hiking).
* The entry will be added to the itinerary for the selected trip.
* ***Edit an Itinerary Entry:***
* Select "Edit Itinerary Entry" from the main menu.
* Enter the Itinerary ID of the entry you wish to update.
* Update the date and activity as needed, or leave blank to keep the existing values.
* The entry will be updated with the new information.
* ***Delete an Itinerary Entry:***
* Choose "Delete Itinerary Entry" from the main menu.
* Enter the Itinerary ID of the entry you wish to delete.
* Confirm deletion when prompted. The entry will be permanently removed.

4. **Expense Tracking**

![Expense management](/assets/images/track-expenses.png)

* ***Add an Expense:***
* Select the "Add Expense" option from the main menu.
* Enter the Trip ID associated with the expense.
* Provide the expense ID (a positive number that hasn’t been used before for this trip).
* Enter the amount spent (a non-negative number).
* Choose a category for the expense (e.g., food, transport, accommodation).
* Add a brief description (e.g., lunch at a restaurant).
* The expense will be saved successfully if all information is valid.
* ***Edit an Expense:***
* Choose the "Edit Expense" option from the main menu.
* Enter the Expense ID of the expense you wish to modify.
* Update the Trip ID, amount, category, or description as needed. Leave any field blank to keep the   
    current value.
* The expense will be updated with the new details.
* ***Delete an Expense:***
* Select "Delete Expense" from the main menu.
* Enter the Expense ID of the expense you want to remove.
* Confirm deletion when prompted. The expense will be permanently removed.

5. **View the Summary Dashboard**

![Summary](/assets/images/summary.png)

* Choose "View Summary" from the main menu to see a comprehensive overview of all your trips.
* ***The dashboard displays:***
* Total Expenses: The total amount spent on each trip.
* Budget Remaining: The remaining budget after accounting for expenses.
* Itinerary Details: A list of planned activities for each trip.
* This section provides insights into spending patterns and trip organization.

6. **Data Validation and Error Handling**

![Trip management](/assets/images/add-trip-errors.png)

* The app validates all inputs (e.g., dates must be in the YYYY-MM-DD format, budget must be a positive number).
* If an invalid input is detected, an error message will appear with guidance on how to correct the entry.
* Follow the prompts to ensure all inputs are correct before proceeding.

7. **Access Data Across Sessions**
* All trips, itineraries, and expenses are saved to JSON files, allowing you to pick up where you left off the next time you use the app.
* Ensure the JSON files are stored in the correct directory to maintain data consistency across sessions.


## Features

1. Trip Management:
* Create Trips:
Users can initiate new trips by specifying essential details, including:
* * Destination: The location of the trip.
* * Start Date and End Date: The timeframe for the trip, ensuring proper planning.
* * Budget: An estimated amount allocated for the trip, helping users stay financially organized.
* Edit Trips:
Users can modify existing trip details to reflect any changes in plans, allowing for adjustments to:
Update the destination, start and end dates, or budget.
* Delete Trips:
If plans change or a trip is no longer necessary, users can remove trips from their records.
* Organize Trip Details:
All trip information is stored and organized for easy access, enabling users to view their upcoming and past trips at a glance.

2. Itinerary Planning:
* Add Itinerary Entries:
Users can create detailed itinerary entries for each trip, specifying:
* * Activities: Various events or activities planned for specific days.
* * Dates: The date for each activity, ensuring an organized daily schedule.
* Edit Itinerary Entries:
Users can modify existing itinerary entries, allowing them to:
Update the activity name or date if plans change.
* Delete Itinerary Entries:
Users can remove entries if activities are canceled or rescheduled, ensuring their itineraries remain accurate.
* Organized Planning:
The itinerary feature helps users visualize their trip day by day, ensuring they make the most of their travel experience.

3. Expense Tracking:
* Record Expenses:
Users can log all expenses incurred during a trip, capturing:
* * Amount Spent: The total amount of each expense.
* * Category: Classifying expenses into types such as food, transport, accommodation, etc.
* * Description: Providing additional context or details about each expense.
* Edit Expenses:
Users can update expense entries to correct any inaccuracies or changes in spending.
* Delete Expenses:
Users can remove expense entries that are no longer relevant or were mistakenly logged.
* Categorization:
Organizing expenses into categories allows users to track their spending habits effectively and understand where their money is going.

4. Summary Dashboard:
* Detailed Summary:
Users can view a comprehensive overview of all trips, including:
* * Total Expenses: The sum of all expenses recorded for each trip.
* * Budget Remaining: A calculation that shows how much budget is left after expenses.
* * Itinerary Details: A quick glance at the planned activities for each trip.
* Insights:
The dashboard provides insights into spending habits, helping users manage their finances better and plan future trips accordingly.

5. Input Validation:
* Data Validation:
User inputs are checked for correct formatting to prevent errors, ensuring:
* * Dates are in the correct format (YYYY-MM-DD).
* * Budgets and expenses are positive numbers.
* Error Handling:
Clear and informative error messages guide users when they enter invalid data, helping them correct mistakes easily.

6. User-Friendly Interface:
* Intuitive Navigation:
The application features a simple and intuitive interface, allowing users to navigate through trip management functions effortlessly.
* Responsive Design:
The app is designed to be accessible on various devices, including smartphones, tablets, and desktops, providing a seamless experience regardless of screen size.

7. Data Persistence:
* JSON Data Storage:
User data, including trips, itineraries, and expenses, is stored in JSON files, enabling easy retrieval and updates.
* Session Accessibility:
Users can access their data across multiple sessions, ensuring their information is saved and available whenever they return to the app.


## Technologies Used

The main technology used to create this program is Python


### Resources

- Gitpod 
- GitHub 
- Heroku
- Draw.io to create flowchart

### Libraries

[json](https://docs.python.org/3/library/json.html) - for parsing and generating JSON data.
[os](https://docs.python.org/3/library/os.html) - for file handling and path manipulation.
[re](https://docs.python.org/3/library/re.html) - for pattern matching using regular expressions.
[pandas](https://pypi.org/project/pandas/) - for data analysis and manipulation.
[datetime](https://docs.python.org/3/library/datetime.html) - for working with dates and times.
[pyfiglet](https://pypi.org/project/pyfiglet/) - for generating ASCII art from text.
[rich](https://pypi.org/project/rich/) - for colorful and formatted console output.



## Future Updates

#### Budget Analysis and Alerts:

* Add detailed budget tracking with visual insights, like pie charts showing spending per category.
* Introduce alerts for categories where spending exceeds a user-defined threshold.

#### Expense Report Generation:

* Create downloadable reports in PDF or Excel formats with expense summaries, categorized breakdowns, and budget vs. actual comparisons.
* Include the option to email the report or share it with other team members.

#### Currency Conversion:

* Automatically convert expenses to a preferred currency based on trip location or user selection.
* Integrate a currency conversion API to ensure exchange rates stay current.

## Validation

Code Institute Python Linter - https://pep8ci.herokuapp.com/# was used.
All code validated and where lines were showing as too long they were adjusted. Some line adjustments caused bugs in the code but those bugs were fixed and some codes were rewritten.

## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for this project, the name is travellingplanner) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Find the repository you want to fork by either searching for it using the search bar or by directly navigating to its URL.
3. Once you're on the repository's main page, locate the "Fork" button in the upper-right corner of the page, usually next to the "Star" button.
4. Click on the "Fork" button.

#### How to Clone

To clone the repository:

* Click on the "Code" button in your forked repository.
* Copy the repository URL (HTTPS, SSH, or GitHub CLI).
* Open a terminal (or command prompt) on your computer.
* Run the following command: git clone <github.com/nontyd/soduku>

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing carried out.
   
The deployed project live link is [HERE](https://travellingplanner-f3f27e55bd6d.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Bugs

Throughout the development process, various bugs were identified and resolved iteratively. A notable challenge was ensuring that the code conformed to a strict 79-character line limit, which occasionally introduced unintended errors, such as syntax issues and incorrect line breaks that affected the functionality.

These bugs were carefully managed and fixed as they arose, with particular attention given to maintaining readability and functionality within the character constraints. This iterative debugging process helped enhance both the code’s structure and its adherence to best practices, ensuring a clean and functional final product.

## Credits

[Real Python: Working with data](https://realpython.com/python-json/) - For handling json data, such as loading and saving expense and trip information in .json files.

[W3Schools: Python String strip() Method](https://www.w3schools.com/python/ref_string_rstrip.asp) - To use .strip() to remove unwanted whitespace from user input, ensuring clean data for IDs, categories, and descriptions.

[GeeksforGeeks: Python Try, Except, and Finally](https://www.geeksforgeeks.org/try-except-else-and-finally-in-python/) - For catching errors (like ValueError when converting input to numbers) and displaying user-friendly error messages.

[DataCamp: Introduction to pandas](https://www.datacamp.com/tutorial/pandas) - For managing, analyzing, and visualizing data with pandas to track expenses effectively.

## Acknowledgements

Tutor support
Friends and family
My mentor