import wx
import MySQLdb as mdb
import datetime
con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu') 
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Logins(Id VARCHAR(25), password VARCHAR(25),username varchar(25))")
    cur.execute("CREATE TABLE IF NOT EXISTS BOOKINGSS(id int NOT NULL AUTO_INCREMENT ,Usid varchar(20),Bid int,RoomType varchar(50),nofrooms int,cost int,froms date,too date,PRIMARY KEY (id))")
con.commit()
con.close()
if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub
 
 
######################################################################################################
x="hi"
y=0
f=11
t=11
c=0
Roomte="hello"
uid=""
#######################################################################################################
class RegisterDialog(wx.Dialog):
    """docstring for """
    def __init__(self):
        wx.Dialog.__init__(self,None,title="REGISTER")
        usersizer_r=wx.BoxSizer(wx.HORIZONTAL)
        self.userre=wx.TextCtrl(self)
        user=wx.StaticText(self,label="YOUR NAME: ")
        usersizer_r.Add(user,0,wx.ALL | wx.CENTER ,5)
        usersizer_r.Add(self.userre,10,wx.ALL,5)

        usersizer_2=wx.BoxSizer(wx.HORIZONTAL)
        self.userde=wx.TextCtrl(self)
        userd=wx.StaticText(self,label="USERNAME:   ")
        usersizer_2.Add(userd,0,wx.ALL | wx.CENTER,5)
        usersizer_2.Add(self.userde,0,wx.ALL,5)

        p_sizer=wx.BoxSizer(wx.HORIZONTAL)
        p_lbl = wx.StaticText(self, label="Password:      ")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        p_sizer.Add(self.password, 0, wx.ALL, 5)
       

        btn1=wx.Button(self,label="REGISTER")
        btn1.Bind(wx.EVT_BUTTON,self.regist)

        main_sizer=wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(usersizer_r,0,wx.ALL,5)
        main_sizer.Add(usersizer_2,0,wx.ALL,5)
        main_sizer.Add(p_sizer,0,wx.ALL,5)
        main_sizer.Add(btn1,0,wx.ALL | wx.CENTER,5)
        self.SetSizer(main_sizer)


    def regist(self,event):
    	i=0
        passi=self.password.GetValue()
        userde=self.userde.GetValue()
        usern=self.userre.GetValue()
        print passi
        if len(usern)==0:
            wx.MessageBox('Please enter a username','Error',wx.OK | wx.ICON_ERROR)
            return
        if len(userde)==0:
            wx.MessageBox('Please enter a userid','Error',wx.OK | wx.ICON_ERROR)
            return
        if len(passi)==0:
            wx.MessageBox('Please enter a password','Error',wx.OK | wx.ICON_ERROR)
            return
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        cur.execute("SELECT Id FROM Logins")
        rows=cur.fetchall()
        for row in rows :
        	if row[0]==userde:
        		i+=1
        		wx.MessageBox('Enter some other username','error',wx.ICON_INFORMATION | wx.OK)
        		break
        if i==0:
        	query="INSERT INTO Logins(Id,password,username) VALUES (%s,%s,%s)"
        	cur.execute(query,(userde,passi,usern))
        	self.Destroy()
        con.commit()
        con.close()

        
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.cMenuBar()
    def gotomyFrame1(self,event):
        global Roomte 
        y=self.GetTopLevelParent()
        item=y.GetMenuBar().FindItemById(event.GetId())
        Roomte=item.GetText()
        #####################incompleteRoomt=eo.Ge()
        print Roomte
        self.GetTopLevelParent().Destroy()
        MyFrame1().Show()
    def gotomyform(self,event):
        self.GetTopLevelParent().Destroy()
        MyForm().Show()
    def gotomain(self,event):
        self.GetTopLevelParent().Destroy()
        global uid
        if uid=="" :
            MainFrame().Show()
        else :
            BookHistory().Show()
    def gotoMainFR(self,event):
        self.GetTopLevelParent().Destroy()
        MainFrame3().Show()
    def gotomenu(self,event):
        self.GetTopLevelParent().Destroy()
        MainFrame4().Show()

    def cMenuBar(self):

        self.menuBar = wx.MenuBar()

        self.filemenu = wx.Menu()
        self.fileitem2=self.filemenu.Append(id=12, text="&CONTACT US")
        self.fileitem3=self.filemenu.Append(id=16,text="&LOGIN/REGISTER")
        self.fileitem4=self.filemenu.Append(id=20,text="&ADMIN LOGIN")
        self.menuBar.Append(menu=self.filemenu, title="&HOME                                ")
        y=self.GetTopLevelParent()
        y.SetMenuBar(self.menuBar)
        y.Bind(wx.EVT_MENU,self.gotomyform,self.fileitem2)
        y.Bind(wx.EVT_MENU,self.gotomain,self.fileitem3)
        y.Bind(wx.EVT_MENU,self.gotoMainFR,self.fileitem4)


        self.filemenu = wx.Menu()
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        cur.execute("SELECT Bname from Branchs")
        rows=cur.fetchall()
        i=0
        for row in rows:
            self.fileitemx1=self.filemenu.Append(id=i, text=row[0])
            i+=1
            y.Bind(wx.EVT_MENU,self.gotomyFrame1,self.fileitemx1)
        self.menuBar.Append(menu=self.filemenu, title="&RESERVATIONS                                ")
        y=self.GetTopLevelParent()
        y.SetMenuBar(self.menuBar)  
        self.filemenu = wx.Menu()
        self.menu=self.filemenu.Append(id=10, text="&DINING MENU")
        y=self.GetTopLevelParent()
        y.Bind(wx.EVT_MENU,self.gotomenu,self.menu)

        self.menuBar.Append(menu=self.filemenu, title="&FACILITIES                               ")
        con.commit()
        con.close()

    

 
 
