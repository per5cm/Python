import requests
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Command-line argument is not a number")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Missing command-line argument")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()

        data = response.json()
        price_usd = data ["bpi"]["USD"]["rate_float"]

        total_cost = bitcoin * price_usd
        print(f"${total_cost:,.4f}")
    except requests.RequestException:
        sys.exit("Request exceptions")

if __name__ == "__main__":
    main()
