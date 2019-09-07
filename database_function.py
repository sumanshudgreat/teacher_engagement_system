import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='tes'
)

con = mydb.cursor()

def convert_tuple_to_list_db(x):
    y=[]
    for i in x:
        y.append(i[0])
    return y

def convert_tuple_to_list_size_variable_db(x,y):
    teacher=[]
    for i in range(len(x)):
        k=''
        for j in range(y):
            k=k+str(x[i][j]).upper()
            if j==0:
                k=k.rjust(3,'0')
                k=k.ljust(5,' ')
        teacher.append(k)
    return teacher

def convert_tuple(x,y):
    t=[]
    for i in x:
        k='    '.join(i)
        t.append(k)

    return t

def add_admin_db(username,password):
    username=username.lower()
    sql_stuff = "select exists (select username from admin where username = %s)"
    con.execute(sql_stuff,(username,))
    if not(con.fetchone()[0]):
        sql_stuff = "insert into admin values(%s,%s)"
        con.execute(sql_stuff,(username,password,))
        mydb.commit()
        return 1
    else:
        return 0
    
def get_admin_db():
    sql_stuff = "select username from admin where username!='admin'"
    con.execute(sql_stuff)
    x = con.fetchall()
    x = convert_tuple_to_list_db(x)
    return x

def remove_admin_db(username):
    sql_stuff = "delete from admin where username=%s"
    con.execute(sql_stuff,(username,))
    mydb.commit()

def pass_change_db(password,username):
    sql_stuff = "update admin set password=%s where username=%s"
    con.execute(sql_stuff,(password,username,))
    mydb.commit()


def login_db(username,password):
    sql_stuff="select exists ( select username from admin where username=%s )"
    con.execute(sql_stuff,(username,))
    if con.fetchone()[0]:
        con.execute("select password from admin where username=%s",(username,))
        if password==con.fetchone()[0]:
            return 1
        else:
            return 2
    return 0


    ######################################################

def get_teacher_db():
    sql_stuff="select Tid,Tname from teacher order by Tname"
    con.execute(sql_stuff)
    x=con.fetchall()
    x=convert_tuple_to_list_size_variable_db(x,2)
    return x

def add_teacher_db(Tid,Tname,Desig,Dept):
    Tid=Tid.upper()
    Tname=Tname.upper()
    sql_stuff="select exists(select Tid from teacher where Tid=%s)"
    con.execute(sql_stuff,(Tid,))
    if con.fetchone()[0]==0:
        sql_stuff="select exists(select Tname from teacher where Tname=%s)"
        con.execute(sql_stuff,(Tname,))
        if con.fetchone()[0]==0:
            sql_stuff="insert into teacher values(%s,%s,%s,%s)"
            con.execute(sql_stuff,(Tid,Tname,Desig,Dept,))
            mydb.commit()
            return 1
        else:
            return 2
    else:
        return 0

def remove_teacher_db(Tid):
    sql_stuff="delete from teacher where Tid=%s"
    con.execute(sql_stuff,(Tid,))
    mydb.commit()

def add_subject_db(Sid,Sname):
    Sid=Sid.upper()
    Sname=Sname.upper()
    sql_stuff="select exists(select Sid from subject where Sid=%s)"
    con.execute(sql_stuff,(Sid,))
    if con.fetchone()[0]==0:
        sql_stuff="select exists(select Sname from subject where Sname=%s)"
        con.execute(sql_stuff,(Sname,))
        if con.fetchone()[0]==0:
            sql_stuff="insert into subject values(%s,%s)"
            con.execute(sql_stuff,(Sid,Sname))
            mydb.commit()
            return 1
        return 2
    return 0

def get_subject_db():
    sql_stuff="select Sid,Sname from subject"
    con.execute(sql_stuff)
    x=con.fetchall()
    x=convert_tuple(x,2)
    return x

def remove_subject_db(x):
    sql_stuff="delete from subject where Sid=%s"
    con.execute(sql_stuff,(x,))
    mydb.commit()

def add_time_tabe_db(l):
    tut=',('+l[0]+'T'
    sql_stuff="insert into time_table values("+l[0]
    for i in range(1,169,28):
        for j in range(7):
            sql_stuff=sql_stuff+","+l[i+j]+","+l[i+7+j]
            tut+=","+l[i+j+14]+","+l[i+21+j]
    sql_stuff+=")"
    sql_stuff+=tut+")"
    con.execute(sql_stuff)
    mydb.commit()