########################################################################
class MyForm(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="CONTACT DETAILS")
        panel = MyPanel(self)
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        cur.execute("SELECT * FROM Branchs")
        rows=cur.fetchall()
        a=wx.StaticText(self,label="BRANCH NAME",pos=(100,30))
        font = self.GetFont() 
        font.SetPointSize(14) 
        a.SetFont(font) 
        b=wx.StaticText(self,label="EMAIL",pos=(300,30))
        b.SetFont(font) 
        c=wx.StaticText(self,label="LOCATION",pos=(550,30))
        c.SetFont(font) 
        d=wx.StaticText(self,label="PHONE NUMBER",pos=(750,30))
        d.SetFont(font) 
        pos2=100
        
        for row in rows:
            y=str(row[1])
            Text=wx.StaticText(self,label=y,style=wx.ALIGN_CENTER,pos=(100,pos2))
            y=str(row[2])
            Text=wx.StaticText(self,label=y,style=wx.ALIGN_CENTER,pos=(300,pos2))
            y=str(row[3])
            Text=wx.StaticText(self,label=y,style=wx.ALIGN_CENTER,pos=(550,pos2))
            y=str(row[4])
            Text=wx.StaticText(self,label=y,style=wx.ALIGN_CENTER,pos=(750,pos2))
            pos2=pos2+40
        self.Maximize()
        con.commit()
        con.close()

        
########################################################################

