
import sqlite3
con=sqlite3.connect("library.db")
cursor=con.cursor()


class Members(object):
    pass





class Members():
    def __init__(self,name):
        self.name=name
    def addmember(self,membernamei):
        self.membername=membernamei
        cursor.execute("INSERT INTO member VALUES(?,?,?)",(None,self.membername,"Active"))
        con.commit()
    def listmember(self):
        cursor.execute("select * from member")
        for i in cursor.fetchall():
            print(i)
    def deletemember(self,memberid):

        self.memberid=memberid
        cursor.execute("select * from bookmemberrelation where status=? ",("active",))
        for i in cursor.fetchall():
            if i[1]==self.memberid:
                print("You can not delete this member")

            else:
                cursor.execute("DELETE FROM member WHERE id=?", (self.memberid,))
                con.commit()




    processtype=int(input("please choose process type 1-add new member 2-list members,3-delete member"))

    if processtype==1:

        membernamei = input("enter member name")
        addmember(Members,membernamei)
    elif processtype==2:
        listmember(Members)
    elif processtype==3:
        memberidi=int(input("write member id for delete"))
        deletemember(Members,memberidi)




con.close()









