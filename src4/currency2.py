import requests


def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=ec1dd77b11df78941cae4f163fac10ea",
                       params={"symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")


if __name__ == "__main__":
    main()
