import sys
import json
import xml.etree.ElementTree as xml

json_file = sys.argv[1]
xml_File = sys.argv[2]

data=[]
for line in open(json_file, 'r'):
        data.append(json.loads(line))

dict=eval(json.dumps(data))
xmlData = open(xml_File, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<accounts>' + "\n")

for i in range(len(dict)):
    for (k, v) in sorted(dict[i].items()):
        if k != "index":
            tags=k
            if tags == "account_number":
                xmlData.write('  <account number="' +  str(v) + '">' + "\n")
            if tags == "balance":
                xmlData.write('    <balance>' +  str(v) + '</balance>' + "\n")
            if tags == "firstname":
                xmlData.write('    <firstname>' +  str(v) + '</firstname>' + "\n")
            if tags == "lastname":
                xmlData.write('    <lastname>' +  str(v) + '</lastname>' + "\n")
            if tags == "age":
                xmlData.write('    <age>' +  str(v) + '</age>' + "\n")
            if tags == "gender":
                xmlData.write('    <gender>' +  str(v) + '</gender>' + "\n")
            if tags == "address":
                xmlData.write('    <address>' +  str(v) + '</address>' + "\n")
            if tags == "employer":
                xmlData.write('    <employer>' +  str(v) + '</employer>' + "\n")
            if tags == "email":
                xmlData.write('    <email>' +  str(v) + '</email>' + "\n")
            if tags == "city":
                xmlData.write('    <city>' +  str(v) + '</city>' + "\n")
            if tags == "state":
                xmlData.write('    <state>' +  str(v) + '</state>' + "\n")
                xmlData.write('  </account>' + "\n")
            
            
xmlData.write('</accounts>' + "\n")
xmlData.close()
