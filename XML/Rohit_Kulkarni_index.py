import sys
import xml.etree.ElementTree as e

read_file = sys.argv[1]
create_File = sys.argv[2]

xml_data = e.parse(read_file)
root_element=xml_data.getroot()
i=0
words={}

for c in root_element:
    for v in root_element[i][0].text.split():
        if v in words:
            words[str(v)].append(str(c.get('number')))
        else:
            words[str(v)]=[str(c.get('number'))]
    i+=1

        
xmlData = open(create_File, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<index>' + "\n")
for k,v in words.iteritems():
    xmlData.write('  <entry>' + "\n")
    xmlData.write('    <keyword>' +  str(k.lower()) + '</keyword>' + "\n")
    xmlData.write('    <accounts>' +  "\n")
    for w in v:
        xmlData.write('        <number>' +  str(w.lower()) + '</number>' + "\n")
    xmlData.write('    </accounts>' + "\n")
    xmlData.write('  </entry>' + "\n") 

xmlData.write('</index>' + "\n") 



