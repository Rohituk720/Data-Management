import sys
import json
import requests
from firebase import firebase

def indextofirebase(filename):
    json_filename = filename[0]
    data = []
    count=0
    wordcount={}
    index={}
    for line in open(json_filename, 'r'):
        data.append(json.loads(line))

    for i in range(len(data)):
        for (k, v) in data[i].items():
            if k == "address":
                for word in v.lower().split():
                    if word in index:
                        index[str(word)].append(str(data[i]['account_number']))
                    else:
                        index[str(word)]=[str(data[i]['account_number'])]

    address_list={}
    dictkeys = index.keys()
    for val in enumerate(dictkeys):
        newlist = [value for key, value in index.items() if val[1] in key]
        address_list[val[1]]=[item for sublist in newlist for item in sublist]
    finallist = {}
    finallist['index'] = address_list
    with open('index.json', 'w') as fp:
        json.dump(finallist, fp,indent=3)
    

def loadindextofirebase():
    url1 = 'https://inf-551-c858e.firebaseio.com/.json'
    data=open('index.json', 'rb')
    requests.patch(url1, data=data)
    
if __name__=="__main__":
    filenamefromcommand=sys.argv[1:]
    indextofirebase(filenamefromcommand)
    loadindextofirebase()
