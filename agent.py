"""AI Agent interface for inventory management."""

from commands import CommandParser
from inventory import Inventory


class InventoryAgent:
    """AI Agent for managing inventory through natural language."""

    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.command_parser = CommandParser(inventory)
        self.conversation_history = []

    def process_command(self, user_input: str) -> str:
        """Process a user command and return a response."""
        # Store in history
        self.conversation_history.append({"user": user_input})

        # Parse and execute command
        response = self.command_parser.parse_and_execute(user_input)

        # Store response
        self.conversation_history[-1]["agent"] = response

        # Save inventory after each command
        self.inventory.save()

        return response

    def get_history(self):
        """Get conversation history."""
        return self.conversation_history

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
