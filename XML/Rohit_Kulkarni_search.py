import sys
import xml.etree.ElementTree as e

file_name=sys.argv[1]
v=sys.argv[2]
xml_data = e.parse(file_name)
root_element=xml_data.getroot()
address_list = v.lower().split(" ")
result=[]

for c in root_element:
    for address in address_list:
        if c.find('keyword').text == address:
            for num in c.findall('accounts/number'):
                result.append(num.text)

print(result)
