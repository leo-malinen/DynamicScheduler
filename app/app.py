from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Function to generate a calendar month
def generate_calendar(year, month):
    # Get the first day of the month and the number of days in the month
    first_day = datetime.date(year, month, 1)
    start_day = first_day.weekday()  # Monday is 0
    month_length = (first_day + datetime.timedelta(days=31)).replace(day=1) - datetime.timedelta(days=1)
    month_length = month_length.day
    days = [f"{year}-{month:02}-{day:02}" for day in range(1, month_length + 1)]
    return start_day, month_length, days

@app.route('/')
def calendar():
    # Current year and month
    today = datetime.date.today()
    year = today.year
    month = today.month

    start_day, month_length, days = generate_calendar(year, month)

    return render_template('calendar.html', year=year, month=month, start_day=start_day, month_length=month_length, days=days)

if __name__ == '__main__':
    app.run(debug=True)
