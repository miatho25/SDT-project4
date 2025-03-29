import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')

st.subheader("📊 Current Selection Overview")
st.write(f"Showing {filtered_df.shape[0]:,} listings based on selected filters.")


# App title
st.title("🚗 Car Sales Dashboard")

# Header
st.header("Distribution of Car Prices")

st.sidebar.header("Filter Listings")

# Filter by car type
car_types = df['type'].dropna().unique()
selected_types = st.sidebar.multiselect("Select car types", car_types, default=car_types)

# Filter by condition
conditions = df['condition'].dropna().unique()
selected_conditions = st.sidebar.multiselect("Select conditions", conditions, default=conditions)

# Apply filters
filtered_df = df[
    (df['type'].isin(selected_types)) &
    (df['condition'].isin(selected_conditions))
]

min_price, max_price = st.sidebar.slider(
    "Select price range",
    int(df['price'].min()), int(df['price'].max()),
    (int(df['price'].min()), int(df['price'].max()))
)

# Update the filtered DataFrame
filtered_df = filtered_df[
    (filtered_df['price'] >= min_price) & (filtered_df['price'] <= max_price)
]


# Histogram of car prices
fig_price = px.histogram(df, x='price', nbins=50, title="Price Distribution")
st.plotly_chart(fig_price)

fig_price = px.histogram(filtered_df, x='price', nbins=50, title="Price Distribution")


# Header
st.header("Odometer vs Price")

# Scatter plot
fig_scatter = px.scatter(df, x='odometer', y='price', title="Odometer Reading vs Price")
st.plotly_chart(fig_scatter)

fig_scatter = px.scatter(filtered_df, x='odometer', y='price', title="Odometer vs Price")


# Checkbox to show condition-based price box plot
if st.checkbox("Show price distribution by condition"):
    st.header("Price Distribution by Condition")
    fig_box = px.box(df, x='condition', y='price', title="Price by Vehicle Condition")
    st.plotly_chart(fig_box)

st.markdown("---")
st.caption("Made with ❤️ by miatho25 · [View on GitHub](https://github.com/miatho25/SDT-project4)")
