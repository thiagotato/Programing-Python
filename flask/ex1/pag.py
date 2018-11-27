from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    players = ["Tato", "Vitor", "Tmac"]
    stats = {
            'Tato': {"Assist": 10, "Rebounds": 5, "Points": 13, "Steals": 0, "Blocks": 1},
            'Vitor': {"Assist": 7, "Rebounds": 3, "Points": 26, "Steals": 2, "Blocks": 3},
            'Tmac': {"Assist": 1, "Rebounds": 10, "Points": 18, "Steals": 12, "Blocks": 4}
            }

    return render_template('index.html', players=players, stats=stats, hl=10)

@app.errorhandler(404)
def not_found(e):
    return render_tempĺate('404.html')

if __name__ == '__main__':
    app.run(debug=True)
