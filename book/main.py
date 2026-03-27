from mannger_book import * 
conn=mangebooks("localhost",3306,"root","123456",True)
while True:
    try:
        print("-"*23)
        print("欢迎来到图书管理系统")
        print("请选择你要做的事：")
        chiose=int(input("1.查询书籍\n2.添加书籍\n3.修改图书\n4.删除图书\n5.显示所有图书\n请输入:"))
        print("-"*23)
    except Exception:
        print("输入格式错误")
    if chiose==1:
        keyword=input("请输入你要查询的关键字：")
        conn.search_books_by_title(keyword=keyword)
    elif chiose==2:
        book_id=int(input("请输入你要增添的id:"))
        name=input("请输入书名:")
        author=input("请输入作者：")
        piece=eval(input("请输入价格"))
        stock=eval(input("请输入存入数量："))
        conn.add_book(id=book_id,name=name,author=author,piece=piece,stock=stock)
    elif chiose==3:
        print("-"*23)
        num=int(input("请选择你要修改的部分\n1.书名\n2.作者\n3.价格\n4.库存\n请输入:"))
        if num==1:
            value=input("请输入修改后的值：")
            conn.update_book(num=num,value=value)
        elif num==2:
            value=input("请输入修改后的值：")
            conn.update_book(num=num,value=value)
        elif num==3:
            value=int(input("请输入修改后的值："))
            conn.update_book(num=num,value=value)
        elif num==4:
            value=int(input("请输入修改后的值："))
            conn.update_book(num=num,value=value)
    elif chiose==4:
        author=input("请输入你要删除的作者名字")
        name=input("请输入你要删除对应作者的书名：")
        conn.delete_book(name=name,author=author)
    elif chiose==5:
        conn.get_all_books()
