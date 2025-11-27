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

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    data = httpx.get(url)

    if data.status_code == 200:
        data = data.json()
        types = []
       
        name = data['name']
        
        for type_info in data["types"]:
            type_name = type_info["type"]["name"]
            types.append(type_name)

        stats = {}

        for stat_info in data["stats"]:
            stats_name = stat_info['stat']["name"]
            base_stat = stat_info["base_stat"]
            stats[stats_name] = base_stat

        image_url = data["sprites"]["front_default"]

        if display_raw == True:
            print(json.dumps(data, indent=4))
        else:
            print(f"Name: {name}")
            print(f"Types: {', '.join(types)}")
            print("Base Stats:")
            for stat, value in stats.items():
                print(f"  {stat.capitalize()}: {value}")
            print(f"Image URL: {image_url}")
    else:
        print(f"Error: Pokémon '{name}' not found!")


# Example usage
fetch_pokemon_custom("squirtle")  # Display summary by default
#fetch_pokemon_custom("squirtle", display_raw=True)  # Display raw JSON

"""
Hints:
- Use json.dumps(data, indent=4) for raw JSON output.
- Extract specific keys like 'types', 'stats', and 'sprites' for summaries.
- Use if display_raw to toggle between outputs.
"""
