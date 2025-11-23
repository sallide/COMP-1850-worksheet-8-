"""
Exercise 1.3: Custom Output (Raw vs Summary) (Stub)
- Fetch Pokémon data from the PokéAPI.
- Display either the full raw JSON or a summarised version based on a parameter.
"""

import httpx
import json

def fetch_pokemon_custom(name, display_raw=False):
    """Fetch Pokémon details and display either raw JSON or a summary."""
    # TODO: Construct the URL using the Pokémon name
    
    # TODO: Make a GET request to the URL
    
    # TODO: Check if the response is successful (status_code == 200)
    pass
        # TODO: Parse the JSON response
        
    
        #if display_raw:
            # TODO: Pretty-print the raw JSON
        #else:
            # TODO: Extract the Pokémon's name, types, base stats, and image URL
            
            # TODO: Print the details in a readable format
    
    # TODO: Print an error message if the Pokémon is not found


# Example usage
# fetch_pokemon_custom("squirtle")  # Display summary by default
# fetch_pokemon_custom("squirtle", display_raw=True)  # Display raw JSON

"""
Hints:
- Use json.dumps(data, indent=4) for raw JSON output.
- Extract specific keys like 'types', 'stats', and 'sprites' for summaries.
- Use if display_raw to toggle between outputs.
"""
