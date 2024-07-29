from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/my_learning')
def my_learning():
    return render_template('my_learning.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/submit', methods=['POST'])
def submit_skill():
    skill_name = request.form['skillName']
    proficiency = request.form['Proficiency']
    hours_per_week = request.form['hoursaweek']
    learning_objective = request.form['Objectives']
    custom_objective = request.form.get('CustomObjective', '')  # Optional field

    # Process the data
    print(f"Skill: {skill_name}, Proficiency: {proficiency}, Hours: {hours_per_week}, Objective: {learning_objective}, Custom: {custom_objective}")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