class MyFrame1(wx.Frame):
    
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        global x,Roomte
        wx.Frame.__init__(self, parent=None, title="RESERVATIONS")

        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu') 
        cur=con.cursor()
        panel = MyPanel(self)
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        cur.execute("SELECT DISTINCT RoomType,cost FROM Availability A,(SELECT DISTINCT(Bid) as  id FROM Branchs WHERE Bname=%s)X WHERE X.id=A.Bid",(Roomte,))
        rows=cur.fetchall()
        cur.execute("SELECT DISTINCT RoomType FROM Availability A,(SELECT DISTINCT(Bid) as  id FROM Branchs WHERE Bname=%s)X WHERE X.id=A.Bid",(Roomte,))
        row1=cur.fetchone()
        x=row1[0]
        pos2=30
        i=0
        for row in rows:

            y=str(row[0])
            self.cb1=wx.RadioButton(panel,label=y,style=wx.ALIGN_CENTER,pos=(40,pos2))
            self.cb1.SetValue=False
            self.Bind(wx.EVT_RADIOBUTTON,self.OnChecked)
            r=str(row[1])
            wx.StaticText(panel,pos=(300,pos2),label=r)
            wx.SpinCtrl(panel,value='0',pos=(500,pos2),size=(120,-1),min=0,max=3)
            self.Bind(wx.EVT_SPINCTRL,self.Onspinned)
            t=3-1
            for t in range(0,3):
                pos2+=30
                t=t-1
            pos2+=50;
        pos2-=50
        wx.StaticBox(panel,label="From ",pos=(50,pos2),size=(220,70))
        pos2+=20
        ch=["11","12","13","14","15","16","17"]
        g2=wx.ComboBox(panel,value='11',pos=(50,pos2),choices=ch,size=(60,-1))
        g2.Bind(wx.EVT_COMBOBOX,self.Onfroch)
        wx.ComboBox(panel,value='4',pos=(110,pos2),size=(60,-1))
        wx.ComboBox(panel,value='2019',pos=(170,pos2),size=(100,-1))
        pos2-=20
        wx.StaticBox(panel,label="To ",pos=(400,pos2),size=(220,70))
        pos2+=20
        ch=["11","12","13","14","15","16","17"]
        g1=wx.ComboBox(panel,value='11',pos=(400,pos2),choices=ch,size=(60,-1))
        wx.ComboBox(panel,value='4',pos=(460,pos2),size=(60,-1))
        wx.ComboBox(panel,value='2019',pos=(520,pos2),size=(100,-1))
        g1.Bind(wx.EVT_COMBOBOX,self.Ontoch)
        pos2+=70
        Btn1=wx.Button(panel,wx.ALIGN_CENTER,label="Book",pos=(400,pos2))
        Btn1.Bind(wx.EVT_BUTTON,self.OnBook)
        self.Show()
        self.Maximize()
        con.commit()
        con.close()


    def OnBook(self,event):
        i=0
        global x,y,f,t,c,Roomte,uid
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        f=int(f)
        now1=datetime.date(2019,4,f)
        t=int(t)
        print x
        print t
        print f
        now2=datetime.date(2019,4,t)
        if y==0:
            wx.MessageBox('Number of rooms cannot be 0','Error',wx.OK | wx.ICON_INFORMATION)
            i+=1
        if f>=t:
            wx.MessageBox('Invalid Date','Error',wx.OK | wx.ICON_INFORMATION)
            i+=1
        print i
        
        if i==0 :
            #Check Availability
            cur.execute("SELECT DISTINCT cost,A.Bid FROM Availability A,(SELECT DISTINCT(Bid) as  id FROM Branchs WHERE Bname=%s)X WHERE X.id=A.Bid AND A.RoomType=%s",(Roomte,x,))
            row=cur.fetchone()
            c=row[0]
            d=row[1]
            cur.execute("SELECT nofrooms,froms,tos from Availability A where Bid=%s AND RoomType=%s AND nofrooms>=%s",(d,x,y,))
            rows=cur.fetchall()
            counter=0
            for row in rows :
                r=row[0]
                fro=row[1]
                too=row[2]
                print y
                print r
                if fro==now1:
                    if too==now2:
                        if y==r:
                            counter+=1
                            print "how"
                            cur.execute("DELETE FROM Availability WHERE nofrooms=%s AND froms=%s AND tos=%s AND Bid=%s AND RoomType=%s",(y,now1,now2,d,x,))
                            break
                        if y<r:
                            print "hello"
                            counter+=1
                            cur.execute("UPDATE Availability SET nofrooms=%s WHERE froms=%s AND tos=%s AND Bid=%s AND RoomType=%s",(r-y,fro,too,d,x,))
                            break
                    if too>now2 :
                        if y==r :
                            counter+=1
                            print "hi"
                            cur.execute("UPDATE Availability SET froms=%s WHERE nofrooms=%s AND tos=%s AND Bid=%s AND RoomType=%s",(now2,y,too,d,x,))
                            break
                        if y<r:
                            counter+=1
                            print "Swetha"
                            cur.execute("UPDATE Availability SET nofrooms=%s,tos=%s WHERE froms=%s AND Bid=%s AND RoomType=%s",(r-y,now2,fro,d,x,))
                            cur.execute("INSERT INTO Availability (RoomType,nofrooms,cost,Bid,froms,tos)VALUES(%s,%s,%s,%s,%s,%s)",(x,r,c,d,now2,too,))
                            break
                # All Sub cases Completed _--_
                
                if fro<now1 :
                    if too==now2 :
                        if y==r :
                            print "ym"
                            counter+=1
                            cur.execute("UPDATE Availability SET tos=%s WHERE froms=%s AND nofrooms=%s AND Bid=%s AND RoomType=%s",(now1,fro,r,d,x,))
                        else :
                            counter+=1
                            print "ll"
                            cur.execute("UPDATE Availability SET froms=%s,nofrooms=%s WHERE tos=%s AND Bid=%s AND RoomType=%s",(now1,r-y,too,d,x,))
                            cur.execute("INSERT INTO Availability (Bid,RoomType,nofrooms,froms,tos,cost) VALUES(%s,%s,%s,%s,%s,%s)",(d,x,r,fro,now1,c,))
                            break
                
                    if too>now2:
                        if y==r :
                            counter+=1
                            print "Bharathi"
                            cur.execute("UPDATE Availability SET tos=%s WHERE froms=%s AND nofrooms=%s AND Bid=%s AND RoomType=%s",(now1,fro,r,d,x,))
                            cur.execute("INSERT INTO Availability (tos,froms,nofrooms,Bid,RoomType,cost) VALUES (%s,%s,%s,%s,%s,%s)",(too,now2,r,d,x,c,))
                        else :
                            counter+=1
                            print "tm"
                            cur.execute("UPDATE Availability SET tos=%s WHERE froms=%s AND nofrooms=%s AND Bid=%s AND RoomType=%s",(now1,fro,r,d,x,))
                            cur.execute("INSERT INTO Availability (tos,froms,nofrooms,Bid,RoomType,cost) VALUES (%s,%s,%s,%s,%s,%s)",(too,now2,r,d,x,c,))
                            cur.execute("INSERT INTO Availability (tos,froms,nofrooms,Bid,RoomType,cost) VALUES (%s,%s,%s,%s,%s,%s)",(now2,now1,r-y,d,x,c,))
                            break
            
            if counter==0 :
                wx.MessageBox('Rooms Not Available','ERROR',wx.OK | wx.ICON_INFORMATION)

            else :
                if len(uid)!=0 :
                    cur.execute("INSERT INTO BOOKINGSS(Bid,Usid,RoomType,nofrooms,cost,froms,too) VALUES(%s,%s,%s,%s,%s,%s,%s)",(d,uid,x,y,c*y,now1,now2,))
                    con.commit()
                    #con.close()
                    self.Destroy()
                    BookHistory().Show()
                    self.Maximize()
                    a=MyFrame2().ShowModal()
                    print a
                else :
                    wx.MessageBox('Please Sign In or Sign Up','ALERT',wx.OK | wx.ICON_INFORMATION)
                    self.Destroy()
                    MainFrame().Show()
        con.commit()
        con.close()


        
        
    def OnChecked(self,event):
        global x
        cb=event.GetEventObject()
        if cb.GetValue()==True:
            x=cb.GetLabel()
    def Onspinned(self,event):
        global y
        cl=event.GetEventObject()
        if cl.GetValue()!=0 :
            y=cl.GetValue()
    def Onfroch(self,event):
        global f
        cl=event.GetEventObject()
        f=cl.GetValue()
    def Ontoch(self,event):
        global t
        cl=event.GetEventObject()
        t=cl.GetValue()

