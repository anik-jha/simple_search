from flask import Flask, request, render_template
from service import search_giant_bomb

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/searchGames', methods=["GET", "POST"])
def searchGames():
    if request.method == "POST":
        # reading search parameters
        query = request.form.get("query").strip()
        api_key = request.form.get("apiKey").strip()

        # calling search service
        data = search_giant_bomb(api_key, query)
        return render_template('output.html', items=data["results"], no_of_results=data["number_of_total_results"])
    return render_template('home.html')
