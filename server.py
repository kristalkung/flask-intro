"""Greeting Flask app."""

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    return  "<!doctype html><html>Hi! This is the home page.  <a href=\"http://localhost:5000/hello\">click here</a> </html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
        <head>
        <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/process-hello">
                Would you like to have a compliment or an insult?
                <input type="radio" name="complimentorinsult" value="compliment">
                <label>Compliment</label>

                <input type="radio" name="complimentorinsult" value="insult">
                <label>Insult</label>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.route('/process-hello')
def process_hello():
    compliment_or_insult = request.args.get("complimentorinsult")

    if compliment_or_insult == "compliment":
        level = f"""
        <!doctype html>
        <html>
            <head>
            <title>Hi There!</title>
            </head>
            <body>
                <h1>Choose your compliment level</h1>
                <form action="/choose-compliment">
                    Choose your compliment level
                    <input type="radio" name="complimentlevel">
                    <label>Low</label>

                    <input type="radio" name="complimentlevel">
                    <label>Medium</label>

                    <input type="radio" name="complimentlevel">
                    <label>High</label>

                    <input type="submit">
                </form>
            </body>
        </html>
        """
    elif compliment_or_insult == "insult":
        level = f"""
        <!doctype html>
        <html>
            <head>
            <title>Hi There!</title>
            </head>
            <body>
                <h1>Choose your insult level</h1>
                <form action="/choose-insult">
                    Choose your insult level
                    <input type="radio" name="insultlevel" value="low">
                    <label>Low</label>

                    <input type="radio" name="insultlevel" value="medium">
                    <label>Medium</label>

                    <input type="radio" name="insultlevel" value="high">
                    <label>High</label>
                </form>
            </body>
        </html>
        """
    return level

@app.route('/choose-compliment')
def choose_compliment():
    level = request.args.get("level")

    if level == "low":
        options = AWESOMENESS[:3]
    elif level == "medium":
        options = AWESOMENESS[3:6]
    elif level == "high":
        options = AWESOMENESS[6:9]
    
    return f"""
    <!doctype html>
    <html>
        <head>
            <title>Choose Compliment</title>
        </head>
        <body>
            Fill out this form and choose your compliment!
            <form action="/greet">
                What's your name? <input type="text" name="person">
                Choose a compliment:
                <select name="compliment">
                    <option name="compliment">{options[0]}</option>
                    <option name="compliment">{options[1]}</option>
                    <option name="compliment">{options[2]}</option>
                </select>
                <input type="submit" value="Take me to my compliment!"
            </form>
        </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    
    return f"""
    <!doctype html>
    <html>
        <head>

        <title>A Compliment</title>
        </head>
        <body>
            Hi, {player}! I think you're {compliment}!
        </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Insult a player"""
    
    player = request.args.get("person")

    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
        <head>

        <title>A Diss</title>
        </head>
        <body>
            Hi, {player}! I think you're {insult}!
        </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")


# Select a compliment
#                 <select name="compliment">
#                     <option name="compliment">awesome</option>
#                     <option name="compliment">terrific</option>
#                     <option name="compliment">fantastic</option>
#                     <option name="compliment">neato</option>
#                     <option name="compliment">fantabulous</option>
#                     <option name="compliment">wowza</option>
#                     <option name="compliment">oh-so-not-meh</option>
#                     <option name="compliment">brilliant</option>
#                     <option name="compliment">ducky</option>
#                     <option name="compliment">coolio</option>
#                     <option name="compliment">incredible</option>
#                     <option name="compliment">wonderful</option>
#                     <option name="compliment">smashing</option>
#                     option name="compliment">lovely</option>
#                 </select>