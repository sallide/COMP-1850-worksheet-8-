
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

    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # TODO: Check if the team already has 6 Pokémon
            # TODO: If yes, print a message indicating the team is full

        # TODO: Check if the Pokémon is already in the team (case-insensitive)
            # TODO: If yes, print a message indicating duplication

        # TODO: Fetch Pokémon data from the PokéAPI (hint: httpx.get + status code check)

        # TODO: If successful, extract the fields you want to store (name, types, sprite URL)
            # TODO: Append the dictionary/object to self.members
            # TODO: Print a confirmation message
        # else:
            # TODO: Print an error message if the Pokémon is not found

# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
