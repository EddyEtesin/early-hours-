import requests
import yfinance as yf

def get_exchange_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()
    
    usd_to_ngn = data["rates"]["NGN"]
    
    rates = {
        "USD": round(usd_to_ngn,2),
        "EUR": round(data["rates"]["NGN"] / data["rates"]["EUR"], 2),
        "GBP": round(data["rates"]["NGN"] / data["rates"]["GBP"], 2),
        "CNY": round(data["rates"]["NGN"] / data["rates"]["CNY"], 2),
    }
    
    return rates

def get_brent_crude():
    ticker = yf.Ticker("BZ=F")
    data = ticker.history(period="2d")
    
    latest = round(data["Close"].iloc[-1], 2)
    previous = round(data["Close"].iloc[-2], 2)
    change = round(((latest - previous) / previous) * 100, 2)
    
    return {
    "price": float(round(data["Close"].iloc[-1], 2)),
    "change": float(round(((latest - previous) / previous) * 100, 2))
    }

def get_lagos_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 6.5244,
        "longitude": 3.3792,
        "daily": "temperature_2m_max,weathercode",
        "timezone": "Africa/Lagos",
        "forecast_days": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    temp = data["daily"]["temperature_2m_max"][0]
    code = data["daily"]["weathercode"][0]

    return {
        "temp": temp,
        "code": code
    }