#########################################################################################################


#########################################################################################################
class MyFrame2(wx.Dialog) :
    """docstring for """
    def __init__(self):
        wx.Dialog.__init__(self,None,title="BILL")
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        cur.execute("SELECT Bid,RoomType,nofrooms,froms,too,cost FROM BOOKINGSS ORDER BY id DESC")
        row=cur.fetchone()
        cur.execute("SELECT Bname FROM Branchs WHERE Bid=%s",(row[0],))
        con.commit()
        con.close()
        row1=cur.fetchone()
        usersizer_r=wx.BoxSizer(wx.HORIZONTAL)
        user=wx.StaticText(self,label="YOUR NAME: ")
        user_val=wx.StaticText(self,label=uid)
        usersizer_r.Add(user,0,wx.ALL | wx.CENTER ,5)
        usersizer_r.Add(user_val,0,wx.ALL | wx.CENTER ,5)

        usersizer_2=wx.BoxSizer(wx.HORIZONTAL)
        
        hotelname_lbl=wx.StaticText(self,label="Hotel Name: ")
        hotelname_value=wx.StaticText(self,label=row1[0])
        usersizer_2.Add(hotelname_lbl,0,wx.ALL | wx.CENTER,5)
        usersizer_2.Add(hotelname_value,0,wx.ALL | wx.CENTER,5)

        p_sizer=wx.BoxSizer(wx.HORIZONTAL)
        RoomType_lbl = wx.StaticText(self, label="Room Type: ")
        p_sizer.Add(RoomType_lbl, 0, wx.ALL|wx.CENTER, 5)
        Roomtype_val= wx.StaticText(self,label=row[1])
        p_sizer.Add(Roomtype_val, 0, wx.ALL, 5)
        
        nofrooms=wx.BoxSizer(wx.HORIZONTAL)
        nofrooms_lbl = wx.StaticText(self, label="Number of Rooms: ")
        nofrooms.Add(nofrooms_lbl, 0, wx.ALL|wx.CENTER, 5)
        nofrooms_val= wx.StaticText(self,label=str(row[2]))
        nofrooms.Add(nofrooms_val, 0, wx.ALL, 5)

        From=wx.BoxSizer(wx.HORIZONTAL)
        From_lbl = wx.StaticText(self, label="From: ")
        From.Add(From_lbl, 0, wx.ALL|wx.CENTER, 5)
        From_val= wx.StaticText(self,label=str(row[3]))
        From.Add(From_val, 0, wx.ALL, 5)

        To=wx.BoxSizer(wx.HORIZONTAL)
        To_lbl = wx.StaticText(self, label="To: ")
        To.Add(To_lbl, 0, wx.ALL|wx.CENTER, 5)
        To_val= wx.StaticText(self,label=str(row[4]))
        To.Add(To_val, 0, wx.ALL, 5)

        Cost=wx.BoxSizer(wx.HORIZONTAL)
        Cost_lbl = wx.StaticText(self, label="Bill Amount: ")
        Cost.Add(Cost_lbl, 0, wx.ALL|wx.CENTER, 5)
        Cost_val= wx.StaticText(self,label=str(row[5]))
        Cost.Add(Cost_val, 0, wx.ALL, 5)

        End=wx.BoxSizer(wx.HORIZONTAL)
        End_lbl = wx.StaticText(self, label="You can pay and collect your bill when you check out.")
        End.Add(End_lbl, 0, wx.ALL|wx.CENTER, 5)
        btn1=wx.Button(self,label="OK")
        btn1.Bind(wx.EVT_BUTTON,self.Closing)

        main_sizer=wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(usersizer_r,0,wx.ALL,5)
        main_sizer.Add(usersizer_2,0,wx.ALL,5)
        main_sizer.Add(p_sizer,0,wx.ALL,5)
        main_sizer.Add(nofrooms,0,wx.ALL,5)
        main_sizer.Add(From,0,wx.ALL,5)
        main_sizer.Add(To,0,wx.ALL,5)
        main_sizer.Add(Cost,0,wx.ALL,5)
        main_sizer.Add(btn1,0,wx.ALL | wx.CENTER,5)
        main_sizer.Add(End,0,wx.ALL | wx.CENTER,5)
        self.SetSizer(main_sizer)
    def Closing(self,event) :
        self.Destroy()
        self.Maximize()

