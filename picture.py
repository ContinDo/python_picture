import requests
import re
import json

content = requests.get('https://huaban.com/discovery/beauty/').text
startIndex = re.search('\[\"pins\"\] \=\ ', content).span()[1]
endIndex = re.search('}}];',content[startIndex:]).span()[1] + startIndex - 1
# print(startIndex,endIndex)

jsonStr = content[startIndex:endIndex]
jsonObj = json.loads(jsonStr)

# print(len(jsonObj))
for item in jsonObj:
    url = 'http://hbimg.huabanimg.com/' + item['file']['key']
    # print(url)
    image = requests.get(url).content
    with open(item['file']['key'] + '.jpg','wb') as file:
        file.write(image)
# 爬取20个图片




