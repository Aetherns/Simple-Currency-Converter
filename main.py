def myconverter(a, b, value): # a - currency to be converted, b - converted currency, input -input value(USD, EUR, 2.05)
    import json, urllib.request
    a, b = a.upper(), b.upper()
    base_url = "http://data.fixer.io/api/latest?access_key="
    key ="ee4fda7b5b36f34e068f26b877ae795c"
    symbols = "&symbols=" + a + "," + b

    FullLenghtURL = base_url + key + symbols
    with urllib.request.urlopen(FullLenghtURL) as url:
        data = json.loads(url.read().decode())

    a = data["rates"][a]
    b = data["rates"][b]
    return round(value * (b/a), 2)      #HUF to USD

def main():
    a = input("code of starting currency (EUR, USD, RUB, etc.): ")
    b = input("code of currency you would like to convert into: ")
    m_input = int(input("How much would you like to convert? "))
    print(m_input, a, "==", myconverter(a, b, m_input), b)


if __name__ == '__main__':
    main()