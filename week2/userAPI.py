import requests

url="https://randomuser.me/api/?results=20&nat=in"
response=requests.get(url)
print(response.status_code)

data=response.json()
# print(data)

listofuser=data["results"]
#print(listofuser)
#print(listofuser[0])
# print(listofuser[0]["name"])
name=listofuser[0]["name"]["title"] +" " + listofuser[0]["name"]["first"] + " " +listofuser[0]["name"]["last"] + " " 


for user in listofuser:
    name=user["name"]["title"] +" " + user["name"]["first"] + " " +user["name"]["last"] + " " 
    print(name)