from fetcher import get_exchange_rates, get_brent_crude, get_lagos_weather
from formatter import build_email
from sender import send_email

SUBSCRIBERS = [
    {"name": "Eddy", "email": "ediomoetesin40@gmail.com"},
    {"name": "Raji", "email":"Opeolurajisodiq@gmail.com"},
    {"name": "Nelly", "email":"nellytracy90@gmail.com"},
    {"name": "Meb", "email":"al_meb.jr@icloud.com"},
    {"name": "Chilet", "email":"Okekechiletaram@gmail.com"},
    {"name": "Aniesua", "email":"aniesuaessiettjnr@gmail.com"},
    {"name": "Jones", "email":"Jjoe9931@gmail.com"},
    {"name": "Idongesit", "email":"lelouch4britania@gmail.com"},

]

def main():
    print("Fetching data...")
    rates = get_exchange_rates()
    crude = get_brent_crude()
    weather = get_lagos_weather()
    print("Data fetched.")

    for subscriber in SUBSCRIBERS:
        html = build_email(subscriber["name"], rates, crude, weather)
        send_email(subscriber["name"], subscriber["email"], html)

    print("All emails sent.")

if __name__ == "__main__":
    main()