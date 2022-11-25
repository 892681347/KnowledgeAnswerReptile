import requests
import re
from bs4 import BeautifulSoup
import http.client


# https://ks.wjx.top/vm/hECGdIM.aspx

def remove_head(s):
    if re.search(r'^\d+\. ', s) is None:
        return s
    return s[re.search(r'^\d+\. ', s).end():]


conn = http.client.HTTPSConnection("ks.wjx.top")
conn.request("GET", "/vm/hECGdIM.aspx")
req = conn.getresponse()
data = req.read()

soup = BeautifulSoup(data.decode("utf-8"), features="html.parser")
company_items = soup.find_all("div", class_="field ui-field-contain")
print(len(company_items))
for company_item in company_items:
    dd = company_item.text.strip()
    print(remove_head(dd))
