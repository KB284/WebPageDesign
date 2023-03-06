from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', active='home')

@app.route('/about')
def about():
    return render_template('about.html', active='about')

@app.route('/contact')
def contact():
    return render_template('contact.html', active='contact')

@app.route('/demo')
def demo():
    return render_template('demo.html', active='demo')

@app.route('/resources')
def resources():
    return render_template('resources.html', active='resources')

if __name__ == '__main__':
    app.run()