"""Main entry point for the AI Inventory Agent."""

from inventory import Inventory
from agent import InventoryAgent


def main():
    """Run the interactive inventory agent."""
    print("\n" + "=" * 60)
    print("         🤖 AI INVENTORY AGENT 📦")
    print("=" * 60)
    print("\nWelcome! I'm your AI inventory assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'quit' to exit.\n")

    # Initialize inventory and agent
    inventory = Inventory()
    agent = InventoryAgent(inventory)

    # Main interaction loop
    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Exit command
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("\nAgent: Goodbye! Your inventory has been saved. 👋\n")
                break

            # Process command
            response = agent.process_command(user_input)
            print(f"\nAgent: {response}\n")

        except KeyboardInterrupt:
            print("\n\nAgent: Inventory saved. See you soon! 👋\n")
            break
        except Exception as e:
            print(f"\nAgent: Sorry, an error occurred: {str(e)}\n")


if __name__ == "__main__":
    main()
