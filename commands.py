"""Command parsing and handling for the AI agent."""

import re
from typing import Tuple, Optional
from inventory import Inventory


class CommandParser:
    """Parses natural language commands and executes them."""

    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def parse_and_execute(self, command: str) -> str:
        """Parse a natural language command and execute it."""
        command = command.strip().lower()

        # List/Show commands
        if self._matches(command, ["list", "show", "display"]):
            return self.inventory.list_all()

        # Total count
        if self._matches(command, ["total", "count", "how many"]):
            total = self.inventory.get_total_items()
            unique = len(self.inventory.items)
            return f"Total items: {total} units across {unique} different items"

        # Add commands
        if self._matches(command, ["add", "insert"]):
            return self._handle_add(command)

        # Remove commands
        if self._matches(command, ["remove", "delete", "take"]):
            return self._handle_remove(command)

        # Search commands
        if self._matches(command, ["search", "find", "where is", "look for"]):
            return self._handle_search(command)

        # Category query
        if "category" in command or "type" in command:
            return self._handle_category_search(command)

        # Help
        if self._matches(command, ["help", "?", "what can"]):
            return self._get_help()

        return "I didn't understand that command. Type 'help' for available commands."

    def _matches(self, command: str, keywords: list) -> bool:
        """Check if command matches any keyword."""
        return any(keyword in command for keyword in keywords)

    def _handle_add(self, command: str) -> str:
        """Handle add item commands."""
        # Pattern: "add X [item] [to category Y]"
        match = re.search(r"add\s+(\d+)\s+(.+?)(?:\s+to\s+category\s+(.+?))?(?:\s+to inventory)?$", command)
        if match:
            quantity = int(match.group(1))
            item_name = match.group(2).strip()
            category = match.group(3).strip() if match.group(3) else "General"
            return self.inventory.add_item(item_name, quantity, category)

        # Pattern: "add [item]"
        match = re.search(r"add\s+(.+?)(?:\s+to inventory)?$", command)
        if match:
            return self.inventory.add_item(match.group(1).strip())

        return "Couldn't parse add command. Try: 'add 5 apples' or 'add 10 oranges to category produce'"

    def _handle_remove(self, command: str) -> str:
        """Handle remove item commands."""
        # Pattern: "remove X [item]"
        match = re.search(r"remove\s+(\d+)\s+(.+?)$", command)
        if match:
            quantity = int(match.group(1))
            item_name = match.group(2).strip()
            return self.inventory.remove_item(item_name, quantity)

        # Pattern: "remove [item]"
        match = re.search(r"remove\s+(.+?)$", command)
        if match:
            return self.inventory.remove_item(match.group(1).strip())

        return "Couldn't parse remove command. Try: 'remove 2 apples' or 'remove oranges'"

    def _handle_search(self, command: str) -> str:
        """Handle search commands."""
        # Extract search term
        match = re.search(r"(?:search|find|where is|look for)\s+(.+?)$", command)
        if match:
            search_term = match.group(1).strip()
            results = self.inventory.search_by_name(search_term)
            if results:
                result_str = f"Found {len(results)} item(s):\n"
                for item in results:
                    result_str += f"  - {item.name}: {item.quantity} {item.unit} ({item.category})\n"
                return result_str
            return f"No items found matching '{search_term}'"

        return "Couldn't parse search command. Try: 'search apples' or 'find oranges'"

    def _handle_category_search(self, command: str) -> str:
        """Handle category search commands."""
        match = re.search(r"(?:show|list)\s+(?:all\s+)?(.+?)(?:\s+category)?$", command)
        if match:
            category = match.group(1).strip()
            results = self.inventory.search_by_category(category)
            if results:
                result_str = f"Items in '{category}' category:\n"
                for item in results:
                    result_str += f"  - {item.name}: {item.quantity} {item.unit}\n"
                return result_str
            return f"No items found in '{category}' category"

        return "Couldn't parse category command"

    def _get_help(self) -> str:
        """Return help message."""
        return """Available Commands:
  • add <quantity> <item> [to category <name>] - Add items
  • remove <quantity> <item> - Remove items
  • list / show / display - Show all items
  • search <term> / find <term> - Search for items
  • show <category> category - Show items in a category
  • total / count - Show total item count
  • help - Show this message

Examples:
  • add 5 apples to category produce
  • show all produce category
  • search oranges
  • remove 2 bananas
        """
