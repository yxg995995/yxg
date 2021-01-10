import requests
import json
from DataBase import *
def getdaydata():#爬取股票每天的价格并插入到数据库保存
    durl='''http://quotes.money.163.com/service/chddata.html?code=1000001&start=20200106&end=20210106&
            fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'''
    r=requests.get(durl)
    data=r.text.splitlines()
    n=len(data)
    for i in range(n-1):
        insertdayTB(data[-i-1].split(',')[0],data[-i-1].split(',')[2],data[-i-1].split(',')[6],
                    data[-i-1].split(',')[3],data[-i-1].split(',')[5],data[-i-1].split(',')[4])
#爬取某只股票的一天里面9：30到15：00每分钟的股票价格并插入数据库保存
#这个只能爬取当天9:30到这个时间段的数据,之前的数据请保存好
def getmindata():
    url='http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&id=0000012&type=r&iscr=false'
    r=requests.get(url)
    l=r.text.strip('(')
    l1=l.strip(')')
    data=json.loads(l1)
    for i in data['data']:
        insertminTB(i.split(',')[0], i.split(',')[1])

if __name__=='__main__':
    getmindata()