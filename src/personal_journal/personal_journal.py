import json
import os
from datetime import datetime

# File to store journal entries
JOURNAL_FILE = "journal.json"

def load_entries():
    """Load journal entries from the file."""
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r") as file:
            return json.load(file)
    return []

def save_entries(entries):
    """Save journal entries to the file."""
    with open(JOURNAL_FILE, "w") as file:
        json.dump(entries, file, indent=4)

def create_entry():
    """Create a new journal entry."""
    content = input("Enter your journal entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"timestamp": timestamp, "content": content}
    entries.append(entry)
    save_entries(entries)
    print("\nEntry added successfully!\n")

def view_entries():
    """View all journal entries."""
    if not entries:
        print("\nNo entries found.\n")
        return

    print("\nYour Journal Entries:")
    for i, entry in enumerate(entries, start=1):
        print(f"{i}. [{entry['timestamp']}]\n   {entry['content']}\n")

def search_entries():
    """Search for journal entries by date."""
    date = input("Enter the date to search for (YYYY-MM-DD): ")
    matching_entries = [entry for entry in entries if entry['timestamp'].startswith(date)]

    if not matching_entries:
        print("\nNo entries found for the specified date.\n")
        return

    print("\nMatching Entries:")
    for i, entry in enumerate(matching_entries, start=1):
        print(f"{i}. [{entry['timestamp']}]\n   {entry['content']}\n")

def main():
    """Main function to run the CLI app."""
    while True:
        print("\nPersonal Journal")
        print("1. Create a new entry")
        print("2. View all entries")
        print("3. Search entries by date")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

# Load existing entries
entries = load_entries()

# Call main() directly
# main()
