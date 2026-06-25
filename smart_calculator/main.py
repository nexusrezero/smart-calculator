# SMART CALCULATOR MAIN SYSTEM
# Handles menu and user interaction

# Load required modules
import calculator as calc
import number_tools as nt
import history as h

history = h.load_history()

# Display main menu
def show_menu():
    print("\n==============================")
    print("   SMART CALCULATOR v5")
    print("==============================")
    print("1. Calculator")
    print("2. Number Check")
    print("3. Even/Odd Check")
    print("4. View History")
    print("5. Clear History")
    print("6. Exit")

def calculator_mode():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1.Add 2.Subtract 3.Multiply 4.Divide")
    op = input("Choose operation: ")

    if op == "1":
        result = calc.add(a, b)
        action = "Addition"
    elif op == "2":
        result = calc.subtract(a, b)
        action = "Subtraction"
    elif op == "3":
        result = calc.multiply(a, b)
        action = "Multiplication"
    elif op == "4":
        result = calc.divide(a, b)
        action = "Division"
    else:
        print("Invalid operation")
        return

    print("Result:", result)
    item = f"{action}: {a}, {b} = {result}"
    history.append(item)
    h.save_history(item)

def number_mode():
    n = float(input("Enter number: "))
    result = nt.check_number(n)

    print(result)
    item = f"Number Check: {n} → {result}"
    history.append(item)
    h.save_history(item)

def even_odd_mode():
    n = int(input("Enter number: "))
    result = nt.check_even_odd(n)

    print(result)
    item = f"Even/Odd: {n} → {result}"
    history.append(item)
    h.save_history(item)

def view_history():
    print("\n===== HISTORY =====")
    if not history:
        print("No history yet.")
    else:
        for item in history:
            print("-", item)

def clear_history():
    history.clear()
    h.clear_history()
    print("History cleared.")

while True:
    show_menu()
    choice = input("\nEnter choice: ")

    if choice == "1":
        calculator_mode()
    elif choice == "2":
        number_mode()
    elif choice == "3":
        even_odd_mode()
    elif choice == "4":
        view_history()
    elif choice == "5":
        clear_history()
    elif choice == "6":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice")