########################################################################################################

class BookHistory(wx.Frame) :
    def __init__(self):
        global uid
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)
        hbox=wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(hbox)

        panel = MyPanel(self)
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        mm=wx.StaticText(self,label="YOUR BOOKING HISTORY",pos=(550,10))
        font = self.GetFont() 
        font.SetPointSize(14) 
        mm.SetFont(font)
        mm.SetBackgroundColour((0,0,0))  
      
        cur.execute("SELECT id,Bid,RoomType,cost,nofrooms,froms,too FROM BOOKINGSS WHERE Usid=%s",(uid,))
        rows=cur.fetchall()
        con.commit()
        con.close()
        Btn1=wx.Button(self,label='LOG OUT',pos=(1200,10))
        Btn1.Bind(wx.EVT_BUTTON,self.Onclicked)
        Text=wx.StaticText(self,label='B Id',style=wx.ALIGN_CENTER,pos=(20,50))
        font.SetPointSize(12) 
        Text.SetFont(font)
        Text=wx.StaticText(self,label='Branch Id',style=wx.ALIGN_CENTER,pos=(100,50))
        Text.SetFont(font)
        Text=wx.StaticText(self,label='Room Type',style=wx.ALIGN_CENTER,pos=(170,50))
        Text.SetFont(font)
        Text=wx.StaticText(self,label='Bill Amt',style=wx.ALIGN_CENTER,pos=(320,50))
        Text.SetFont(font)
        Text=wx.StaticText(self,label='No. of rooms',style=wx.ALIGN_CENTER,pos=(470,50))
        Text.SetFont(font)
        Text=wx.StaticText(self,label='Check-In',style=wx.ALIGN_CENTER,pos=(620,50))
        Text.SetFont(font)
        Text=wx.StaticText(self,label='Check-Out',style=wx.ALIGN_CENTER,pos=(780,50))
        Text.SetFont(font)
        pos2=110
        for row in rows:
            self.Id=row[0]
            self.room=str(row[2])
            self.Bookid=row[1]
            Text=wx.StaticText(self,label=str(self.Bookid),style=wx.ALIGN_CENTER,pos=(20,pos2))
            Text=wx.StaticText(self,label=str(self.Id),style=wx.ALIGN_CENTER,pos=(100,pos2))
            Text=wx.StaticText(self,label=str(self.room),style=wx.ALIGN_CENTER,pos=(170,pos2))
            self.co=str(row[3])
            Text=wx.StaticText(self,label=str(self.co),style=wx.ALIGN_CENTER,pos=(320,pos2))
            self.nor=str(row[4])
            Text=wx.StaticText(self,label=str(self.nor),style=wx.ALIGN_CENTER,pos=(470,pos2))
            self.fr=str(row[5])
            Text=wx.StaticText(self,label=str(self.fr),style=wx.ALIGN_CENTER,pos=(620,pos2))
            self.tol=str(row[6])
            Text=wx.StaticText(self,label=str(self.tol),style=wx.ALIGN_CENTER,pos=(780,pos2))
            Btn2=wx.Button(self,id=self.Id,label="CANCEL",pos=(900,pos2-8))
            Btn2.Bind(wx.EVT_BUTTON,self.Oncancel)
            pos2=pos2+40
        self.Maximize()
    def Oncancel(self,event):
            cb=event.GetEventObject().GetId()
            cb1=event.GetEventObject().GetLabel()
            print cb
            conl=mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
            with conl:
                cur=conl.cursor()
            cur.execute("SELECT Bid,RoomType,nofrooms,froms,too FROM BOOKINGSS WHERE id=%s",(cb,))
            row1=cur.fetchone()
            cur.execute("DELETE FROM BOOKINGSS WHERE id=%s",(cb,))
            wx.MessageBox('The booking is cancelled','CANCELLATION',wx.OK | wx.ICON_INFORMATION)
            #update AVAILABILITY
            cur.execute("SELECT nofrooms,froms,tos,cost,Bid,RoomType FROM Availability WHERE Bid=%s AND RoomType=%s",(row1[0],row1[1]))
            rows=cur.fetchall()
            conl.commit()
            #print rows
            print row1[3]
            print row1[4]
            count=0
            for row in rows :
                if row[1]==row1[3] :
                    if row[2]==row1[4] :
                        count+=1
                        print "look"
                        cur.execute("UPDATE Availability SET nofrooms=%s WHERE Bid=%s AND RoomType=%s AND froms=%s AND tos=%s",(row[0]+row1[2],row1[0],row1[1],row1[3],row1[4],))
            #case 2 insert
            conl.commit()
            conl.close()
            conl1=mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
            with conl1 : 
                cur=conl1.cursor()
                i=0
                for row in rows :
                    for row2 in rows :
                        i+=1
                        print row
                        if row[0]+row1[2]==row2[0] and row[3]==row2[3] and row[4]==row2[4] and row[5]==row2[5] and row[2]==row2[1] :
                            print "good"
                            cur.execute("UPDATE Availability SET tos=%s WHERE Bid=%s AND froms=%s AND nofrooms=%s AND RoomType=%s",(row2[2],row[4],row[1],row2[0],row[5],))
                            cur.execute("DELETE FROM Availability WHERE Bid=%s AND RoomType=%s AND froms=%s AND nofrooms=%s",(row[4],row[5],row2[1],row2[0],))
                            rowr=cur.fetchall()
                            print rowr
                            conl1.commit()
            if count==0 :
                cur.execute("SELECT nofrooms,froms,tos,cost,Bid,RoomType FROM Availability WHERE Bid=%s AND RoomType=%s",(row1[0],row1[1],))
                row=cur.fetchone()
                cur.execute("INSERT INTO AVAILABILITY (RoomType,Bid,cost,nofrooms,froms,tos) VALUES (%s,%s,%s,%s,%s,%s)",(row1[1],row1[0],row[3],row1[2],row1[3],row1[4]))
            conl1.close()
            print i
            self.Destroy()
            BookHistory().Show()
            self.Maximize()
            #con.commit()
            #.Show()
    def Onclicked(self,event) :
            global uid
            uid=""
            self.Destroy()
            MainFrame().Show()
            self.Maximize()



