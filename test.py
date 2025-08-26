def performMathOperation(a, b):
    """
    This function performs a mathematical operation on two numbers.
    It returns the sum of the two numbers.
    """
    return a + b

import pandas as pd
import random
from faker import Faker

fake = Faker()

# Sample product and category lists
products = [
    ("Laptop", "Electronics"),
    ("Smartphone", "Electronics"),
    ("Desk Chair", "Furniture"),
    ("Notebook", "Stationery"),
    ("Pen", "Stationery"),
    ("Monitor", "Electronics"),
    ("Coffee Table", "Furniture"),
    ("Backpack", "Accessories")
]

regions = ["North", "South", "East", "West"]

# Generate sample data
data = []
for i in range(100):  # 100 orders
    product, category = random.choice(products)
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(5.0, 1500.0), 2)
    order_date = fake.date_between(start_date='-1y', end_date='today')
    customer_name = fake.name()
    region = random.choice(regions)
    sales = round(quantity * unit_price, 2)

    data.append({
        "Order ID": f"ORD{i+1:04d}",
        "Customer Name": customer_name,
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit Price": unit_price,
        "Order Date": order_date,
        "Region": region,
        "Sales": sales
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("sample_order_sales.csv", index=False)

print(df.head())


