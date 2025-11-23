"""
Exercise 2.3: Remove Pokémon from the Team (Stub)
- Implement a method to remove a Pokémon from the team by name.
- Make sure the team size is updated accordingly.
"""

import httpx

class Team:
    def __init__(self):
        """Initialise an empty team."""
        self.members = []
    
    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # (Implementation from Exercise 2.1)
        pass  # Remove this when implementing
    
    def view_team(self):
        """View the current team with details."""
        # (Implementation from Exercise 2.2)
        pass  # Remove this when implementing
    
    def remove_pokemon(self, name):
        """Remove a Pokémon from the team by name."""
        # TODO: Find the Pokémon in the team
            # TODO: If found, remove it and print a confirmation message
            # TODO: If not found, print a message indicating the Pokémon is not in the team
        pass

# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
# team.view_team()
# team.remove_pokemon("squirtle")
# team.view_team()
