import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')

# App title
st.title("🚗 Car Sales Dashboard")

# Header
st.header("Distribution of Car Prices")

# Histogram of car prices
fig_price = px.histogram(df, x='price', nbins=50, title="Price Distribution")
st.plotly_chart(fig_price)

# Header
st.header("Odometer vs Price")

# Scatter plot
fig_scatter = px.scatter(df, x='odometer', y='price', title="Odometer Reading vs Price")
st.plotly_chart(fig_scatter)

# Checkbox to show condition-based price box plot
if st.checkbox("Show price distribution by condition"):
    st.header("Price Distribution by Condition")
    fig_box = px.box(df, x='condition', y='price', title="Price by Vehicle Condition")
    st.plotly_chart(fig_box)
