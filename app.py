from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        description TEXT NOT NULL,
                        category TEXT NOT NULL,
                        amount REAL NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        description = request.form['description']
        category = request.form['category']
        amount = float(request.form['amount'])
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (date, description, category, amount) VALUES (?, ?, ?, ?)",
                       (date, description, category, amount))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/totals')
def totals():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Fetch all unique months and categories
    cursor.execute("SELECT DISTINCT strftime('%Y-%m', date) AS month FROM expenses ORDER BY month")
    months = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT DISTINCT category FROM expenses ORDER BY category")
    categories = [row[0] for row in cursor.fetchall()]
    
    # Create a dictionary to store totals
    totals_data = {month: {category: 0 for category in categories} for month in months}
    totals_per_month = {month: 0 for month in months}
    total_food = 0  # To track total expenses for the "Food" category across all months

    # Fetch the sum of expenses grouped by month and category
    cursor.execute("""
        SELECT strftime('%Y-%m', date) AS month, category, SUM(amount) 
        FROM expenses 
        GROUP BY month, category
    """)
    
    for month, category, total in cursor.fetchall():
        totals_data[month][category] = total
        totals_per_month[month] += total
        if category == 'Food':
            total_food += total

    conn.close()
    return render_template('totals.html', months=months, categories=categories, totals_data=totals_data, totals_per_month=totals_per_month, total_food=total_food)

# Initialize database before running the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
