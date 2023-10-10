# Table with right-aligned numbers
item = "Item"
price = "Price"
quantity = "Quantity"
total = "Total"

table = f"| {item:>10} | {price:>10} | {quantity:>10} | {total:>10} |\n"
table += f"| {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12} |\n"
table += f"| {'Apple':>10} | {'$1.50':>10} | {'5':>10} | {'$7.50':>10} |\n"
table += f"| {'Banana':>10} | {'$0.75':>10} | {'3':>10} | {'$2.25':>10} |\n"
table += f"| {'Orange':>10} | {'$2.00':>10} | {'2':>10} | {'$4.00':>10} |\n"

print(table)