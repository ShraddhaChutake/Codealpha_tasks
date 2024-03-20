### Application Code ###
source venv/bin/activate
pip install Flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to store expenses
expenses = []


@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)


@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    category = request.form['category']
    amount = float(request.form['amount'])

    expenses.append({
        'description': description,
        'category': category,
        'amount': amount
    })

    return redirect(url_for('index'))


@app.route('/summary')
def summary():
    # Implement logic to calculate summaries and insights
    total_expenses = sum(expense['amount'] for expense in expenses)
    categories = set(expense['category'] for expense in expenses)

    return render_template('summary.html', total_expenses=total_expenses, categories=categories)


if __name__ == '__main__':
    app.run(debug=True)



### Html code ###

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker</title>
</head>
<body>
    <h1>Expense Tracker</h1>
    <form action="/add_expense" method="post">
        <label for="description">Description:</label>
        <input type="text" name="description" required>
        <label for="category">Category:</label>
        <input type="text" name="category" required>
        <label for="amount">Amount:</label>
        <input type="number" name="amount" required>
        <button type="submit">Add Expense</button>
    </form>
    <h2>Expenses</h2>
    <ul>
        {% for expense in expenses %}
            <li>{{ expense.description }} - {{ expense.category }} - ${{ expense.amount }}</li>
        {% endfor %}
    </ul>
</body>
</html>

