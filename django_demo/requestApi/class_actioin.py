# 班级
import pymysql
from django.shortcuts import render, redirect
import random
def classes(request):
    # 连接数据库
    conn = pymysql.connect(host="39.106.29.92", user="root", password="123456", database="test", port=int(3306), charset="utf8")
    # 创建一个游标对象 可以利用这个对象进行数据库的操作
    try:
        opt_sql = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql: str = 'select id, title from tb_class'
        opt_sql.execute(sql)
        class_list = opt_sql.fetchall()
        print('连接数据库成功啦.......')
        return render(request, 'class/class_list.html', {'class_list': class_list})
    except Exception as msg:
        print(msg)
    finally:
        opt_sql.close()
        conn.close()
        print('关闭连接池===结束')
    pass

def add_class(request):

    if request.method == 'GET':
        return render(request, 'class/add_class.html')
    else:
        class_id = random.randint(1, 100)
        #新增员工请求
        title = request.POST.get('title')
        # 连接数据库
        conn = pymysql.connect(host="39.106.29.92", user="root", password="123456", database="test", port=int(3306),
                               charset="utf8")
        # 创建一个游标对象 可以利用这个对象进行数据库的操作

        try:
            opt_sql = conn.cursor(cursor=pymysql.cursors.DictCursor)
            sql: str = 'insert into tb_class(id, title) values (%s, %s)'
            params = (class_id, title)
            opt_sql.execute(sql, params)
            conn.commit()
            print('数据添加成功啦.......')
            return redirect('/class/')
        except Exception as msg:
            print(msg)
            return render(request, 'class/add_class.html')
        finally:
            opt_sql.close()
            conn.close()
    pass