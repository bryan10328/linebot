import pymysql
import datetime
Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#資料庫連線設定
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='120906394', db='line', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法
aa='債瑞直'
bb='湊找'
abc = '測試'
# abc=abc.encode('utf-8')
# aa=aa.encode("utf-8") 
# bb=bb.encode("utf-8") 
# aa='123'
# bb='45678'
#sql = "INSERT INTO test(a01, a02, a03) VALUES ('"+ aa.decode("utf-8")+"','"+ bb.decode("utf-8")+"','"+ str(Now) +"')"
sql = "INSERT INTO test(a01, a02, a03) VALUES ('"+ aa +"','"+ bb+"','"+ str(Now) +"')"
#執行語法

try:
  cursor.execute(sql)
  #提交修改
  db.commit()
  print('success')
except Exception as e:
  #發生錯誤時停止執行SQL
  db.rollback()
  print('error')

#關閉連線
db.close()