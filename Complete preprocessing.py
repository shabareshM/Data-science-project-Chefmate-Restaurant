import json
import pandas as pd

with open("file1.json","r",encoding="utf-8") as f:
    data=json.load(f)

restaurants=[]

for item in data:

    if "restaurants" in item:

        for r in item["restaurants"]:

            restaurant=r["restaurant"]

            restaurants.append({

                "Restaurant Name":restaurant.get("name"),

                "City":restaurant.get("location",{}).get("city"),

                "Address":restaurant.get("location",{}).get("address"),

                "Locality":restaurant.get("location",{}).get("locality"),

                "Latitude":restaurant.get("location",{}).get("latitude"),

                "Longitude":restaurant.get("location",{}).get("longitude"),

                "Cuisines":restaurant.get("cuisines"),

                "Average Cost for two":restaurant.get("average_cost_for_two"),

                "Aggregate rating":
                restaurant.get("user_rating",{}).get("aggregate_rating"),

                "Votes":
                restaurant.get("user_rating",{}).get("votes")

            })

df=pd.DataFrame(restaurants)

df["Aggregate rating"]=pd.to_numeric(
    df["Aggregate rating"],
    errors="coerce"
)

df["Votes"]=pd.to_numeric(
    df["Votes"],
    errors="coerce"
)

df["Average Cost for two"]=pd.to_numeric(
    df["Average Cost for two"],
    errors="coerce"
)

df["Primary Cuisine"]=df["Cuisines"].str.split(",").str[0].str.strip()

def budget(cost):

    if cost<=300:
        return "Budget"

    elif cost<=800:
        return "Standard"

    return "Premium"

df["Restaurant Category"]=df["Average Cost for two"].apply(budget)

df.to_csv("data/cleaned_restaurants.csv",index=False)

print(df.head())
print(df.columns.tolist())
print(df.shape)