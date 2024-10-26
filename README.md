
# Simple Flask API for Learning HTTP Requests

This is a lightweight Flask API designed to demonstrate basic HTTP request handling for educational purposes. The API provides random responses for simple games and learning exercises, including **Wordle**, **Hangman**, random **color codes**, and **Pokémon** information.

## Features

- **Wordle** - Get a random 5-letter word.
- **Hangman** - Get a random word for Hangman.
- **Random Color** - Retrieve a random color name and its hex code.
- **Pokémon** - Fetch a random Pokémon name and image from the PokéAPI.

## Endpoints

### Base URL
- **URL:** `http://localhost:8000`

### `/` - Welcome Endpoint
- **Method:** `GET`
- **Description:** Returns a basic greeting message.
- **Response:** `"Hello, World!"`

### `/wordle` - Wordle Word
- **Method:** `GET`
- **Description:** Returns a random 5-letter word.
- **Response Example:**
  ```json
  {
    "word": "flame"
  }
  ```

### `/hangman` - Hangman Word
- **Method:** `GET`
- **Description:** Returns a random word for a Hangman game.
- **Response Example:**
  ```json
  {
    "word": "keyboard"
  }
  ```

### `/color` - Random Color
- **Method:** `GET`
- **Description:** Returns a random color and its hex code.
- **Response Example:**
  ```json
  {
    "color": "Blue",
    "hex": "#0000FF"
  }
  ```

### `/pokemon` - Pokémon Information
- **Method:** `GET`
- **Description:** Fetches a random Pokémon name and image using the PokéAPI GraphQL endpoint.
- **Response Example:**
  ```json
  {
    "name": "pikachu",
    "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
  }
  ```

## Running the API

### Prerequisites

- **Python 3.12+**
- **Flask**: Install via `pip install Flask`
- **Requests Library**: Install via `pip install requests`

### Start the API Server

1. Save the script in a file, e.g., `app.py`.
2. Run the server:
   ```bash
   python app.py
   ```
3. The server will start on `http://localhost:8000`.

## Example Usage

To test the endpoints, you can use [curl](https://curl.se/) in the terminal or [Postman](https://www.postman.com/) for API requests.

Example:
```bash
curl http://localhost:8000/wordle
```

## Contact

For questions or suggestions, please contact me at [elianrenteriadevelopment@gmail.com](mailto:elianrenteriadevelopment@gmail.com).
