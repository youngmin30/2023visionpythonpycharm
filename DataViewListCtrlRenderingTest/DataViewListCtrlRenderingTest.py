# -*- coding: utf-8 -*- 
import wx.dataview
import cx_Oracle

# 이 함수는 범용성 있게 사용할 수 있다. 필요한 자리에 카피해서 
# 사용하면 된다. (사용하는 DataViewListCtrl객체를 매개변수로 전달하면
# 그 DataViewListCtrl객체에 보낸 질의의 결과가 랜더링 된다. 
def rendering(dateViewList,sql,user,password):
        # Execute SQL and fetch all results
        connection = cx_Oracle.connect(user,password, 'xe')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Clear output list
        dateViewList.DeleteAllItems()
        dateViewList.ClearColumns()
 
        # Get column names from cursor description
        col_names = [desc[0] for desc in cursor.description]
        print(col_names)
        # Set column titles for output control
        for col_name in col_names:
            dateViewList.AppendTextColumn(col_name)

        # Populate output list with results
        for row in rows:
            row_str = [str(val) for val in row] # convert each element in row to str
            print(row_str)
            dateViewList.AppendItem(row_str)

        # Close database connection
        cursor.close()
        connection.close()




class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent,title ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SQL Tester ver 1.0 by JWS", pos = wx.DefaultPosition, size = wx.Size( 807,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
        
        self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.sqlArea = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,250 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_WORDWRAP )
        self.sqlArea.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer2.Add( self.sqlArea, 0, wx.ALL, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"dbUser/Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button1, 0, wx.ALL, 5 )
        
        self.txtUser = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"madang", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txtUser, 0, wx.ALL, 5 )
        
        
        self.txtPassword = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"madang", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txtPassword, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Tables:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"Cue", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        bSizer6.Add( self.m_button3, 0, wx.ALL, 5 ) 
        
        self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button4, 0, wx.ALL, 5 )
        
        comboTableChoices = []
        self.comboTable = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Tables", wx.DefaultPosition, wx.Size( 210,-1 ), comboTableChoices, 0 )
        bSizer6.Add( self.comboTable, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.dvlc = wx.dataview.DataViewListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,300 ), wx.dataview.DV_MULTIPLE|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
        bSizer3.Add( self.dvlc, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        self.m_splitter1.SplitHorizontally( self.m_panel1, self.m_panel2, 0 )
        bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.on_changeCombo ) # 콤보 박스의 테이블명을 읽어서 gui에 뿌려 준다.
        self.m_button2.Bind( wx.EVT_BUTTON, self.on_changeCombo ) # 콤보 박스의 테이블명을 읽어서 gui에 뿌려 준다.
        self.m_button3.Bind( wx.EVT_BUTTON, self.on_execute ) # on_execute cue버튼을 누르면 실행하게 하는 메소드
        # self.m_button5.Bind( wx.EVT_BUTTON, self.on_search ) # 추가해야 한다.
        self.m_button4.Bind( wx.EVT_BUTTON, self.on_clear ) # clear 버튼을 누르면 모두 지우는 메소드
        # 누락된 코드가 있음.
        self.comboTable.Bind(wx.EVT_COMBOBOX, self.on_combo) # on_combo 버튼을 누르면 이벤트가 수행하게 되는 부분
    def __del__( self ):
        pass
    
    def m_splitter1OnIdle( self, event ):
        self.m_splitter1.SetSashPosition( 0 )
        self.m_splitter1.Unbind( wx.EVT_IDLE )

    def OnClose(self, event):
        # Destroy frame and quit app
        self.Destroy()
        event.Skip()
    
    
    def on_changeCombo( self, event ):
            
        user = self.txtUser.GetValue();
        password = self.txtPassword.GetValue();
        self.comboTable.Clear()
        self.comboTable.LabelText = "Tables"
        connection = cx_Oracle.connect(user,password, 'xe')
        cursor = connection.cursor()
        sql ="SELECT TABLE_NAME FROM USER_TABLES" # 공식임
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        for x in rows: 
            self.comboTable.AppendItems(str(x[0]))
        cursor.close() 
        connection.close()
        
        event.Skip()
    
    
    def on_clear(self, event):
        # Clear output list
        self.dvlc.DeleteAllItems()
        self.dvlc.ClearColumns()
        self.sqlArea.SetValue('')

    def on_execute(self, event):
        sql = self.sqlArea.GetValue()
        sql = sql.replace(';', '')  # ';'을 빈 문자열로 대체
        print(sql)
        user = self.txtUser.GetValue();
        password = self.txtPassword.GetValue();
        rendering(self.dvlc, sql, user, password)
    
    def on_combo(self, event):
        selected_item = self.comboTable.GetValue()
        user = self.txtUser.GetValue();
        password = self.txtPassword.GetValue();
        sql = "SELECT * FROM "+str(selected_item)
        self.sqlArea.SetValue(sql)
        rendering(self.dvlc, sql, user, password)
        

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None, title="SQL Tester")
    frame.Show()
    app.MainLoop()