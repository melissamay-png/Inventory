# AI Inventory Agent

An interactive inventory management system powered by an AI agent that processes natural language commands.

## Features

- 📦 **Add/Remove Items** - Manage inventory items dynamically
- 🔍 **Search & Filter** - Find items by name, category, or quantity
- 🤖 **AI Agent** - Natural language interface for inventory operations
- 💾 **Persistent Storage** - Save inventory to JSON
- 📊 **Reporting** - Generate inventory reports

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Then interact with the agent using natural language:
- "Add 5 apples to inventory"
- "How many items do we have?"
- "Show me everything in the produce category"
- "Remove 2 oranges"

## Project Structure

```
.
├── main.py                 # Entry point
├── inventory.py            # Inventory management
├── agent.py                # AI agent logic
├── commands.py             # Command handlers
├── requirements.txt        # Dependencies
└── inventory_data.json     # Persistent storage
```
