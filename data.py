import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

# ----------------------------
# Customers Dataset (5,000)
# ----------------------------
n_customers = 5000

customers = pd.DataFrame({
    "customer_id": range(1, n_customers+1),
    "gender": np.random.choice(["Male", "Female"], n_customers),
    "age": np.random.randint(18, 65, n_customers),
    "region": np.random.choice(["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Nakuru"], n_customers),
    "signup_date": pd.to_datetime(np.random.choice(pd.date_range("2022-01-01", "2024-12-31"), n_customers))
})

customers.to_csv("Data/customers.csv", index=False)


# ----------------------------
# Products Dataset (200)
# ----------------------------
n_products = 200

products = pd.DataFrame({
    "product_id": range(1, n_products+1),
    "category": np.random.choice(["Electronics", "Fashion", "Home", "Health", "Sports"], n_products),
    "price": np.round(np.random.uniform(500, 50000, n_products), 2)
})

products.to_csv("Data/products.csv", index=False)


# ----------------------------
# Orders Dataset (50,000)
# ----------------------------
n_orders = 50000

orders = pd.DataFrame({
    "order_id": range(1, n_orders+1),
    "customer_id": np.random.randint(1, n_customers+1, n_orders),
    "product_id": np.random.randint(1, n_products+1, n_orders),
    "quantity": np.random.randint(1, 5, n_orders),
    "order_date": pd.to_datetime(np.random.choice(pd.date_range("2023-01-01", "2024-12-31"), n_orders))
})

orders.to_csv("Data/orders.csv", index=False)


# ----------------------------
# Payments Dataset (50,000)
# ----------------------------
payments = pd.DataFrame({
    "order_id": range(1, n_orders+1),
    "payment_method": np.random.choice(["M-Pesa", "Card", "Cash on Delivery"], n_orders),
    "payment_status": np.random.choice(["Completed", "Failed", "Refunded"], n_orders, p=[0.85, 0.10, 0.05])
})

payments.to_csv("Data/payments.csv", index=False)
print("All datasets saved inside the 'Data' folder successfully.")