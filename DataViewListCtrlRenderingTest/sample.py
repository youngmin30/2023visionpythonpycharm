'''
Created on 2023. 3. 30.

@author: youngmin
'''
'''
Created on 2023. 3. 29.
비젼직업전문학교 성주원 교수 
@author: vscsem
'''
import wx
import wx.dataview as dv
import cx_Oracle

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(800, 800))

        self.panel_input = wx.Panel(self)
        self.panel_output = wx.Panel(self)

        # Create input controls
        #self.text_input = wx.TextCtrl(self.panel_input, style=wx.TE_MULTILINE)
        self.text_input = wx.TextCtrl( self.panel_input, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,300 ), wx.HSCROLL|wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_WORDWRAP )
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.text_input.SetFont(font)
        self.btn_execute = wx.Button(self.panel_input, label="Execute")
        self.btn_execute.Bind(wx.EVT_BUTTON, self.on_execute)
        
        self.btn_clear = wx.Button(self.panel_input, label="Clear")
        self.btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)

        # Create output control
        self.listctrl_output = dv.DataViewListCtrl(self.panel_output)

        # Add controls to sizers
        sizer_input = wx.BoxSizer(wx.VERTICAL)
        sizer_input.Add(self.text_input, 1, wx.EXPAND | wx.ALL, 5)
        sizer_input.Add(self.btn_execute, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizer_input.Add(self.btn_clear, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        
        self.panel_input.SetSizer(sizer_input)

        sizer_output = wx.BoxSizer(wx.VERTICAL)
        sizer_output.Add(self.listctrl_output, 1, wx.EXPAND | wx.ALL, 5)
        self.panel_output.SetSizer(sizer_output)

        # Add panels to main sizer
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_main.Add(self.panel_input, 0, wx.EXPAND | wx.ALL, 5)
        sizer_main.Add(self.panel_output, 1, wx.EXPAND | wx.ALL, 5)

        # Set main sizer for frame and center
        self.SetSizer(sizer_main)
        self.Center()

        # Bind EVT_CLOSE event to OnClose method
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        # Destroy frame and quit app
        self.Destroy()
        event.Skip()
        
    def on_clear(self, event):
        # Clear output list
        self.listctrl_output.DeleteAllItems()
        self.listctrl_output.ClearColumns()
        self.text_input.SetValue('')
        
    def on_execute(self, event):
        # Get input SQL statement
        
        # start, end = self.text_input.GetSelection()
        # if start == end:
        sql = self.text_input.GetValue()
        # else: 
        #     sql = self.text_input.GetValue()[start:end]
        #

        sql = sql.replace(';', '')  # ';'을 빈 문자열로 대체
        print(sql)
        
        # Execute SQL and fetch all results
        connection = cx_Oracle.connect('madang', 'madang', 'xe')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Clear output list
        self.listctrl_output.DeleteAllItems()
        self.listctrl_output.ClearColumns()
 
        # Get column names from cursor description
        col_names = [desc[0] for desc in cursor.description]

        # Set column titles for output control
        for col_name in col_names:
            self.listctrl_output.AppendTextColumn(col_name)

        # Populate output list with results
        for row in rows:
            row_str = [str(val) for val in row] # convert each element in row to str

            self.listctrl_output.AppendItem(row_str)

        # Close database connection
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, title="SQL Tester")
    frame.Show()
    app.MainLoop()