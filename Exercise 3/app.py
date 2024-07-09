from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

# List of random quotes
quotes = [
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
    "Get busy living or get busy dying.",
    "You have within you right now, everything you need to deal with whatever the world can throw at you."
]

@app.route('/')
def index():
    # Generate dynamic content
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return render_template('index.html', current_time=current_time, quote=random_quote)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
