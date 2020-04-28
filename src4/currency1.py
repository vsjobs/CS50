import requests


def main():
    #  res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    res = requests.get(
        "http://data.fixer.io/api/latest?access_key=ec1dd77b11df78941cae4f163fac10ea&symbols=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["USD"]
    print(f"1 EUR is equal to {rate} USD")


if __name__ == "__main__":
    main()
