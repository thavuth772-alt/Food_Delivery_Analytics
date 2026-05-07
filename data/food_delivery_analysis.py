# Import Required Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv('data/food_orders.csv')

# Display Dataset

print("\n FOOD DELIVERY DATASET")
print(df)

# --------------------------------------------
# Total Revenue Calculation
# --------------------------------------------

df['TotalAmount'] = df['Quantity'] * df['Price']

total_revenue = df['TotalAmount'].sum()

print("\n TOTAL REVENUE")
print(total_revenue)

# --------------------------------------------
# Most Popular Food Items
# --------------------------------------------

popular_food = df.groupby('FoodItem')['Quantity'].sum()

print("\n MOST POPULAR FOOD ITEMS")
print(popular_food.sort_values(ascending=False))

# --------------------------------------------
# Orders by Location
# --------------------------------------------

location_orders = df['Location'].value_counts()

print("\n ORDERS BY LOCATION")
print(location_orders)

# --------------------------------------------
# Peak Order Time Analysis
# --------------------------------------------

# Extract Hour from OrderTime

df['Hour'] = pd.to_datetime(df['OrderTime'], format='%H:%M').dt.hour

peak_orders = df.groupby('Hour')['OrderID'].count()

print("\n PEAK ORDER HOURS")
print(peak_orders)

# --------------------------------------------
# Highest Revenue Food Item
# --------------------------------------------

food_revenue = df.groupby('FoodItem')['TotalAmount'].sum()

print("\n HIGHEST REVENUE FOOD ITEMS")
print(food_revenue.sort_values(ascending=False))

# --------------------------------------------
# Visualization 1 - Popular Food Items
# --------------------------------------------

plt.figure(figsize=(8,5))

popular_food.sort_values(ascending=False).plot(kind='bar')

plt.title('Most Popular Food Items')
plt.xlabel('Food Items')
plt.ylabel('Total Quantity Sold')

plt.tight_layout()

plt.show()

# --------------------------------------------
# Visualization 2 - Orders by Location
# --------------------------------------------

plt.figure(figsize=(8,5))

location_orders.plot(kind='bar')

plt.title('Orders by Location')
plt.xlabel('Location')
plt.ylabel('Number of Orders')

plt.tight_layout()

plt.show()

# --------------------------------------------
# Visualization 3 - Peak Order Hours
# --------------------------------------------

plt.figure(figsize=(10,5))

peak_orders.plot(kind='line', marker='o')

plt.title('Peak Order Hours')
plt.xlabel('Hour')
plt.ylabel('Number of Orders')

plt.grid(True)

plt.tight_layout()

plt.show()

# --------------------------------------------
# Visualization 4 - Revenue by Food Item
# --------------------------------------------

plt.figure(figsize=(8,5))

food_revenue.sort_values(ascending=False).plot(kind='pie', autopct='%1.1f%%')

plt.title('Revenue Contribution by Food Item')
plt.ylabel('')

plt.tight_layout()

plt.show()

# --------------------------------------------
# Business Insights
# --------------------------------------------

print("\n BUSINESS INSIGHTS")

print("""
1. Identify high-demand food items for inventory planning.

2. Peak ordering hours help optimize delivery staff allocation.

3. Revenue analysis helps prioritize profitable menu items.

4. Location-wise analysis supports targeted marketing strategies.

5. Customer ordering patterns improve operational efficiency.
""")