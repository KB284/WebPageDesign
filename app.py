from flask import Flask
from flask import render_template
import graphyte

app = Flask(__name__)
app.config['STATSD_HOST'] = '127.0.0.1'
app.config['STATSD_PORT'] = 5000

graphyte.init('127.0.0.1', prefix='myapp.')

#define available products
products = [
    {
        'name': 'Product A',
        'description': 'Basic Meme.',
        'price': 19.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'name': 'Product B',
        'description': 'Pro Meme.',
        'price': 29.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'name': 'Product C',
        'description': 'Premium Meme.',
        'price': 39.99,
        'image': 'https://via.placeholder.com/150'
    }
]

#create general webpages for website
@app.route('/')
def home():
    graphyte.send('page.views', 1)
    return render_template('home.html', active='home')

@app.route('/demo')
def demo():
    return render_template('demo.html', active='demo')

@app.route('/resources')
def resources():
    return render_template('resources.html', active='resources')

@app.route('/store')
def store():
    return render_template('store.html', active='store', products=products)


#run the website
if __name__ == '__main__':
    app.run(debug=True)