#######################################################################################################
class MainFrame(wx.Frame):
 
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App")
        image = wx.Image('htl.jpeg', wx.BITMAP_TYPE_JPEG)
        temp=image.ConvertToBitmap()
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        str1 = "%s  %dx%d" % (image, temp.GetWidth(),
                                  temp.GetHeight())
        panel = MyPanel(self)
        hbox=wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(hbox)
        
    
        # Ask user to login
        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl = wx.StaticText(self, label="Username",size=(573,30),pos=(620,210))
        user_lbl.SetForegroundColour((0,0,0)) 
        user_lbl.SetBackgroundColour((0,0,0)) 
        font = self.GetFont() 
        font.SetPointSize(12) 
        user_lbl.SetFont(font) 
        self.user = wx.TextCtrl(self,pos=(610,230))
        user_sizer.Add(self.user, 1, wx.ALL, 4)
 
        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)
         # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)
 
        p_lbl = wx.StaticText(self, label="Password",size=(573,80),pos=(620,268))
        p_lbl.SetForegroundColour((0,0,0)) 
        p_lbl.SetBackgroundColour((0,0,0)) 
        font = self.GetFont() 
        font.SetPointSize(12) 
        p_lbl.SetFont(font)  
        self.password = wx.TextCtrl(self,pos=(610,290),style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        btn = wx.Button(self, label="Login",pos=(573,380),size=(180,35))
        btn.Bind(wx.EVT_BUTTON,self.onLogin)
        btnr=wx.Button(self,label="Register",pos=(573,340),size=(180,35))
        btnr.Bind(wx.EVT_BUTTON,self.gotoreg)
        
        self.Show()
        self.Maximize()
    #---------------------------------------------------------------------
    #----------------------------------------------------------------------
    def gotoreg(self,event):
        a=RegisterDialog().ShowModal()
        print a
    #-----------------------------------------------------------------------
    def gotobranch(self,event):
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        cur.execute("select* from Branchs")
        rows=cur.fetchall()
        for row in rows:
            print row[0]
        con.commit()
        con.close()
    #-------------------------------------------------------------------------
     
    #-----------------------------------------------------------------------
    def onLogin(self, event):
                global uid
                i=0
                user_password = self.password.GetValue()
                user_id=self.user.GetValue()
                con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
                cur=con.cursor()
                with con:
                    cur=con.cursor()
                    cur.execute("SELECT * FROM Logins")
                    rows=cur.fetchall()
                    for row in rows:
                            paaswoed= row[1]
                            if user_id==row[0]:
                                if user_password == paaswoed:
                                    i+=1
                                    uid=user_id
                                    print "You are now logged in!"
                                    self.Destroy()
                                    BookHistory().Show()
                    if i==0:
                    	wx.MessageBox('Incorrect Login','Error',wx.ICON_EXCLAMATION | wx.OK)
                                
                con.commit()
                con.close()
        #----------------------------------------------------------------------
class MainFrame3(wx.Frame):
 
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="AdminLogin")
    
        # Ask user to login
        # user info
        user_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        panel = MyPanel(self)
        user_lbl2 = wx.StaticText(self, label="Admin Id",pos=(620,240))
        font = self.GetFont() 
        font.SetPointSize(12) 
        user_lbl2.SetFont(font) 
        user_lbl2.SetForegroundColour((0,0,0)) 
        self.admin = wx.TextCtrl(self,pos=(610,260))
 
        # pass info
        p_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
         # pass info
        p_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
 
        p_lbl_1 = wx.StaticText(self, label="Password",pos=(620,310))
        font = self.GetFont() 
        font.SetPointSize(12) 
        p_lbl_1.SetFont(font) 
        p_lbl_1.SetForegroundColour((0,0,0)) 
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,pos=(610,330))
 
        main_sizer_1 = wx.BoxSizer(wx.VERTICAL)
        main_sizer_1.Add(user_sizer_1, 0, wx.ALL, 5)
        main_sizer_1.Add(p_sizer_1, 0, wx.ALL, 5)
 
        btn_1= wx.Button(self, label="Login",pos=(580,380),size=(180,35))
        btn_1.Bind(wx.EVT_BUTTON,self.gotoOnAdmLog)
        self.Show()
        self.Maximize()
    def gotoOnAdmLog(self,event):
        global aid
        i=0
        adm_password = self.password.GetValue()
        admin_id=self.admin.GetValue()
        con = mdb.connect(host='localhost',database='testdb',user='root', password='ramya vishhnu')
        cur=con.cursor()
        with con:
            cur=con.cursor()
            cur.execute("SELECT * FROM AdminLogin")
            rows=cur.fetchall()
            for row in rows:
                paaswoed= row[2]
                if admin_id==row[0]:
                    if adm_password == paaswoed:
                        i+=1
                        aid=admin_id
                        print "You are now logged in!"
                        self.Destroy()
                        MainFr().Show()
            if i==0:
                wx.MessageBox('Incorrect Login','Error',wx.ICON_EXCLAMATION | wx.OK)
            con.commit()
            con.close()

       
    def gotoadminreg(self,event):
        self.Destroy()
        a=MainFr().Show()

