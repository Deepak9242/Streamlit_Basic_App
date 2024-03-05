import pandas as pd
import plotly.graph_objects as go
import streamlit as st



# Function to calculate invalid data
def calculate_invalid_data(df):
    df['fare_invalidity'] = False
    df['trip_invalidity'] = False
    df['passenger_invalidity'] = False
    df['date_invalidity'] = False
    df['invalid'] = False
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'],dayfirst=True)
    df.loc[df['fare_amount'] < 0, 'fare_invalidity'] = True
    df.loc[df['fare_amount'].isnull(), 'fare_invalidity'] = True
    df.loc[df['trip_distance'] < 0, 'trip_invalidity'] = True
    df.loc[df['trip_distance'].isnull(), 'trip_invalidity'] = True
    df.loc[df['passenger_count'] < 0, 'passenger_invalidity'] = True
    df.loc[df['passenger_count'].isnull(), 'passenger_invalidity'] = True
    df['date_invalidity'] = ~(df['pickup_datetime'].dt.year == 2020) & (df['pickup_datetime'].dt.month == 1)
    df['invalid'] = (df['fare_invalidity']) | (df['trip_invalidity']) | (df['passenger_invalidity']) | (df['date_invalidity'])

# Function to generate the invalidity chart
def get_invalid_chart(df):
    # Calculate total rows
    total_rows = df.shape[0]

    # Data for pie charts
    pie_labels = ['Valid', 'Invalid']

    # Plotting the first pie chart (Distribution of Invalid Fare)
    invalid_fare = df[df['fare_invalidity']].shape[0]
    fare_values = [total_rows - invalid_fare, invalid_fare]

    # Plotting the second pie chart (Distribution of Invalid Trip)
    invalid_trip = df[df['trip_invalidity']].shape[0]
    trip_values = [total_rows - invalid_trip, invalid_trip]

    # Plotting the third pie chart (Distribution of Invalid Date)
    invalid_date = df[df['date_invalidity']].shape[0]
    date_values = [total_rows - invalid_date, invalid_date]

    # Plotting the fourth pie chart (Distribution of Invalid Passenger Count)
    invalid_passenger = df[df['passenger_invalidity']].shape[0]
    passenger_values = [total_rows - invalid_passenger, invalid_passenger]

    # Create Pie chart figures
    fig_fare = go.Figure(data=[go.Pie(labels=pie_labels, values=fare_values,)])
    fig_fare.update_layout(title_text="Distribution of Invalid Fare", title_font_size=20)
    
 
    fig_trip = go.Figure(data=[go.Pie(labels=pie_labels, values=trip_values)])
    fig_trip.update_layout(title_text="Distribution of Invalid Trip Distance", title_font_size=20)

    fig_date = go.Figure(data=[go.Pie(labels=pie_labels, values=date_values)])
    fig_date.update_layout(title_text="Distribution of Invalid Date", title_font_size=20)

 
    fig_passenger = go.Figure(data=[go.Pie(labels=pie_labels, values=passenger_values)])
    fig_passenger.update_layout(title_text="Distribution of Invalid Passenger", title_font_size=20)

 

    return fig_fare, fig_trip, fig_date, fig_passenger

# Main function to run the Streamlit app
def get_plot(df):
    st.divider()
    st.subheader('Invalidity Analysis')
    st.divider()

    # Calculate invalid data
    calculate_invalid_data(df)


    # Generate and display the pie charts
    fig_fare, fig_trip, fig_date, fig_passenger = get_invalid_chart(df)

    # Display the chart
    st.plotly_chart(fig_passenger)
    st.divider()
    st.plotly_chart(fig_trip)
    st.divider()
    st.plotly_chart(fig_date)
    st.divider()
    st.plotly_chart(fig_fare)
   


