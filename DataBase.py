import sqlite3
def createDB():
    db=sqlite3.connect('D:/gupiao.db')#数据库文件路径，如果有就连接，如果没有就创建
    return db
    
def createdayTB():#创建股票每天的数据表
    db=createDB()
    #使用游标
    cur=db.cursor()
    #sql语句
    qrl='''create table daygp (day datetime,name varchar(20),openprice numeric(6,2),
    endprice numeric(6,2),minprice numeric(6,2),maxprice numeric(6.2))'''
    cur.execute(qrl)
    #释放游标
    db.commit()
    #关闭数据库
    db.close()

def createminTB():#创建股票每分钟的数据表
    db=createDB()
    cur=db.cursor()
    #sql语句
    qrl='''create table mingp (minute datetime,price numeric(6,2))'''
    cur.execute(qrl)
    db.commit()
    db.close()

def insertdayTB(day,name,openprice,endprice,minprice,maxprice):#插入每天的股票价格
    db=createDB()
    cur=db.cursor()
    qrl='''insert into daygp values (?,?,?,?,?,?)'''
    cur.execute(qrl,(day,name,openprice,endprice,minprice,maxprice))
    db.commit()
    db.close()

def insertminTB(minute,price):#插入每分钟的股票价格
    db=createDB()
    cur=db.cursor()
    qrl='''insert into mingp values (?,?)'''
    cur.execute(qrl,(minute,price))
    db.commit()
    db.close()

def getdaydata():#获取每天的股价
    db=createDB()
    cur=db.cursor()
    qrl='''select day,openprice,endprice,minprice,maxprice from daygp'''
    cur.execute(qrl)
    result=cur.fetchall()
    db.commit()
    db.close()
    return result

def getmindata():#获取每分钟的股价
    db=createDB()
    cur=db.cursor()
    qrl='''select * from mingp'''
    cur.execute(qrl)
    result=cur.fetchall()
    db.commit()
    db.close()
    return result

def main():
    #如果要更新，请先删除daygp里面数据，然后更改日期
    createdayTB() 
    createminTB()

if __name__=='__main__':
    main()