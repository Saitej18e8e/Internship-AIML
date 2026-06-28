import requests

url = "https://countriesnow.space/api/v0.1/countries"

try:
    response = requests.get(url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:

        print("----------------------------")
        print(type(response.text))

        data = response.json()

        country = data["data"][0]   

        print("----------------------------")
        print(country)

        print("----------------------------")
        print("Country:", country["country"])

        print("----------------------------")
        print("First City:", country["cities"][0])

        print("----------------------------")
        print("Total Cities:", len(country["cities"]))

    else:
        print("API Error:", response.status_code)

except Exception as e:
    print("Something went wrong")
    print("Error:", e)