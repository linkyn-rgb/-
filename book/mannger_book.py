from pymysql import connect
class mangebooks:
    def __init__(self,host,port,user,password,autocommit):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.autocommit=autocommit
    def connect(self):
            self.connection=connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            autocommit=self.autocommit
        )
    def add_book(self,id,name,author,piece,stock):
        self.connect()
        self.cursor=self.connection.cursor()
        sql1=f"use library_stream;"
        sql2=f"insert into books(id,name,author,piece,stock) values(%s,%s,%s,%s,%s);"
        self.cursor.execute(sql1)
        try:
            self.cursor.execute(sql2,(id,name,author,piece,stock))
        except Exception:
            print("输入格式有误，请输入正确的格式")
        finally:
            self.connect_close()
    def get_all_books(self):
        self.connect()
        self.cursor=self.connection.cursor() 
        sql1=f"use library_stream;"
        sql2=f"select * from books;"
        self.cursor.execute(sql1)
        self.cursor.execute(sql2)
        result=self.cursor.fetchall()
        print(f"现在共有图书如下{result}")
        self.connect_close()
    def delete_book(self,name,author):
        self.connect()
        self.cursor=self.connection.cursor()
        sql1=f"use library_stream;"
        sql2=f"delete from books where name='{name}' and author='{author};"
        self.cursor.execute(sql1)
        try:
            self.cursor.execute(sql2,(name,author))
        except Exception:
            print("输入格式错误，请输入正确的格式")
        finally:
            self.connect_close()
    def search_books_by_title(self,keyword):
        self.connect()
        self.cursor=self.connection.cursor()
        sql=f"select {keyword} from books;"
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            print(f"已按照{keyword}结果查询，结果为：{result}")
        except Exception:
            print(f"格式错误。请输入正确格式")
        finally:
            self.connect_close()
    def update_book(self,num,value):
        num=range(1,5)
        self.connect()
        self.cursor=self.connection.cursor()
        try:
            if num==1:
                sql1=f"update books set name={value};"
                self.cursor.execute(sql1)
            elif num==2:
                sql2=f"update books set author={value};"
                self.cursor.execute(sql2)
            elif num==3:
                sql3=f"update books set piece={value};"
                self.cursor.execute(sql3)
            else:
                sql4=f"update books set stock={value};"
                self.cursor.execute(sql4)
        except Exception:
            print(f"{value}格式错误")
        finally:
            self.connect_close()
    def connect_close(self):
        if self.connection:
            self.connection.close()
if __name__=='__main__':
    book=mangebooks(host="localhost",port=3306,user="root",password="123456",autocommit=True)
    book.connect()
    book.delete_book('lwh','sdasdsaddasdasdasdasd')
    