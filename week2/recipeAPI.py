import requests

url="https://dummyjson.com/recipes"
response=requests.get(url)
print(response.status_code)

data=response.json()
# print(data)

listofrecipes=data["recipes"]

for rec in listofrecipes:
    recname=rec["name"]
    print(recname)