#!/usr/bin/python3

import requests
import pandas as pd

# Define the base URL of the API
api_url = "https://www.themealdb.com/api/json/v1/1/search.php?s=chicken"

# Fetch JSON data from API
response = requests.get(api_url)
# Check if response is successful
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
    exit()

# Convert JSON to DataFrame
meals = data.get("meals")
df = pd.DataFRame(meals)

# Rename Columns
rename_dict = {
        "idMeal": "Meal_ID",
        "strMeal": "Meal_Name",
        "strCategory": "Category",
        "strArea": "Region",
        "strINstructions": "Instructions",
        "strMealThumb": "Thummbnail_URL",
}
df.rename(columns=rename_dict, inplace=True)

# Check columns after renaming
print("Columns after renaming:", df.columns)

# Select only the required columns 
expected_columns = ["Meal_ID", "Meal_Name", "Category", "Region", "Instruction", "Thumbnail_URL"]
available_columns = [col for col in expected_columns if col in df.columns]
df = df[available_columns]

# preview DataFrame
print(df.head)
