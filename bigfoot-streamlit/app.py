import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv("bfro_reports_fall2022.csv")


state_counts = df['state'].value_counts().reset_index()
state_counts.columns = ['state', 'count']


st.title("Bigfoot Sightings Analysis")
st.write("Explore two visualizations of Bigfoot sightings based on public reports.")
st.header("Sightings by State")

bar_chart1 = alt.Chart(state_counts).mark_bar().encode(
    x=alt.X('count:Q', title='Number of Sightings'),
    y=alt.Y('state:N', sort='-x', title='State'),
    color=alt.Color('count:Q', scale=alt.Scale(scheme='reds'))
).properties(
    title='Bigfoot Sightings by State',
    width=600, height=600
)

st.altair_chart(bar_chart1, use_container_width=True)

st.write("The bar chart showcases the number of Bigfoot sightings reported across the states in the U.S. On the y-axis, the states are displayed while on the x-axis, the number of sightings is placed. The chart is created in descending order, where the states that have the most sightings are on top. The chart colors indicate the number of sightings based on the darker tone bars. To create this bar chart, I decided to group the dataset by the state column and organize the number of sightings per state. I went with a bar chart because it makes it simpler to compare each state and its sightings. I selected the \"reds\" color scale to indicate the number of sightings, as it provides a clear distinction between lower and higher counts visually. The state values were used directly for the column. This chart helps reveal patterns in Bigfoot sightings, highlighting states with higher numbers of those reports, which suggest either more sightings of “Bigfoot” or a greater interest in Bigfoot-related topics, leading to more potential “sightings.”")


df['year'] = pd.to_datetime(df['date'], errors='coerce').dt.year
yearly_counts = df['year'].value_counts().sort_index().reset_index()
yearly_counts.columns = ['year', 'count']

st.header("Sightings Over Time")

bar_chart2 = alt.Chart(yearly_counts).mark_bar().encode(
    x='year:O',
    y='count:Q',
    color=alt.Color('count:Q', scale=alt.Scale(scheme='blues')),
    tooltip=['year', 'count']
).properties(
    title='Bigfoot Sightings by Year',
    width=600, height=600
)

st.altair_chart(bar_chart2, use_container_width=True)

st.write("For my next plot, I decided to visualize the number of Bigfoot sightings over the years, using a bar chart. On the x-axis, it represents the year of the sighting, and on the y-axis, it represents the count of sightings for each year. The chart takes the sightings by year, providing an overview of how the number of sightings has changed over time. I chose a color scale that varies based on the count of sightings. The color gradient uses the \"blues\" color scheme, which can visually emphasize the higher counts with darker shades similar to those of the first chart. I aggregated the dataset by year, counting the number of sightings for each year. I figured this would be an easier way to display the sightings in an easy-to-read manner. For interactivity, I added hover tooltips to the bars, so when hovering over any of the chart's bars, the year and the count of sightings for that year will be displayed. This allows for a more detailed viewing of each data point. Adding this interactivity enhances the user's experience by providing contextual information directly on the plot.")
