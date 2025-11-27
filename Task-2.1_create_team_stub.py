
"""
Exercise 2.1: Create a Team Class and Add Pokémon (Stub)
- Create a Team class.
- Implement the add_pokemon method to add a Pokémon to the team.
- Ensure no duplicates and enforce a maximum team size of 6 Pokémon.
"""

import httpx


class Team:
    def __init__(self):
        """Initialize an empty team."""
        # TODO: Initialize an empty list to store team members
        self.members = []
    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # TODO: Check if the team already has 6 Pokémon
        if len(self.members) == 6:
            # TODO: If yes, print a message indicating the team is full
            print("Team is full")
            return
        # TODO: Check if the Pokémon is already in the team (case-insensitive)
            # TODO: If yes, print a message indicating duplication
        for i in self.members:
            if i["name"].lower() == name.lower():
                print("Pokemon is in team already")
                return
            
        # TODO: Fetch Pokémon data from the PokéAPI (hint: httpx.get + status code check)
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

        data = httpx.get(url)

        # TODO: If successful, extract the fields you want to store (name, types, sprite URL)
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

            pokemon = {
                "name": name,
                "types": types,
                "stats": stats,
                "image": image_url

            }

            # TODO: Append the dictionary/object to self.members
            self.members.append(pokemon)
            # TODO: Print a confirmation message
            print(f"{name} added to team")
        else:
            # TODO: Print an error message if the Pokémon is not found
            print(f"Error: Pokémon '{name}' not found!")

# Example usage
team = Team()
team.add_pokemon("squirtle")
team.add_pokemon("charmander")
