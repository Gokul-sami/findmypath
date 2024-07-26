from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    skill_name = request.form.get('skillName')
    proficiency = request.form.get('Proficiency')
    hours_per_week = request.form.get('hoursaweek')
    objectives = request.form.get('Objectives')
    custom_objective = request.form.get('CustomObjective')

    # Process the data as needed
    # Example: Print the values (you can replace this with other logic)
    print(f"Skill: {skill_name}")
    print(f"Proficiency: {proficiency}")
    print(f"Hours per week: {hours_per_week}")
    print(f"Objectives: {objectives}")
    print(f"Custom Objective: {custom_objective if objectives == 'other' else 'N/A'}")

    # Return a response (render another template, send a message, etc.)
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
