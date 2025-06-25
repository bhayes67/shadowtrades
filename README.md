# shadowtrades

# 🏴‍☠️ Star Citizen Smuggler's Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Star Citizen](https://img.shields.io/badge/Star%20Citizen-4.0-green.svg)](https://robertsspaceindustries.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A real-time trading intelligence app for Star Citizen smugglers and traders, focusing on high-risk, high-reward cargo runs across Stanton and Pyro systems.

![Smuggler's Assistant Demo](demo_screenshot.png)

## 🎯 Features

### Core Functionality
- **Real-time Price Data** - Live commodity prices from UEX Corp API
- **Illegal Goods Tracking** - Identifies all tradeable contraband
- **Terminal Locations** - Shows exactly where to buy and sell each drug
- **Profit Calculations** - Instant profit margins and route optimization
- **Safe Haven Identification** - Highlights unmonitored locations like Grim HEX
- **Stock Levels** - Current availability at each terminal
- **Cross-System Support** - Includes both Stanton and Pyro systems

### Why Use This Tool?
- 🚀 **Adventure First** - Prioritizes interesting routes over pure profit
- 🏴‍☠️ **Smuggling Focus** - Specialized for illegal commodity trading
- 🌌 **Multi-System** - Plan routes between Stanton and Pyro
- 📊 **Data-Driven** - Based on real player-submitted market data
- 🔄 **Auto-Refresh** - Keep data current during play sessions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/star-citizen-smuggler.git
cd star-citizen-smuggler
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run smuggler_app.py
```

4. Open your browser to `http://localhost:8501`

## 📁 Project Structure

```
star-citizen-smuggler/
│
├── smuggler_app.py          # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── LICENSE                 # MIT License
│
├── modules/                # Optional: Split code into modules
│   ├── uex_api.py         # API interface
│   ├── route_calculator.py # Route optimization
│   └── data_processor.py   # Data analysis
│
└── assets/                 # Optional: Images, icons
    └── demo_screenshot.png
```

## 🔧 Configuration

The app uses these UEX Corp API endpoints:

- `/api/commodities` - All commodity data
- `/api/commodities_prices_all` - Terminal-specific prices
- `/api/terminals` - Trading terminal information
- `/api/space_stations` - Station data including security status
- `/api/star_systems` - System information

No API key required - all endpoints are public!

## 📖 Usage Guide

### Basic Usage

1. **Select a Drug** - Use the sidebar dropdown to choose a commodity
2. **View Buy Locations** - See all terminals selling that drug with current prices
3. **View Sell Locations** - Find the best places to offload your cargo
4. **Check Optimal Route** - The app calculates the most profitable buy/sell combination
5. **Identify Safe Havens** - Look for unmonitored locations to avoid security

### Advanced Tips

- **Grim HEX** - Primary safe haven in Stanton system
- **Pyro Stations** - Everything is legal in Pyro!
- **Stock Levels** - Check "Stock" column before making long trips
- **Refresh Data** - Click refresh button for latest prices
- **Multi-Drug Runs** - Plan routes with multiple commodities

### Example Routes

**High Profit Stanton Run:**
```
Buy: Altruciatoxin at [Mining Outpost]
Sell: Grim HEX
Profit: ~800 aUEC/unit
```

**Cross-System Smuggling:**
```
Buy: Any drug in Stanton
Jump: Stanton → Pyro
Sell: Any Pyro station (all legal!)
Profit: Premium prices due to scarcity
```

## 🛠️ API Documentation

### Data Models

**Commodity Object:**
```json
{
  "id": 123,
  "name": "Altruciatoxin",
  "code": "ALTR",
  "is_illegal": 1,
  "price_buy": 3383,
  "price_sell": 4125
}
```

**Price Data Object:**
```json
{
  "commodity_name": "Altruciatoxin",
  "terminal_name": "Admin Office - Grim HEX",
  "price_buy": 3383,
  "price_sell": 4125,
  "scu_buy": 850,
  "scu_sell_stock": 1200
}
```

### Making Custom Queries

```python
import requests

# Get all commodities
commodities = requests.get("https://uexcorp.space/api/commodities").json()

# Get all prices
prices = requests.get("https://uexcorp.space/api/commodities_prices_all").json()

# Filter for illegal goods
illegal = [c for c in commodities["data"] if c["is_illegal"] == 1]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Areas for improvement:

- [ ] Add route planning for multiple stops
- [ ] Include fuel consumption calculations
- [ ] Add ship cargo capacity selector
- [ ] Create price history tracking
- [ ] Add desktop notifications for stock alerts
- [ ] Include legitimate cargo mixing suggestions
- [ ] Add risk assessment scores
- [ ] Create mobile-responsive design

### Development Setup

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Data Sources

- **[UEX Corp](https://uexcorp.space/)** - Community-driven trade data
- **[Star Citizen Wiki](https://starcitizen.tools/)** - Game information
- **[SC Trade Tools](https://sc-trade.tools/)** - Additional trade resources

## ⚠️ Disclaimer

This tool is for entertainment purposes within Star Citizen. Not affiliated with Cloud Imperium Games. All game content and materials are property of Cloud Imperium Games and/or Roberts Space Industries.

Remember: In Star Citizen, smuggling is a legitimate gameplay mechanic!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- UEX Corp for maintaining the community trade API
- Star Citizen community for price data submissions
- Cloud Imperium Games for creating this amazing universe
- All the smugglers and traders keeping the 'verse interesting

## 🐛 Known Issues

- Prices may be delayed (player-submitted data)
- Some terminals might not report stock accurately
- Pyro data is limited due to newer system
- API rate limiting may occur with frequent refreshes

## 📮 Contact

- GitHub Issues: [Report bugs or request features](https://github.com/yourusername/star-citizen-smuggler/issues)
- Star Citizen Handle: [YOUR_HANDLE]

---

*Safe flying, and may your cargo holds be full and your quantum drives be fast!* 🚀

**Version:** 1.0.0  
**Last Updated:** June 2025
