import requests
from flask import Flask, jsonify
from random import randint, choice

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

wordle_words = [
    "apple", "brave", "crisp", "dance", "eager", "flame", "grape", "happy", "irony", 
    "jolly", "knock", "lemon", "mango", "noble", "ocean", "plant", "query", "royal", 
    "smart", "track", "unity", "vivid", "waste", "xenon", "yield", "zebra"
]

@app.route("/wordle", methods=["GET"])
def get_wordle_word():
    word = choice(wordle_words)
    return jsonify({"word": word})

hangman_words = [
    "python", "flask", "coding", "computer", "algorithm", "function", "variable",
    "developer", "keyboard", "monitor", "internet", "network", "server", "database",
    "library", "framework", "syntax", "loop", "condition", "hardware"
]

@app.route("/hangman", methods=["GET"])
def get_hangman_word():
    word = choice(hangman_words)
    return jsonify({"word": word})

colors = [
    {"color": "Red", "hex": "#FF0000"},
    {"color": "Green", "hex": "#00FF00"},
    {"color": "Blue", "hex": "#0000FF"},
    {"color": "Yellow", "hex": "#FFFF00"},
    {"color": "Purple", "hex": "#800080"},
    {"color": "Cyan", "hex": "#00FFFF"},
    {"color": "Magenta", "hex": "#FF00FF"},
    {"color": "Orange", "hex": "#FFA500"},
    {"color": "Pink", "hex": "#FFC0CB"},
    {"color": "Brown", "hex": "#A52A2A"},
]

@app.route("/color", methods=["GET"])
def get_random_color():
    random_color = choice(colors)
    return jsonify(random_color)

@app.route('/pokemon', methods=["GET"])
def get_pokemon():
    variables = {
      "id": randint(1, 1025)
    }
    URL = "https://beta.pokeapi.co/graphql/v1beta"
    query = """
    query samplePokeAPIquery($id: Int!) {
      pokemon_v2_pokemon(where: {id: {_eq: $id}}) {
        name
        pokemon_v2_pokemonsprites {
          sprites(path: "front_default")
        }
      }
    }
    """
    response = requests.post(URL, json={"query": query, "variables": variables}).json()
    payload = {
      "name": response["data"]["pokemon_v2_pokemon"][0]["name"],
      "image": response["data"]["pokemon_v2_pokemon"][0]["pokemon_v2_pokemonsprites"][0]["sprites"]
    }
    return payload


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
