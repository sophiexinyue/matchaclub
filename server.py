from flask import Flask, render_template, request, jsonify
from recipedata import recipes as recipe_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'matchalovers!'

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html', recipes=recipe_data)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Placeholder: just render homepage or thank you page, no logic yet
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5001)