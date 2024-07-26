from flask import Flask, render_template, request, redirect
import sqlite3
from sklearn.linear_model import LinearRegression # type: ignore
import numpy as np # type: ignore

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('user_data.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS skills 
             (id INTEGER PRIMARY KEY, skill TEXT, proficiency TEXT, hours INTEGER, objectives TEXT, custom_objective TEXT)''')
conn.commit()

@app.route('/')
def home():
    c.execute("SELECT * FROM skills")
    skills = c.fetchall()
    return render_template('my_learning.html', skills=skills)

@app.route('/submit', methods=['POST'])
def submit():
    skill_name = request.form.get('skillName')
    proficiency = request.form.get('Proficiency')
    hours_per_week = request.form.get('hoursaweek')
    objectives = request.form.get('Objectives')
    custom_objective = request.form.get('CustomObjective')

    # Save data to the database
    c.execute("INSERT INTO skills (skill, proficiency, hours, objectives, custom_objective) VALUES (?, ?, ?, ?, ?)",
              (skill_name, proficiency, hours_per_week, objectives, custom_objective))
    conn.commit()

    # Simple machine learning example (adjust with actual logic)
    X = np.array([hours_per_week]).reshape(-1, 1)
    y = np.array([10, 20, 30])  # Example target values, replace with actual logic
    model = LinearRegression().fit(X, y)
    suggested_plan = model.predict(X)[0]

    # Example response
    return f"Form submitted successfully! Suggested plan: {suggested_plan}"

if __name__ == '__main__':
    app.run(debug=True)
