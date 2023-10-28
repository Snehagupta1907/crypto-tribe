import streamlit as st
import plotly.express as px
import requests
import pandas as pd
import base64 

base_url = 'https://api.cryptorank.io/v1'
api_key = 'api key'

def fetch_current_prices():
    endpoint = '/currencies'
    params = {'api_key': api_key, 'limit': 6000}
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    currencies = []
    for currency in data.get('data', []):
        name = currency.get('name', '')
        symbol = currency.get('symbol', '')
        price_usd = currency.get('values', {}).get('USD', {}).get('price', 0)
        currencies.append({"Name": name,"Symbol": symbol, "Price (USD)": price_usd})
    return currencies

exchange_data = {
    "Okk": [
        {"name": "SUI", "listing_price": "$0.100", "current_price": "$0.398"},
        {"name": "TAKI", "listing_price": "$0.04", "current_price": "$0.0069"},
        {"name": "ELT", "listing_price": "$0.009", "current_price": "$0.0000722"},
        {"name": "ORB", "listing_price": "$0.035", "current_price": "$0.0442"},
        {"name": "GARI", "listing_price": "$0.200", "current_price": "$0.0225"},
        {"name": "WGRT", "listing_price": "$0.003", "current_price": "$0.00329"},
        {"name": "NDN", "listing_price": "$0.006", "current_price": "0.005"},
        {"name": "DEP", "listing_price": "$0.0025", "current_price": "$0.000732"},
        {"name": "IMVU", "listing_price": "$0.00286", "current_price": "$0.00625"},
    ],
    "Coinstore": [
        {"name": "Innovator Metaverse (INVT)", "listing_price": "$0.01", "current_price": "$0.074146"},
        {"name": "KISSAN (KSN)", "listing_price": "$0.08", "current_price": "$0.09340"},
        {"name": "Sportzchain (SPN)", "listing_price": "$0.0024", "current_price": "$0.000036"},
        {"name": "Cointrading (CNT)", "listing_price": "$0.015", "current_price": "$0.05919"},
        {"name": "KeeDX (KDX)", "listing_price": "$0.25", "current_price": "$0.00066"},
        {"name": "Meta Warriors (MWS)", "listing_price": "$0.095", "current_price": "$0.00038"},
        {"name": "Social Innovation (SOIT)", "listing_price": "$0.008", "current_price": "$0.113958"},
        {"name": "PomeBox ($POMB)", "listing_price": "$0.016", "current_price": "$0.054980"},
        {"name": "NIKEL ($NIKL)", "listing_price": "$0.0801", "current_price": "$0.01019198"},
        {"name": "Hippo Wallet Token (HPO)", "listing_price": "$0.003", "current_price": "$0.003441"},
        {"name": "NORDEK ($NRK)", "listing_price": "$0.025", "current_price": "$0.044954"},
        {"name": "Damex.io (DAMEX)", "listing_price": "$0.15", "current_price": "$0.003448"},
        {"name": "Magic Shiba Starter ($MSHIB)", "listing_price": "$0.00001881", "current_price": "$0.0000078000"},
        {"name": "Royal Society NFT ($ROYSY)", "listing_price": "$0.0001", "current_price": "$0.0000045"},
        {"name": "Bearium", "listing_price": "$0.0067", "current_price": "$0.002104"},
        {"name": "BAJ Token", "listing_price": "$0.0010", "current_price": "$0.0000041"},
        {"name": "ixo", "listing_price": "$0.02", "current_price": "$0.00617"},
    ],
    
    "KuCoin": [
        {"name": "IMVU", "listing_price": "$0.00286", "current_price": "$0.00625"},
        {"name": "Sui", "listing_price": "$0.394", "current_price": "$0.100"},
        {"name": "Mechaverse", "listing_price": "$0.00342", "current_price": "$0.100"},
        {"name": "Fracton Protocol", "listing_price": "$1.77", "current_price": "$0.200"},
        {"name": "Pikaster", "listing_price": "$0.028", "current_price": "$0.120"},
        {"name": "Aurigami", "listing_price": "$0.0000851", "current_price": "$0.005"},
        {"name": "Melos Studio", "listing_price": "$0.00207", "current_price": "$0.05"},
        {"name": "Gari Network", "listing_price": "$0.0216", "current_price": "$0.200"},
        {"name": "ClearDAO", "listing_price": "$0.00187", "current_price": "$0.01"},
        {"name": "Chumbi Valley", "listing_price": "$0.000134", "current_price": "$0.001"},
        {"name": "Victoria VR", "listing_price": "$0.006", "current_price": "$0.00295"},
        {"name": "Cryowar", "listing_price": "$0.0067", "current_price": "$0.028"},
        {"name": "IX Swap", "listing_price": "$0.0111", "current_price": "$0.140"},
        {"name": "Lithium Finance", "listing_price": "$0.000247", "current_price": "$0.006"},
        {"name": "Burp", "listing_price": "$0.00034", "current_price": "$0.110"},
    ],
    "Bitmart":[
       {"name": "Crypto Tex", "listing_price": "$0.212", "current_price": "$0.212"},
       {"name": "O-MEE", "listing_price": "$0.000084", "current_price": "$0.000084"},
       {"name": "Hibiki Run", "listing_price": "$0.0038", "current_price": "$0.0038"},
       {"name": "Evadore", "listing_price": "$0.0988", "current_price": "$0.0988"},
       {"name": "RADA", "listing_price": "$0.00269", "current_price": "$0.00269"},
       {"name": "Family Over Everything", "listing_price": "$0.0107", "current_price": "$0.0107"},
       {"name": "CyberConnect", "listing_price": "$4.23", "current_price": "$4.23"},
       {"name": "Damex", "listing_price": "$0.0114", "current_price": "$0.0114"},
       {"name": "Quantum Hunter", "listing_price": "$0.0000102", "current_price": "$0.0000102"},
       {"name": "Crypto Tex", "listing_price": "$0.800", "current_price": "$0.05"},
       {"name": "O-MEE", "listing_price": "$0.007", "current_price": "$0.045"},
       {"name": "Hibiki Run", "listing_price": "$0.04", "current_price": "$0.016"},
       {"name": "Evadore", "listing_price": "$0.00225", "current_price": "$0.00085"},
       {"name": "RADA", "listing_price": "$1.80", "current_price": "$0.150"},
       {"name": "Family Over Everything", "listing_price": "$0.0075", "current_price": "$0.01"},
],

    "AscendEX":[
  {"name": "Waterfall DeFi", "listing_price": "$0.350", "current_price": "$0.000523"},
  {"name": "Jet Protocol", "listing_price": "$0.040", "current_price": "$0.00644"},
  {"name": "Oxygen", "listing_price": "$0.100", "current_price": "$0.0128"},
  {"name": "Showcase", "listing_price": "$0.075", "current_price": "$0.01"},
  {"name": "Persistence", "listing_price": "$0.400", "current_price": "$0.166"},
  {"name": "Maps.me", "listing_price": "$0.150", "current_price": "$0.0313"},
  {"name": "Bonfida", "listing_price": "$0.100", "current_price": "$0.160"},
  {"name": "The Virtua Kolect", "listing_price": "$0.012", "current_price": "$0.02"},
  {"name": "Akash Network", "listing_price": "$0.767", "current_price": "$0.841"},
  {"name": "StaFi", "listing_price": "$0.130", "current_price": "$0.263"},
  {"name": "Serum", "listing_price": "$0.170", "current_price": "$0.0319"},
],

"Gate.io ":[
  {"name": "ZTX", "listing_price": "$0.025", "current_price": "$0.0118"},
  {"name": "VinuChain", "listing_price": "$0.02", "current_price": "$0.0229"},
  {"name": "Raft", "listing_price": "$0.015", "current_price": "$0.00629"},
  {"name": "Phantom of the Kill", "listing_price": "$0.04", "current_price": "$0.0152"},
  {"name": "Tezos Domains", "listing_price": "$0.180", "current_price": "$0.0407"},
  {"name": "Soil", "listing_price": "$0.00138", "current_price": "$0.141"},
  {"name": "Cyber Arena", "listing_price": "$0.180", "current_price": "$0.000803"},
  {"name": "Archway", "listing_price": "$0.500", "current_price": "$0.0536"},
  {"name": "Kunji Finance", "listing_price": "$0.05", "current_price": "$0.0683"},
  {"name": "O-MEE", "listing_price": "$0.015", "current_price": "$0.000082"},
  {"name": "Connext", "listing_price": "$0.025", "current_price": "$0.0305"},
  {"name": "PymeDAO", "listing_price": "$0.02", "current_price": "$0.00128"},
],
 "Bybit" : [
  {"name": "Virtual Versions", "listing_price": "$0.007", "current_price": "$0.00626"},
  {"name": "Cashtree Token", "listing_price": "$0.0033", "current_price": "$0.0192"},
  {"name": "GameSwift", "listing_price": "$0.0144", "current_price": "$0.0691"},
  {"name": "Sui", "listing_price": "$0.100", "current_price": "$0.397"},
  {"name": "XCAD Network", "listing_price": "$0.01", "current_price": "$0.0148"},
  {"name": "Medieval Empires", "listing_price": "$0.01", "current_price": "$0.0034"},
  {"name": "PUML Better Health", "listing_price": "$0.07", "current_price": "$0.00946"},
  {"name": "MIBR", "listing_price": "$1.00", "current_price": "$0.181"},
  {"name": "Diamond Launch", "listing_price": "$0.02", "current_price": "$0.0748"},
],
 "HTX Primelist":[
  {"name": "HistoryDAO", "listing_price": "$0.01", "current_price": "$0.00167"},
  {"name": "Metababy", "listing_price": "$0.03", "current_price": "$0.0018"},
  {"name": "Hero Blaze: Three Kingdoms", "listing_price": "$0.120", "current_price": "$0.00943"},
  {"name": "Fellaz", "listing_price": "$0.100", "current_price": "$2.47"},
  {"name": "Walken", "listing_price": "$0.0165", "current_price": "$0.00402"},
  {"name": "SIGNIN", "listing_price": "$0.02", "current_price": "$0.0077"},
  {"name": "WeBuy", "listing_price": "$0.500", "current_price": "$0.259"},
  {"name": "Konnect", "listing_price": "$0.01", "current_price": "$0.0488"},
],

}

