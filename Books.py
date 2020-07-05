
import sqlite3
con=sqlite3.connect("library.db")
cursor=con.cursor()


class Books(object):
    pass


class Books():
    def __init__(self,name,quantity,writer):

        self.name=name
        self.quantity=quantity
        self.writer=writer

    def addbook(self, namei, quantityi, writeri):
        self.name = namei
        self.quantity = quantityi
        self.writer = writeri
        cursor.execute("INSERT INTO books VALUES (?,?,?,?,?)", (None, self.name, self.quantity, self.writer,"Available"))
        con.commit()

    def listbooks(self,whichbook):
        cursor.execute("SELECT * FROM books")
        for i in cursor.fetchall():
            if whichbook!="*":
                if i[1]==whichbook:
                    print(" Book Id:",i[0],"\n","Book Name:",i[1],"\n","Book quantity:",i[2],"\n","Book writer:",i[3])
                else:
                    print("sorry  we couldnt find any books in database")
                    break
            elif whichbook=="*":
                print(i)
 ############ the book  is giving to member
    def givebook(self,memberid,bookid):
        self.bookid=bookid
        self.memberid=memberid
        booksquantity=[]
        cursor.execute("SELECT * FROM books where id=?",(self.bookid,))
        for i in cursor.fetchall():
            booksquantity.append(i[2])
        if booksquantity[0] == 1:

            cursor.execute("INSERT INTO bookmemberrelation VALUES(?,?,?,?)",(None,self.memberid,self.bookid,"active"))
            cursor.execute("UPDATE books set quantity=? where id=?", (booksquantity[0] - 1, self.bookid))

            cursor.execute("UPDATE books SET status=?  where id=?",("Not available",self.bookid))
        elif booksquantity[0]>1:
            cursor.execute("INSERT INTO bookmemberrelation VALUES(?,?,?,?)", (None, self.memberid, self.bookid,"active"))
            cursor.execute("UPDATE books set quantity=? where id=?",(booksquantity[0]-1,self.bookid))
        elif booksquantity[0]==0:
            print("its not available ")
        con.commit()
###book is getting from member
    def getbook(self,memberid,bookid):
        self.memberid=memberid
        self.bookid=bookid
        bookquantity=[]

        cursor.execute("select * from books where id=?",(self.bookid,))
        for i in cursor.fetchall():
            bookquantity.append(i[2])


        cursor.execute("UPDATE bookmemberrelation set status=? where memberid=? and bookdid=? ",("passive",self.memberid,self.bookid))
        cursor.execute("UPDATE books set quantity=? where id=?",((bookquantity[0]+1),self.bookid))
        cursor.execute("UPDATE books set status=? where id=?",("Available",self.bookid))
        con.commit()
    processtype = int(input("please choose process type 1-Add Book 2-List Books 3-Give Books 4-Get Book\n"))
    if processtype == 1:
        namei = input("Enter Book name\n")
        quantityi = int(input("enter book quantity\n"))
        writeri = input("enter writer book\n")
        registeranswer = input("if you want to register please  write Y\n")
        if registeranswer == "Y":
            addbook(Books,namei,quantityi,writeri)
    elif processtype==2:

        whichbook=input(" what is the book for looking if you want to list allbooks please write * \n")
        listbooks(Books,whichbook)
    elif processtype==3:
        memberid=input("enter memberid")
        bookid=input("enter bookid")
        givebook(Books,memberid,bookid)
    elif processtype==4:
        memberid = input("enter memberid")
        bookid = input("enter bookid")
        getbook(Books,memberid,bookid)




con.close()







