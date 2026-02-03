from storage import (
    storage_file,
    read_expenses_storage,
)
from datetime import datetime

def monthly_total(user_year, user_month):
    amounts = []
    total = 0
    category_totals = {}


    expense_list = read_expenses_storage(storage_file)

    for row in expense_list:
        parsed_data = datetime.strptime(row["date"], "%m-%d-%Y")
        if parsed_data.year == user_year and parsed_data.month == user_month:
            amounts.append(float(row["amount"]))
            if row["category"] in category_totals:
                category_totals[row["category"]] += float(row["amount"])
            else:
                category_totals[row["category"]] = float(row["amount"])
    for amount in amounts:
        amount += total
        total = amount

    return total, category_totals