from storage import initialize_expenses_storage, read_expenses_storage, write_expenses_storage, storage_file

def prompt_expense():
    date_str = input("Date (DD-MM-YYY): ").strip()
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    amount_str = input("Amount (No negative #'s): ").strip()
    
    print {
        "date": date_str,
        "category": category,
        "description": description,
        "amount": amount_str
    }

def main():
    
    initialize_expenses_storage()
    read_expenses_storage(storage_file)

    prompt_expense()
main()

