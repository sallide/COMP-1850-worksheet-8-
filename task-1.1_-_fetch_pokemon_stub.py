"""
Exercise 1.1: Fetch and Display a Pokémon (Stub)
- Fetch Pokémon data from the PokéAPI.
- Pretty-print the raw JSON response.
"""

import httpx
import json


def fetch_pokemon(name):
    """Fetch Pokémon data from the PokéAPI and display raw JSON."""
    # TODO: Construct the URL using the Pokémon name (hint: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")

    # TODO: Make a GET request to the URL with httpx

    # TODO: Check if the response is successful (status_code == 200)
        # TODO: Parse the JSON response and pretty-print it with json.dumps(..., indent=4)
    # else:
        # TODO: Print an error message if the Pokémon is not found

# Example usage
# fetch_pokemon("squirtle")

"""
Hints:
- Use httpx.get(url) to fetch the data.
- Use response.json() to parse the JSON.
- Use json.dumps(data, indent=4) to pretty-print the JSON.
"""
