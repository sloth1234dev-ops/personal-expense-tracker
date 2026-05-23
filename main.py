import json
from datetime import datetime


FILE_NAME = "expenses.json"
    
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

def save_data(data):
    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent = 4)   

def add_expense():
    print("\n---Add all your expenses---")
    category = input("Enter category (e.g., Food,Transport)").strip()
    amount = input("Enter amount:").strip()

    if not amount.isdigit():
        print("Wrong input.It must be a digit")
        return
    amount = int(amount)    
    expenses = load_data()
    # date time will be shown in YYYY-MM-DD this format
    current_date = datetime.now().strftime("%Y-%m-%d")
    new_item = {"category":category, "amount":amount, 'date':current_date}
    expenses.append(new_item)

    save_data(expenses)
    print(f"successfully {amount} Taka saved to this {category}")

def view_expenses():
    print("\n--- All Your Expenses (সব খরচ) ---")
    
    # ১. ফাইল থেকে ডাটা লোড করা
    expenses = load_data()
    
    # ২. জেসন ফাইল বা লিস্ট যদি খালি থাকে
    if len(expenses) == 0:
        print("No expenses found! Please add some first.")
        return
        
    # ৩. মোট খরচ হিসাব করার ভেরিয়েবল
    total_amount = 0
    
    # ৪. লুপ চালিয়ে একটা একটা করে খরচ স্ক্রিনে দেখানো
    print("---------------------------------")
    for item in expenses:
        print(f"Category: {item['category']} | Amount: {item['amount']} Taka")
        
        # প্রতিটা খরচের টাকা টোটালের সাথে যোগ হচ্ছে
        total_amount = total_amount + item['amount']
    print("---------------------------------")
    
    # ৫. লুপ শেষ হওয়ার পর সর্বমোট খরচ দেখানো
    print(f"Total Spent: {total_amount} Taka")

def delete_expenses():
    expenses = load_data()

    if len(expenses) == 0:
        print("No expenses to delete! Please add some first.")
        return
    print("-----------------------------------")
    for index,exp in enumerate(expenses,start = 1):
        print(f"{index}.Category: {exp['category']}   |   Amount: {exp['amount']} Taka")
    print("-----------------------------------")

    choice = input("Enter the number of the expense you want to delete ").strip()
    if not choice.isdigit():
        print("Wrong input. Please enter in valid format.")        
        return
    choice = int(choice)

    if 1 <= choice <= len(expenses):
        deleted_expense = expenses.pop(choice -1) 
        save_data(expenses)
        print(f"Deleted expense: Category: {deleted_expense['category']} | Amount: {deleted_expense['amount']} Taka")
    else:
        print("Invalid choice. Please enter a valid number.")
def update_expense():
    print("\n--- Update an Expense (খরচ সংশোধন করুন) ---")
    expenses = load_data()
    
    if len(expenses) == 0:
        print("No expenses found to update!")
        return
        
    print("-----------------------------------")
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. Category: {exp['category']} | Amount: {exp['amount']} Taka")
    print("-----------------------------------")

    choice = input("Enter the number of the expense you want to update: ").strip()
    if not choice.isdigit():
        print("Wrong input. Please enter a valid number.")
        return
        
    choice = int(choice)
    
    if 1 <= choice <= len(expenses):
        selected_expense = expenses[choice - 1]
        # ফিক্সড: এখানে selected_expense (একবচন) করা হয়েছে
        print(f"Selected Expense: Category: {selected_expense['category']} | Amount: {selected_expense['amount']} Taka")

        new_category = input("Enter new category: ").strip()
        new_amount = input("Enter new amount: ").strip()
        
        if not new_amount.isdigit():
            print("Wrong input. Amount must be a digit.")
            return
            
        # ফিক্সড: নাম ঠিক করা হয়েছে এবং ইনডেন্টেশন সোজা করা হয়েছে
        selected_expense['category'] = new_category
        selected_expense['amount'] = int(new_amount)
        
        # 🎯 এখনকার কাজ: আপডেট হওয়া ডাটা ফাইলে সেভ করা
        save_data(expenses)
        print("✅ Expense updated successfully!")
        
    else:
        print("Invalid choice. Please enter a valid number.")


def clear_all_expenses():
    print("\n--- Clear All Expenses ---")
    expenses = load_data()
    if len(expenses) == 0:
        print("No expenses to clear! Please add some first.")
        return
    
    confirmation = input("Are you sure you want to clear all expenses? (yes/no): ").strip().lower()

    if confirmation == "yes":
        save_data([])
        print("✅All expenses have been cleared successfully.")
    else:
        print("Clear operation cancelled.")    

def filter_by_date():
    print("\n--- Filter Expenses by Date ---")
    expenses = load_data()

    if len(expenses) == 0:
        print("No expenses found to filter!")
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_total = 0
    found = False

    print(f"Expenses for today ({today}):")
    print("-----------------------------------")
    for item in expenses:
        if item.get('date') == today:
            print(f"Category: {item['category']} | Amount: {item['amount']} Taka")
            today_total += item['amount']
            found = True
    print("-----------------------------------")
    if not found:
        print("No expenses found for today.")
    else:
        print(f"Total spent today: {today_total} Taka")

def main_menu():
    while True:
        print("\n=== SMART EXPENSE TRACKER ===")
        print("1. Add Expense (খরচ যোগ করুন)")
        print("2. View All Expenses (সব খরচ দেখুন)")
        print("3. View Today's Expenses (আজকের খরচ দেখুন)")
        print("4. Update an Expense (খরচ সংশোধন করুন)")
        print("5. Delete an Expense (একটি খরচ মুছে ফেলুন)")
        print("6. Clear All Expenses (সব খরচ মুছে ফেলুন)")
        print("7. Exit (প্রস্থান করুন)")        

        choice = input("Enter as your preference: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_date()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expenses()
        elif choice == "6":
            clear_all_expenses()
        elif choice == "7":
            print("OK Exiting the app.")
            break
        else:
            print("Your input method incorrect.Please try again")           

if __name__ == "__main__":
    main_menu()

    