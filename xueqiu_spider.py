import json
import requests
from openpyxl import Workbook
session = requests.session()
headers = {
    'Host':'xueqiu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Referer':'https://xueqiu.com/hq',
    'cache-control':'no-cache',
    'X-Requested-With':'XMLHttpRequest',
    'Connection':'keep-alive',
    'Cookie':'aliyungf_tc=AQAAAEfTdDm7RgoARgy3cw4bZYOS2FVd; s=eb11mkw7c3; xq_a_token=2702d8e6d725cfa9cf118a92a6003cd58874d8b8; xq_r_token=8de4392cac1fbfc8c00cd70c2f8f9d5147787a67; u=431555641095472; Hm_lvt_1db88642e346389874251b5a1eded6e3=1555641096; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1555646003; __utma=1.1293743908.1555641096.1555641096.1555646004.2; __utmc=1; __utmz=1.1555641096.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); device_id=4d7df643b8d68c85d4b2a707eac2f180; __utmb=1.1.10.1555646004; __utmt=1'
}

count = 0
wd = Workbook()
ws = wd.active
ws.append(['股票代码', '股票名称', '当前价', '涨跌幅', '市值', '市盈率 '])
for page in range(1,5):
    url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page='+ str(page) +'&size=30&order=desc&orderby=chg&order_by=chg&market=US&type=us'
    response = session.get(url=url,headers=headers)
    js = json.loads(response.text)
    for company_dict in js["data"]["list"]:
        if count<100:
            symbol = company_dict["symbol"]
            name = company_dict["name"]
            current = company_dict["current"]
            percent = company_dict["percent"]
            market_capital = company_dict["market_capital"]
            pe_ttm = company_dict["pe_ttm"]
            ws.append([symbol,name,current,percent,str(market_capital),str(pe_ttm) +"%"])
        wd.save("美国股市涨幅前100名.xlsx")
        count += 1
