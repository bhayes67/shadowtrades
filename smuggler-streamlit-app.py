"""
STAR CITIZEN SMUGGLER'S ASSISTANT - WEB APP
Save this as 'smuggler_app.py' and run with: streamlit run smuggler_app.py
"""

import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import time

# Page config
st.set_page_config(
    page_title="SC Smuggler's Assistant",
    page_icon="🏴‍☠️",
    layout="wide"
)

# Cache data for 5 minutes
@st.cache_data(ttl=300)
def fetch_all_data():
    """Fetch all necessary data from UEX"""
    data = {}
    
    endpoints = {
        "commodities": "https://uexcorp.space/api/commodities",
        "prices": "https://uexcorp.space/api/commodities_prices_all",
        "terminals": "https://uexcorp.space/api/terminals",
        "stations": "https://uexcorp.space/api/space_stations",
        "systems": "https://uexcorp.space/api/star_systems"
    }
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, (key, url) in enumerate(endpoints.items()):
        status_text.text(f"Fetching {key}...")
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data[key] = response.json()["data"]
        except:
            data[key] = []
        
        progress_bar.progress((i + 1) / len(endpoints))
        time.sleep(0.2)
    
    status_text.empty()
    progress_bar.empty()
    
    return data

def find_illegal_drugs(commodities):
    """Find all illegal drugs that are tradeable"""
    drugs = []
    for item in commodities:
        if item.get("is_illegal") == 1 and item["price_buy"] > 0:
            drugs.append(item)
    return drugs

def get_drug_routes(drug_name, prices_data):
    """Get buy/sell locations for a specific drug"""
    buy_locations = []
    sell_locations = []
    
    for price in prices_data:
        if drug_name in price["commodity_name"]:
            if price["price_buy"] > 0 and price["scu_buy"] > 0:
                buy_locations.append({
                    "Terminal": price["terminal_name"],
                    "Buy Price": price["price_buy"],
                    "Stock": price["scu_buy"]
                })
            
            if price["price_sell"] > 0:
                sell_locations.append({
                    "Terminal": price["terminal_name"],
                    "Sell Price": price["price_sell"]
                })
    
    return buy_locations, sell_locations

def main():
    # Header
    st.title("🏴‍☠️ Star Citizen Smuggler's Assistant")
    st.markdown("*Real-time drug trading intelligence from UEX Corp*")
    
    # Sidebar
    st.sidebar.header("⚙️ Settings")
    
    # Fetch data
    with st.spinner("Connecting to underground networks..."):
        data = fetch_all_data()
    
    if not data.get("commodities"):
        st.error("Failed to connect to UEX. Please try again later.")
        return
    
    # Find illegal drugs
    illegal_drugs = find_illegal_drugs(data["commodities"])
    
    # Sidebar drug selector
    drug_names = [d["name"] for d in illegal_drugs]
    selected_drug = st.sidebar.selectbox(
        "Select Drug to Analyze",
        drug_names,
        index=0
    )
    
    # Main content area
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.metric("Active Drugs", len(illegal_drugs))
    with col2:
        st.metric("Total Terminals", len(data.get("terminals", [])))
    with col3:
        st.metric("Last Update", datetime.now().strftime("%H:%M"))
    
    # Drug overview
    st.header("💊 Illegal Commodities Market")
    
    drugs_df = pd.DataFrame([{
        "Name": d["name"],
        "Type": d["kind"],
        "Avg Buy": f"{d['price_buy']} aUEC",
        "Avg Sell": f"{d['price_sell']} aUEC",
        "Profit": f"{d['price_sell'] - d['price_buy']} aUEC",
        "Margin": f"{((d['price_sell'] - d['price_buy']) / d['price_buy'] * 100):.1f}%"
    } for d in illegal_drugs])
    
    st.dataframe(drugs_df, use_container_width=True)
    
    # Selected drug analysis
    st.header(f"🔍 {selected_drug} Trading Analysis")
    
    buy_locs, sell_locs = get_drug_routes(selected_drug, data["prices"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Buy Locations")
        if buy_locs:
            buy_df = pd.DataFrame(buy_locs).sort_values("Buy Price")
            st.dataframe(buy_df, use_container_width=True)
        else:
            st.warning("No buy locations found")
    
    with col2:
        st.subheader("💰 Sell Locations")
        if sell_locs:
            sell_df = pd.DataFrame(sell_locs).sort_values("Sell Price", ascending=False)
            st.dataframe(sell_df, use_container_width=True)
        else:
            st.warning("No sell locations found")
    
    # Best route calculation
    if buy_locs and sell_locs:
        st.header("🎯 Optimal Route")
        
        best_buy = min(buy_locs, key=lambda x: x["Buy Price"])
        best_sell = max(sell_locs, key=lambda x: x["Sell Price"])
        
        profit = best_sell["Sell Price"] - best_buy["Buy Price"]
        margin = (profit / best_buy["Buy Price"]) * 100
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info(f"**BUY:** {best_buy['Terminal']}")
            st.metric("Price", f"{best_buy['Buy Price']} aUEC")
            st.metric("Stock", f"{best_buy['Stock']} units")
        
        with col2:
            st.success(f"**SELL:** {best_sell['Terminal']}")
            st.metric("Price", f"{best_sell['Sell Price']} aUEC")
        
        with col3:
            st.warning("**PROFIT**")
            st.metric("Per Unit", f"{profit} aUEC")
            st.metric("Margin", f"{margin:.1f}%")
            st.metric("100 Units", f"{profit * 100:,} aUEC")
    
    # Safe havens
    st.header("🏴‍☠️ Safe Haven Terminals")
    
    safe_havens = []
    for price in data["prices"]:
        terminal = price["terminal_name"]
        if any(safe in terminal.upper() for safe in ["GRIM", "HEX", "PYRO", "RUIN", "CHECKMATE"]):
            if terminal not in [s["Terminal"] for s in safe_havens]:
                safe_havens.append({"Terminal": terminal, "System": "Unknown"})
    
    if safe_havens:
        st.dataframe(pd.DataFrame(safe_havens[:10]), use_container_width=True)
    
    # Tips
    with st.expander("💡 Smuggling Tips"):
        st.markdown("""
        - **Grim HEX** is the primary safe haven in Stanton
        - **All Pyro stations** have no security - everything is legal!
        - Mix legal cargo with contraband to reduce suspicion
        - Avoid direct quantum jumps to monitored stations
        - Check stock levels before long trips
        - Prices update frequently - refresh before each run
        """)
    
    # Footer
    st.divider()
    st.caption("Data provided by UEX Corp | Not affiliated with Cloud Imperium Games")
    
    # Refresh button
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

if __name__ == "__main__":
    main()
