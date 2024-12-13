from src.file_operations.file_operation import start as start_file_operations
from src.text_analyser.text_analyser import start as start_text_analyser
from src.personal_journal.personal_journal import main as start_personal_journal
from src.random_quotes.random_quotes import start as start_random_quotes
from src.calc_func.calc import start as start_calculator
from src.task_manager.task_manager_app import main as start_task_manager


def main():
    while True:
        print("\nPersonal Assistant CLI")
        print("1. Task Manager")
        print("2. Journal")
        print("3. File Operations")
        print("4. Text Analyzer")
        print("5. Calculator")
        print("6. Random Quotes")
        print("7. Exit")
        choice=input("\n Choose an option:")

        if choice == "1":
            start_task_manager()
        elif choice == "2":
            start_personal_journal()
        elif choice == "3":
            start_file_operations()
        elif choice == "4":
            start_text_analyser()
        elif choice == "5":
            start_calculator()
        elif choice == "6":
            start_random_quotes()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Please enter valid numbers:")
main()