import pandas as pd

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv("data/cleaned_restaurants.csv")

# Remove spaces from column names
df.columns = df.columns.str.strip()

# =====================================================
# Rename Columns (if needed)
# =====================================================

rename_columns = {
    "location.city": "City",
    "location_city": "City",
    "city": "City",
    "name": "Restaurant Name",
    "restaurant.name": "Restaurant Name",
    "aggregate_rating": "Aggregate rating",
    "average_cost_for_two": "Average Cost for two",
    "votes": "Votes",
    "cuisines": "Cuisines"
}

df.rename(columns=rename_columns, inplace=True)

# =====================================================
# Create Restaurant Category
# =====================================================

if "Restaurant Category" not in df.columns:

    if "Average Cost for two" in df.columns:

        def category(cost):

            if pd.isna(cost):
                return "Unknown"

            elif cost <= 300:
                return "Budget"

            elif cost <= 800:
                return "Standard"

            else:
                return "Premium"

        df["Restaurant Category"] = df["Average Cost for two"].apply(category)

# =====================================================
# Create Primary Cuisine
# =====================================================

if "Primary Cuisine" not in df.columns:

    if "Cuisines" in df.columns:

        df["Primary Cuisine"] = (
            df["Cuisines"]
            .astype(str)
            .str.split(",")
            .str[0]
            .str.strip()
        )

# =====================================================
# Get Cities
# =====================================================

def get_cities():

    if "City" not in df.columns:
        return []

    cities = (
        df["City"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
    )

    return sorted(cities)

# =====================================================
# Get Cuisines
# =====================================================

def get_cuisines():

    if "Primary Cuisine" in df.columns:

        cuisines = (
            df["Primary Cuisine"]
            .dropna()
            .astype(str)
            .unique()
        )

        return sorted(cuisines)

    return []

# =====================================================
# Recommendation Function
# =====================================================

def recommend(city, cuisine, budget, rating):

    data = df.copy()

    # -------------------------
    # City Filter
    # -------------------------

    if city != "All":

        data = data[
            data["City"].astype(str).str.lower()
            ==
            city.lower()
        ]

    # -------------------------
    # Cuisine Filter
    # -------------------------

    if cuisine != "All":

        data = data[
            data["Primary Cuisine"].astype(str).str.lower()
            ==
            cuisine.lower()
        ]

    # -------------------------
    # Budget Filter
    # -------------------------

    if budget != "All":

        data = data[
            data["Restaurant Category"]
            ==
            budget
        ]

    # -------------------------
    # Rating Filter
    # -------------------------

    if "Aggregate rating" in data.columns:

        data = data[
            data["Aggregate rating"] >= rating
        ]

    # -------------------------
    # Sort
    # -------------------------

    if "Votes" in data.columns:

        data = data.sort_values(
            by=["Aggregate rating", "Votes"],
            ascending=False
        )

    else:

        data = data.sort_values(
            by="Aggregate rating",
            ascending=False
        )

    # -------------------------
    # Display Columns
    # -------------------------

    display_columns = []

    for col in [

        "Restaurant Name",
        "City",
        "Primary Cuisine",
        "Average Cost for two",
        "Aggregate rating",
        "Votes",
        "Restaurant Category"

    ]:

        if col in data.columns:
            display_columns.append(col)

    return data[display_columns]

