# Import necessary libraries
import pandas as pd
import numpy as np
import random
import datetime

# Create an empty DataFrame
df = pd.DataFrame()

# Define min and max dates
min_date = datetime.date(2000,1,1)
max_date = datetime.date(2025,12,31)

# Define liked foods list
liked_food = ["Pizza","Burger","Stake","Pastha","Fried Chicken"]

# Create a date range
date_range = pd.date_range(start=min_date, end=max_date, freq='D')

# Generate data for the DataFrame
df["ID"] = range(1,100001)  # Unique IDs
df["Date"] = np.random.choice(date_range,size=len(df))  # Random dates
df["Food"] = np.random.choice(liked_food,size=len(df))  # Random food choices
df["Quantity"] = np.random.choice(range(1,15),size=len(df))  # Random quantities
df["Price"] = np.where(df["Food"].isin(["Pizza","Burger","Fried Chicken"]), np.random.randint(10,16), 25)  # Price based on food
df["Sales"] = df["Quantity"] * df["Price"]  # Calculate sales

# View the first few rows
df.head()
