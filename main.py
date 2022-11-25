import re
import os
from bs4 import BeautifulSoup
import http.client  # https://ks.wjx.top/vm/hECGdIM.aspx

dic = {}


def remove_head(s):
    if re.search(r'^\d+\. ', s) is None:
        return s
    return s[re.search(r'^\d+\. ', s).end():]


def run_once():
    new_item = 0
    conn = http.client.HTTPSConnection("ks.wjx.top")
    conn.request("GET", "/vm/hECGdIM.aspx")
    req = conn.getresponse()
    data = req.read()
    soup = BeautifulSoup(data.decode("utf-8"), features="html.parser")
    items = soup.find_all("div", class_="field ui-field-contain")
    for item in items:
        text = item.text.strip()
        text = remove_head(text)
        if text not in dic:
            dic[text] = True
            new_item += 1
    print(new_item, end='  ')
    return new_item == 0


def run():
    no_new_time = 0
    run_time = 0
    while no_new_time <= 100:
        run_time += 1
        if run_once():
            no_new_time += 1
        else:
            no_new_time = 0
    print()
    print("runtime: ", run_time)


def write_to_file():
    name = r'.\TIKU\tiku'
    file_name = name + '.txt'
    index = 0
    while os.path.exists(file_name):
        index += 1
        file_name = name + '(' + str(index) + ')' + '.txt'
    f = open(file_name, "w", encoding='utf-8')
    keys = list(dic.keys())
    keys.sort()
    for key in keys:
        f.write(key+"\n")
    f.close()
    print('导出成功')


if __name__ == "__main__":
    run()
    write_to_file()
