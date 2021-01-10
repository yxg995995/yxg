from DataBase import *
from pyecharts import options as opts
from pyecharts.charts import Kline,Line #pycharts带有画k线的函数
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
def fenriK():
    daydata=getdaydata()
    
    date=[]#装日期
    dataK=[]#装日的开盘价，收盘价，最高价，最低价
    for i in daydata:
        date.append(i[0])
        dataK.append(i[1:])
    kline=(
        Kline()
            .add_xaxis(date)
           .add_yaxis("K线", dataK)
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(is_scale=True),
                 xaxis_opts=opts.AxisOpts(is_scale=True),
                 title_opts=opts.TitleOpts(title="分日K线图"),
             )
         )
    kline.render("分日K线图.html")

def fenshiK():
    result=getmindata()
    date=[]
    dataK2=[]
    for i in result:
        date.append(i[0])
        dataK2.append(i[1])
    Max=0
    Min=0
    end=0
    Open=0
    datak2=[]
    for i in range(int(len(dataK2)/60)):#计算出每个小时的开盘价，收盘价，最高价，最低价
        d=[]
        Open=dataK2[i*60]
        Max=max(dataK2[i*60:60*(i+1)])
        Min=min(dataK2[i*60:60*(i+1)])
        end=dataK2[60*(i+1)]
        d.append(Open)
        d.append(end)
        d.append(Min)
        d.append(Max)
        datak2.append(d)
    n=len(date)/241
    date1=[]
    for j in range(len(date)):#生成每天的小时时间
        year=date[j].split(' ')[0]
        if j%240==0 and j!=0:
            date1.append(year+" 10:30")
            date1.append(year+" 11:30/13:00")
            date1.append(year+" 14:00")
            date1.append(year+" 15:00")
            year=date[j+1].split(' ')[0]
    kline1=(
            Kline()
                .add_xaxis(date1)
               .add_yaxis("K线", datak2)
                .set_global_opts(
                    yaxis_opts=opts.AxisOpts(is_scale=True),
                     xaxis_opts=opts.AxisOpts(is_scale=True),
                     title_opts=opts.TitleOpts(title="分时K线图"),
                 )
             )
    kline1.render('分时K线图.html')

def KDJ():
    
    result=getdaydata()
    x=[]
    d=[]
    for i in range(len(result)):
        x.append(result[i][0])
        d.append(result[i][1:])
    n=len(d)
    K1=50
    D1=50
    K=[]
    D=[]
    J=[]
    j=0
    d1=[]
    for i in range(int(n/4)):#以4日为一个周期
        d1.append(d[i*4:(i+1)*4])
    for i in d1:#计算rsv,K,D,J
        Max=[]
        Min=[]
        end=[]
        for j in i:
            Max.append(max(j))
            Min.append(min(j))
            end.append(j[1])
        for j in range(4):
            rsv=100*(end[-1]-min(Min))/(max(Max)-min(Min))
            K1=(2/3)*K1+rsv/3
            D1=(2/3)*D1+K1/3
            j=3*K1-2*D1
            K.append(K1)
            D.append(D1)
            J.append(j)
        K1=50
        D1=50
    #画KDJ图
    plt.figure(figsize=(10,5))
    xticks=range(len(K))
    plt.plot(x,K,label='K线')
    plt.plot(x,D,label='D线')
    plt.plot(x,J,label='J线')
    plt.legend()
    plt.show()

if __name__=='__main__':
    fenriK()
    fenshiK()
    KDJ()
    