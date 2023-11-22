import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
url = "/content/day.csv"  # Gantilah link dengan link dataset yang sesuai
bike_data = pd.read_csv(url)

# Set the title of the web app
st.title("Bike Sharing Dashboard")

# Add a section for data exploration
st.header("Data Exploration")

# Display the first few rows of the dataset
st.write("### Bike Sharing Data Overview")
st.write(bike_data.head())

# Display summary statistics
st.write("### Summary Statistics")
st.write(bike_data.describe())

# Add a section for visualizations
st.header("Visualizations")

# Line chart: Hourly trend of bike rental count
hourly_trend_chart = px.line(bike_data, x='hr', y='cnt', title='Hourly Trend of Bike Rental Count')
st.plotly_chart(hourly_trend_chart)

# Line chart: Total bike rental count during Hurricane Sandy event
sandy_event_chart = px.line(bike_data[(bike_data['dteday'] >= '2012-10-29') & (bike_data['dteday'] <= '2012-10-31')],
                            x='dteday', y='cnt', title='Total Bike Rental Count During Hurricane Sandy Event')
st.plotly_chart(sandy_event_chart)
