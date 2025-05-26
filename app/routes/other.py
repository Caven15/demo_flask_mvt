from flask import render_template
from app import app

@app.route('/')
def index():
    test_python = "Ma valeur test"
    return render_template('index.html', test_html = test_python)

@app.route('/demo/jinja')
def demo_jinja():
    jeux_python = [
		{"titre": "The witcher 3", "genre": "Action/RPG", "note" : 18, "prix" :35.9999999, "jouable": True},
		{"titre": "Among us", "genre": "Plateforme", "note" : 15, "prix" : 8.9999999, "jouable": True},
		{"titre": "Dark Souls III", "genre": "Action", "note" : 17, "prix" : 25.855555, "jouable": False},
		{"titre": "GTA5", "genre": "Open world", "note" : 20, "prix" : 13.99, "jouable": False},
		{"titre": "GTA6", "genre": "Open world", "note" : 20, "prix" : 13.99, "jouable": False}
	]
    utilisateur_python = "alex"
    return render_template('demo-jinja.html', jeux= jeux_python, utilisateur=utilisateur_python)