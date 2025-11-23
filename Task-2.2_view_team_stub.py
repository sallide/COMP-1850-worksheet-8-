"""
Exercise 2.2: View the Current Team (Stub)
- Implement a method to view the current team.
- Display each Pokémon's name, types, and image URL.
"""

import httpx

class Team:
    def __init__(self):
        """Initialize an empty team."""
        self.members = []
    
    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # (Implementation from Exercise 2.1)
        pass  # Remove this when implementing
    
    def view_team(self):
        """View the current team with details."""
        # TODO: Check if the team is empty
            # TODO: If empty, print a message indicating the team is empty
        pass  # Remove this when implementing
        
        # TODO: Print the team members with their details (numbering them with enumerate for readability)
        print("Your Team:")
        for idx, pokemon in enumerate(self.members, 1):
            # TODO: Extract and format the Pokémon's details
            pass
    
# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
# team.view_team()
