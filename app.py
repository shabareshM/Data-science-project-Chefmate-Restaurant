import streamlit as st
from recommendation import *

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="ChefMate",
    page_icon="🍽",
    layout="wide"
)

st.title("🍽 ChefMate Restaurant Recommendation System")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.header("Restaurant Filters")

cities = get_cities()

if len(cities) == 0:
    st.error("No City data found in dataset.")
    st.stop()

city = st.sidebar.selectbox(
    "Select City",
    cities,
    key="city"
)

cuisines = get_cuisines()

if len(cuisines) == 0:
    st.error("No Cuisine data found in dataset.")
    st.stop()

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    cuisines,
    key="cuisine"
)

budget = st.sidebar.selectbox(
    "Budget",
    ["Budget", "Standard", "Premium"],
    key="budget"
)

rating = st.sidebar.slider(
    "Minimum Rating",
    min_value=0.0,
    max_value=5.0,
    value=4.0,
    step=0.1,
    key="rating"
)

search = st.sidebar.button(
    "Recommend Restaurants",
    key="recommend"
)

# ---------------------------------------------------
# Recommendation
# ---------------------------------------------------

if search:

    result = recommend(
        city,
        cuisine,
        budget,
        rating
    )

    if result.empty:

        st.warning("No restaurants found.")

    else:

        st.success(f"{len(result)} Restaurants Found")

        st.dataframe(
            result,
            use_container_width=True
        )

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="restaurant_recommendation.csv",
            mime="text/csv",
            key="download"
        )