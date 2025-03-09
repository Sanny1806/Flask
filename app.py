from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route 1: Simple hello world
@app.route('/')
def home():
    return 'Hello World'

# Route 2: Render an html page
@app.route('/page')
def page():
    return render_template('index.html')

# Route 3: Passing Data to HTML
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', user=name)

# Route 4: Handling a form
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

# Route 5: JSON API
@app.route('/api')
def api():
    data = {'name': 'Sania', 'age': 23, 'city': 'Pune'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)