import requests

url="http://jsonplaceholder.typicode.com/users"


def fetchAPI():
    try:
        response=requests.get(url)
        print(response.status_code)

        if response.status_code==200:
            #print(response.text)
            print("---------------------------")
            print(type(response.text))


            data=response.json()

            user=data[0]
            print(user)
            print("-------------")
            print("Name:",user["name"])
            print("-------------")
            print("Email:",user["email"])

            print(user["address"]["zipcode"])
            print("-------------")
            print(user["address"]["geo"]["lat"])
            print("-------------")
        else:
            print("Api error",response.status_code)

    except Exception as e:
        print("something went wrong") #sever down,no internet connection,etc
        print("Error",e)



fetchAPI