from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJ = [{
    'id': 1,
    'title': 'Thryft',
    'techStack': 'React',
    'link': "https://github.com/tanmaynema1/Thryft"
}, {
    'id': 2,
    'title': 'Meditate App',
    'techStack': 'Swift',
    'link': 'https://github.com/tanmaynema1/meditateApp'
}, {
    'id': 3,
    'title': 'Laptop Price Prediction',
    'techStack': 'Python',
    'link': 'https://github.com/tanmaynema1/Laptop-Price-Prediction-System'
}, {
    'id': 4,
    'title': 'Weather App',
    'techStack': 'Swift',
    'link': 'https://github.com/tanmaynema1/'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', proj=PROJ)


@app.route("/api/proj")
def list_proj():
    return jsonify(PROJ)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