class MainFr(wx.Frame): 

    def __init__(self):
        con = mdb.connect(host='localhost',
                             database='testdb',
                             user='root',
                            password='ramya vishhnu')
        cur=con.cursor()
        global uid
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)
        Btn1=wx.Button(self,label='LOG OUT',pos=(1200,50))
        Btn1.Bind(wx.EVT_BUTTON,self.Onclicked)
        Btn2=wx.Button(self,label='Update Menu',pos=(1200,20))
        Btn2.Bind(wx.EVT_BUTTON,self.OnMenuUpdate)

        self.Show()
        self.Maximize(True)


        m=wx.StaticText(self,label="BOOKING HISTORY",pos=(500,10))
        font = self.GetFont() 
        font.SetPointSize(14) 
        m.SetFont(font) 
        m.SetBackgroundColour((0,0,0))
        cur.execute("SELECT * FROM BOOKINGSS")
        pos2=155
        rows=cur.fetchall()
        font = self.GetFont() 
        font.SetPointSize(12.5)
        m=wx.StaticText(self,label="Customer Name",pos=(20,100))
        m.SetFont(font) 
        m=wx.StaticText(self,label="Booking Id",pos=(150,100))
        m.SetFont(font) 
        m=wx.StaticText(self,label="Room Type",pos=(280,100))
        m.SetFont(font) 
        m=wx.StaticText(self,label="No. of rooms",pos=(460,100))
        m.SetFont(font) 
        m=wx.StaticText(self,label="Amount",pos=(590,100))
        m.SetFont(font) 
        m=wx.StaticText(self,label="From",pos=(730,100))
        m.SetFont(font) 
        m=wx.StaticText(self,label="To",pos=(830,100))
        m.SetFont(font) 
        k=1
        for row in rows:
            self.Name=str(row[1])
            Text=wx.StaticText(self,label=str(self.Name),style=wx.ALIGN_CENTER,pos=(20,pos2))
            self.room=str(row[2])
            Text=wx.StaticText(self,label=str(self.room),style=wx.ALIGN_CENTER,pos=(150,pos2))
            self.co=str(row[3])
            Text=wx.StaticText(self,label=str(self.co),style=wx.ALIGN_CENTER,pos=(280,pos2))
            self.nor=str(row[4])
            Text=wx.StaticText(self,label=str(self.nor),style=wx.ALIGN_CENTER,pos=(460,pos2))
            self.fr=str(row[5])
            Text=wx.StaticText(self,label=str(self.fr),style=wx.ALIGN_CENTER,pos=(590,pos2))
            self.tol=str(row[6])
            Text=wx.StaticText(self,label=str(self.tol),style=wx.ALIGN_CENTER,pos=(730,pos2))
            self.too=str(row[7])
            Text=wx.StaticText(self,label=str(self.too),style=wx.ALIGN_CENTER,pos=(830,pos2))
            Btn2=wx.Button(self,id=row[0],label="CHECK OUT",pos=(1000,pos2-10))
            Btn2.Bind(wx.EVT_BUTTON,self.Oncancel2)
            pos2=pos2+40
            self.Maximize()
    def Oncancel2(self,event):
        con = mdb.connect(host='localhost',
                             database='testdb',
                             user='root',
                            password='ramya vishhnu')

        cur=con.cursor()
        cb=event.GetEventObject().GetId()
        print cb
        cur.execute("DELETE FROM BOOKINGSS WHERE id=%s",(cb,))
        con.commit()
        wx.MessageBox('The booking is checked out ;)','CHECKED OUT',wx.OK | wx.ICON_INFORMATION)
        self.Destroy()
        MainFr().Show()
        con.close()
        self.Maximize()



    def Onclicked(self,event) :
        global uid
        uid=""
        self.Destroy()
        MainFrame().Show()
    def OnMenuUpdate(self,event):
        self.Destroy()
        MainFrame5().Show()

