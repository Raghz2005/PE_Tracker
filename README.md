# Personal Expenses Tracker

## Overview
The **Personal Expenses Tracker** is a Python-based web application built using the Flask framework. It helps users manage and track their personal expenses efficiently. The application stores expense data in an SQLite database and provides a simple and intuitive interface for managing financial records.

## Features
- Add, edit, and delete expense records.
- View all expenses in a table format.
- Organize and categorize expenses.
- Lightweight and easy to deploy.

## Project Structure
personal_expenses_tracker/ 
├── app.py 
### Main application script 
├── expenses.db 
### SQLite database file 
├── static/ 
### Folder for static files (CSS, JavaScript, images) 
├── templates/ 
### HTML templates for the app's frontend 
├── requirements.txt 
### List of project dependencies 
├── .gitignore 
### Git configuration to exclude unnecessary files 
└── README.md 


## Prerequisites
To run this application, you need:
- Python 3.7 or higher installed on your system.
- A virtual environment (optional but recommended).

## Installation and Setup

1. **Clone the repository**:
   git clone https://github.com/your-username/personal-expenses-tracker.git
   cd personal-expenses-tracker


2. **Create and activate a virtual environment**:
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows

3. **Install dependencies: Install the required Python libraries from requirements.txt**:
    pip install -r requirements.txt

4. **Run the application: Start the Flask application**:
    python app.py
    Access the app: Open your browser and go to http://127.0.0.1:5000.

**Usage**
Use the Add Expense form to input your expense details (e.g., amount, category, and description).
View your expense records in the Expense Table.
Edit or delete entries as needed.

**Outputs**
All expense records are saved in the expenses.db SQLite database.
If required, you can export the database or add custom scripts to generate reports.

**File Descriptions**
app.py: The main Flask application that runs the backend logic and serves the frontend.
expenses.db: The SQLite database file where all expense data is stored.
static/: Contains CSS, JavaScript, and other static assets.
templates/: Holds HTML templates for rendering the user interface.

**Example Output**
Below is a sample of how the application interface looks:

Date	    Category	    Description	        Amount
2024-12-01	Food	        Lunch at cafe	    $12.50
2024-12-02	Transport	    Taxi to airport	    $35.00

**Additional Notes**
    Modify app.py to customize routes or add new features.
    Backup the expenses.db file regularly to prevent data loss.

**Contributing**
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
