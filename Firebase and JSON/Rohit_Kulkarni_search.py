import json
import requests
import sys
from firebase import firebase

def search(v, data):
    address_list=[]
    address_list = v.lower().split(" ")
    result_list=[]
    for address in address_list:
        if address in data.keys():
            for i in data.get(address):
                if i not in result_list:
                    result_list.append(i)
    print(result_list)


if __name__=="__main__":
     address=sys.argv[1]
     url = 'https://inf-551-c858e.firebaseio.com/index.json'
     response = requests.get(url)
     data = response.json()
     dict=eval(json.dumps(data))
     search(address,dict)
