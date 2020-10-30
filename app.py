
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route("/dessert/<users_dessert>")
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

@app.route("/madlibs/<adjective>/<noun>")
def madLibs(adjective, noun):
    return f"Mary bought a new {adjective} {noun}!"

@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        return f"{int(number1)} times {int(number2)} equals {int(number1)*int(number2)}"
    else:
        return "Invalid input(s), please try again."




if __name__ == '__main__':
    app.run(debug=True)