class MainFrame4(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Menu")
        con = mdb.connect(host='localhost',
                             database='testdb',
                             user='root',
                            password='ramya vishhnu')
        cur=con.cursor()
        panel = MyPanel(self)
        m=wx.StaticText(self,label="MENU",pos=(500,10))
        font = self.GetFont() 
        font.SetPointSize(17) 
        m.SetFont(font) 
        m.SetBackgroundColour((0,0,0))
        cur.execute("SELECT * FROM menu")
        rows=cur.fetchall()
        wx.StaticText(self,label="Item Name",pos=(300,80))
        wx.StaticText(self,label="Type",pos=(500,80))
        wx.StaticText(self,label="Price",pos=(620,80))
        pos2=120
        for row in rows:
            self.Name=str(row[0])
            Text=wx.StaticText(self,label=str(self.Name),style=wx.ALIGN_CENTER,pos=(300,pos2))
            self.Type=str(row[1])
            Text=wx.StaticText(self,label=str(self.Type),style=wx.ALIGN_CENTER,pos=(500,pos2))
            self.price=str(row[2])
            Text=wx.StaticText(self,label=str(self.price),style=wx.ALIGN_CENTER,pos=(620,pos2))
            pos2=pos2+40
            self.Maximize()
            con.commit()
class MainFrame5(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="New ")
        con = mdb.connect(host='localhost',
                             database='testdb',
                             user='root',
                            password='ramya vishhnu')
        cur=con.cursor()
        panel = MyPanel(self)
        m=wx.StaticText(self,label="ADD ITEMS",pos=(580,10))
        font = self.GetFont() 
        font.SetPointSize(17) 
        m.SetFont(font) 
        m.SetBackgroundColour((0,0,0))
        cur.execute("SELECT * FROM menu")
        rows=cur.fetchall()
        hbox=wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(hbox)
        con.commit()
        con.close()
    
        # Ask user to login
        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl = wx.StaticText(self, label="Item Name",size=(573,30),pos=(620,210))
        user_lbl.SetForegroundColour((0,0,0)) 
        user_lbl.SetBackgroundColour((0,0,0)) 
        font = self.GetFont() 
        font.SetPointSize(12) 
        user_lbl.SetFont(font) 
        self.item1 = wx.TextCtrl(self,pos=(610,230))
 
        p_lbl = wx.StaticText(self, label="Type",size=(573,80),pos=(640,268))
        p_lbl.SetForegroundColour((0,0,0)) 
        p_lbl.SetBackgroundColour((0,0,0)) 
        font = self.GetFont() 
        font.SetPointSize(12) 
        p_lbl.SetFont(font)  
        self.type1= wx.TextCtrl(self,pos=(610,290))
        p_lbl2=wx.StaticText(self,label="Price",size=(573,80),pos=(640,340))
        p_lbl2.SetForegroundColour((0,0,0)) 
        p_lbl2.SetBackgroundColour((0,0,0)) 
        p_lbl2.SetFont(font)
        self.price = wx.TextCtrl(self,pos=(610,360))
        btn = wx.Button(self, label="Update",pos=(573,420),size=(180,35))
        btn.Bind(wx.EVT_BUTTON,self.OnMenuAdd)
        self.Show()
        self.Maximize()
    def OnMenuAdd(self,event):
        con = mdb.connect(host='localhost',
                             database='testdb',
                             user='root',
                            password='ramya vishhnu')
        cur=con.cursor()
        itm1=self.item1.GetValue()
        typ1=self.type1.GetValue()
        price1=self.price.GetValue()
        if len(itm1)!=0 and len(typ1)!=0 and len(price1)!=0: 
            cur.execute("INSERT INTO menu(Item,type,price) VALUES (%s,%s,%s)",(itm1,typ1,price1,))
            self.Destroy()
            MainFr().Show()
            con.commit()
            con.close()
        else:
            wx.MessageBox('Please enter a username','Error',wx.OK | wx.ICON_ERROR)
            con.close()
        


        

 
if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()