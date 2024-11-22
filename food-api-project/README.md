# Food API Data Extraction Project

## Project Overview
This project uses [TheMealDB API](https://www.themealdb.com/api.php) to fetch recipes based on a search query.
 The data is processed using Python and saved into a structured CSV file.

## Features:
- Fetch meals containing a specific keyword.
- Extract details like meal name, category, area, instructions, and image URL.
- Save the data into a CSV file for further analysis.

## How to Use:
1. Clone the repository.
2. Install dependencies: `pip install requests pandas`.
3. Run `fetch_meals.py`.
4. Find the output in `meals_data.csv`.

## Sample Output:
| Meal_ID   | Meal_Name         | Category | Region    | Instructions          | Thumbnail_URL:                 |
|----------|-----------------|-------------|------------|--------------------------|------------------------------|
| 52772    | Chicken Handi   | Chicken     | Pakistani  | [Cooking Instructions]   | https://link-to-thumbnail.jpg|

