import streamlit as st
import pandas as pd
import altair as alt

exchange_data = {
    'Binance': {'percent': 1374.7, 'x': 13},
    'KuCoin Spotlight': {'percent': 126.7, 'x': 2},
    'Bitget': {'percent': 57.4, 'x': 0.5},
    'HTX Primelist': {'percent': 50.9, 'x': 0.5},
    'Bybit': {'percent': 41.7, 'x': 0.4},
    'OKX Jumpstart': {'percent': 33.2, 'x': 0.3},
    'BitMart': {'percent': -13.2, 'x': 0},
    'Bitforex Turbo Starter': {'percent': -26.8, 'x': 0},
    'AscendEX': {'percent': -30.6, 'x': 0},
    'Gate.io Startup': {'percent': -50.3, 'x': 0}
}


# Sort the data by return in descending order
sorted_data = sorted(exchange_data.items(), key=lambda x: x[1]['percent'], reverse=True)
exchange_names = [item[0] for item in sorted_data]
returns = [item[1]['percent'] for item in sorted_data]

# Create a DataFrame for the data
df = pd.DataFrame({'Exchange': exchange_names, 'Return': returns})

# Create a horizontal bar chart using Altair
st.title("Exchange Profit Data")
bar_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Return:Q', title='Return in Percent'),
    y=alt.Y('Exchange:O', title='Exchange'),
    color=alt.Color('Exchange:N', legend=None),
    tooltip=['Exchange:N', 'Return:Q']
).properties(width=600, height=300)

# Render the chart using st.altair_chart
st.altair_chart(bar_chart, use_container_width=True)

# Display the return in percent form when a bar is hovered over
selected_exchange = st.selectbox("Select an Exchange to see the return in percent:", exchange_names)
selected_return = [item[1]['percent'] for item in sorted_data if item[0] == selected_exchange][0]

if selected_exchange and selected_return:
    st.write(f"Selected: {selected_exchange}: {selected_return} percent")

st.write("Exchange Profit Data (in percent and 'x' amount):")
for exchange, data in sorted_data:
    st.write(f"{exchange}: {data['percent']} percent ({data['x']}x)")