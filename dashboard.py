# dashboard.py

import pandas as pd
import matplotlib.pyplotpip as plt
import seaborn as sns
import streamlit as st

# Load datasets
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Title of the dashboard
st.title("Bike Sharing Data Analysis Dashboard")

# Display the datasets
if st.checkbox('Show Day Data'):
    st.write(day_df.head())

if st.checkbox('Show Hour Data'):
    st.write(hour_df.head())

# Average rentals by season
st.subheader("Average Rentals by Season")
seasonal_rentals = day_df.groupby('season')['cnt'].mean()
seasonal_rentals_plot = seasonal_rentals.plot(kind='bar', color='skyblue')
plt.title('Average Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Average Rentals')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Winter', 'Spring', 'Summer', 'Fall'], rotation=45)
plt.grid(axis='y')

# Show seasonal rentals plot
st.pyplot()

# Total rentals by hour
st.subheader("Total Rentals by Hour of Day")
hourly_rentals = hour_df.groupby('hr')['cnt'].sum()
hourly_rentals_plot = hourly_rentals.plot(kind='line', title='Total Rentals by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Total Rentals')
plt.xticks(range(0, 24), rotation=45)
plt.grid()

# Show hourly rentals plot
st.pyplot()

# Scatter plot for temperature vs rentals
st.subheader("Bike Rentals vs. Temperature")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df, alpha=0.6, color='green')
plt.title('Bike Rentals vs. Temperature')
plt.xlabel('Temperature (Normalized)')
plt.ylabel('Total Rentals')
plt.grid()

# Show temperature vs rentals plot
st.pyplot()

# Conclusion Section
st.subheader("Conclusions")
st.write("1. Bike rentals are significantly higher during spring and summer.")
st.write("2. Higher temperatures lead to increased bike rentals.")
