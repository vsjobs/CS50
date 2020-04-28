import requests

#    ec1dd77b11df78941cae4f163fac10ea

#  http://data.fixer.io/api/latest?access_key=ec1dd77b11df78941cae4f163fac10ea&symbols=GBP


def main():
    #  res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    res = requests.get(
        "http://data.fixer.io/api/latest?access_key=ec1dd77b11df78941cae4f163fac10ea&symbols=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)


if __name__ == "__main__":
    main()