st.title("Crypto ROI Dashboard")

currencies = fetch_current_prices()

df2 = pd.DataFrame(currencies)

st.write("Current price")
st.write(df2)


selected_exchange = st.selectbox("Select an Exchange", list(exchange_data.keys()))

df = pd.DataFrame(exchange_data[selected_exchange])

df["current_price"] = df["current_price"].str.replace('$', '').astype(float)
df["listing_price"] = df["listing_price"].str.replace('$', '').astype(float)


df["ROI"] = ((df["current_price"] - df["listing_price"]) / df["listing_price"]) * 100

st.write("Price Data for Selected Exchange:")
st.write(df)

def update_prices(row):
    name = row['name']
    matching_rows = df2[df2['Name'].str.contains(fr"\b{name}\b", case=False, regex=True) | df2['Symbol'].str.contains(fr"\b{name}\b", case=False, regex=True)]   
    if not matching_rows.empty:
        prices = matching_rows['Price (USD)'].astype(str)
        row['Prices (USD)'] = ', '.join(prices)
    
    return row



df['Prices (USD)'] = ''
df = df.apply(update_prices, axis=1)


st.write("Updated Price Data for Selected Exchange:")
st.write(df)



st.write("Bar Chart:")
fig_bar = px.bar(
    df, x="name", y="ROI", title=f"ROI for Crypto Coins on {selected_exchange} Exchange", text="ROI",
    labels={"name": "Crypto Coin", "ROI": "ROI %"}
)
fig_bar.update_traces(marker_line_width=3, opacity=0.8)
fig_bar.update_layout(yaxis_tickformat="%")
st.plotly_chart(fig_bar)

st.write("Line Chart:")
fig_line = px.line(
    df, x="name", y=["listing_price", "current_price"],
    title=f"Price Comparison for Crypto Coins on {selected_exchange} Exchange",
    labels={"name": "Crypto Coin", "value": "Price (USDT)"}
)
fig_line.update_traces(line=dict(width=2))
st.plotly_chart(fig_line)
