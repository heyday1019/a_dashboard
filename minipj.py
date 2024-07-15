import datetime
import pandas as pd
import requests
import xml.etree.ElementTree as ET

def get_items(response):
    root = ET.fromstring(response.content)
    item_list = []
    for child in root.find('body').find('items'):
        elements = child.findall('*')
        data = {}
        for element in elements:
            tag = element.tag.strip()
            text = element.text.strip()
            # print tag, text
            data[tag] = text
        item_list.append(data)
    return item_list

url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
service_key = '6nqieI8hHurV2IeQWuaHtEXRTSPOxlztaW2SM1ETKtL2oMp30hQNCJ%2B1Xx0HEvq928VpwKyVjcNh7afDkO5esg%3D%3D'
contract_date = '201512'
location_code = '11110'

payload = "LAWD_CD=" + location_code + "&" + \
          "DEAL_YMD=" + contract_date + "&" + \
          "serviceKey=" + service_key + "&"

res = requests.get(url + payload)

items_list = get_items(res)
df = pd.DataFrame(items_list)
print(df)