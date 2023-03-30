'''
Created on 2023. 3. 30.
oraclePool은 공통 모듈이다.
oracle 데이터를 파이썬으로 바꾼 부분이 렌더링하는 부분이다.
@author: youngmin
'''

import cx_Oracle
import pandas as pd
from sqlalchemy import create_engine,text
import wx.dataview
import datetime

# 여기에 있는 함수는 범용성 있게 사용할 수 있다. 필요한 자리에 카피해서 
# 사용해도 된다. 

def getConnection(xuser, xpassword,xurl='localhost', xport='1521', xsid='xe'):
    # Oracle 데이터베이스에 연결하기 위한 SQLAlchemy 엔진 생성
    engine = create_engine('oracle+cx_oracle://%s:%s@localhost:1521/xe' % (xuser, xpassword))
    # 엔진으로부터 연결을 가져와서 반환
    conn = engine.connect() 
    return conn

def getMeta(tableName, xuser, xpassword):
    try:
        # create SQLAlchemy engine
        engine = create_engine('oracle+cx_oracle://' + xuser + ':' + xpassword + '@localhost:1521/XE')
        # execute query
        # 컬럼명과 데이터타입을 리턴하는 질의
        sql = "SELECT column_name, data_type FROM user_tab_columns WHERE table_name = '" + tableName + "'"
        result = engine.execute(sql).fetchall() # 엔진을 excute하고 sql 질의를 넣음.
        # close connection
        engine.dispose() # 엔진을 끝낸다.
        return result
    except Exception as error:
        print(f"Error while fetching metadata from Oracle database: {error}")

        
# 질의로 select 결과를 튜플로 얻기 
def getRows(sql, xuser, xpassword):
# Oracle 데이터베이스 연결
    con = getConnection(xuser, xpassword)
    # SQL 문 실행 결과를 데이터프레임으로 변환
    df = pd.read_sql(sql, con)
    # 데이터프레임에서 튜플 리스트로 변환
    rows = [tuple(x) for x in df.values]
    # 연결 종료
    con.close()
    return rows # 튜플을 담은 리스트인 row로 리턴한다. [('', '', ''), ('', '', '')]


def getMeta2(sql, xuser, xpassword):
    # SQLAlchemy 엔진 생성
    engine = create_engine('oracle+cx_oracle://%s:%s@localhost:1521/xe' % (xuser, xpassword))
    # SQL 문 실행 결과를 데이터프레임으로 변환
    df = pd.read_sql(text(sql), engine)
    # 데이터프레임에서 컬럼 이름과 타입 정보를 가져와서 메타 데이터 생성
    meta = []
    for col in df.dtypes.items():
        column_name = col[0]
        column_type = col[1].name
        meta.append((column_name, column_type))
    # 연결 종료
    engine.dispose()
    return meta


# (사용하는 DataViewListCtrl객체를 매개변수로 전달하면
# 그 DataViewListCtrl객체에 보낸 질의의 결과가 랜더링 된다. 
def rendering(dateViewList, sql, user, password): # rendering 데이터를 표에 뿌리는 것, 표현하는 것 예) 오토캐드 설계 프로그램 기계, 건물, 선박 설계 최종적으로 쓰리디맥스로 랜더링할 수도 있음. 장판인지 대리석이든지에 따라서 달라지는 것처럼.
   oracle_data_types = {
    'int64':float,
    'object':str,
    'CHAR': str,
    'VARCHAR2': str,
    'NCHAR': str,
    'NVARCHAR2': str,
    'DATE': datetime.datetime,
    'NUMBER': float,
    'FLOAT': float,
    'BINARY_FLOAT': float,
    'BINARY_DOUBLE': float,
    'TIMESTAMP': datetime.datetime,
    'TIMESTAMP(6)': datetime.datetime, # hire_date에 해당하는 데이터 타입 추가
    'datetime64[ns]':datetime.datetime,
    'float64':float,
    }
   # Execute SQL and fetch all results
   connection = cx_Oracle.connect(user, password, 'xe')
   # 숫자컬럼은 오른쪽정렬을 위해 사용 
   meta = getMeta2(sql, user, password)
   cursor = connection.cursor()
   cursor.execute(sql)
   rows = cursor.fetchall()

   # Clear output list
   dateViewList.DeleteAllItems()
   dateViewList.ClearColumns()

   # Get column names from cursor description
   col_names = [desc[0] for desc in cursor.description]
   print(col_names) # 0번째 것이 컬럼 이름이고, 그것만 꺼내서 넣어준다.
   
   for col in meta:
        column_type = oracle_data_types[col[1]]
        if column_type == str :
            dateViewList.AppendTextColumn(col[0], width=wx.COL_WIDTH_AUTOSIZE, mode=wx.dataview.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT, flags=wx.dataview.DATAVIEW_COL_RESIZABLE)
        elif column_type == float or column_type == int:
            dateViewList.AppendTextColumn(str(col[0]), width=wx.COL_WIDTH_AUTOSIZE, mode=wx.dataview.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_RIGHT, flags=wx.dataview.DATAVIEW_COL_RESIZABLE)
        elif column_type == datetime.datetime:
            dateViewList.AppendTextColumn(col[0], width=wx.COL_WIDTH_AUTOSIZE, mode=wx.dataview.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT, flags=wx.dataview.DATAVIEW_COL_RESIZABLE)
   # 숫자컬럼을 오른쪽 정렬이 필요 없으면 
   # 아래 2라인의 주석을 해제하고 사용 대신 위 for 문은 사용하지 않는다.
   # 그리고 org.vision.wxoracle.oraclePool.py 를 사용할 필요가 없어진다. 
   # for col_name in col_names:
   #     dateViewList.AppendTextColumn(col_name)
 
   # Populate output list with results
   for row in rows: # 
       # convert each element in row to str
       row_str = [str(val) for val in row] #
       dateViewList.AppendItem(row_str) # row_str은 한 줄의 정보 오라클 투플을 말한다.

   # Close database connection
   cursor.close() # 커서 닫고
   connection.close() # 커넥션 닫는다. 한 번 만들어 놓으면, 파이썬으로 디비 작업하는 사람은 항상 불러서 사용한다. 공통 모듈 등 다양한 이름으로 이것을 부른다.

def getRenderingData(dateViewList): # 렌더링된 데이터를 얻어 온다.
    # 컬럼 이름 리스트 생성(필요할때 사용하세요) 
    col_names = [] # col_name이라는 빈 리스트를 선언한다.
    for col in range(dateViewList.GetColumnCount()): # 컬럼이 5라면, range는 6을 준다.
        col_names.append(dateViewList.GetColumn(col).GetTitle()) # 컬럼은 객체이다. 객체가 가지고 있는 타이틀을 얻어온다. 타이틀은 문자열이다. colnames에 문자열이 담긴다.
  
    # 데이타 리스트 생성
    data = [] # data에 빈 리스트를 선언한다.
    for row in range(dateViewList.GetItemCount()): # item이 총 몇 개인지 센다.
        row_data = [] # row_data라는 빈 리스트를 만든다.
        for col in range(dateViewList.GetColumnCount()): # 숫자를 하나씩 제너레이트한다.
            item = dateViewList.GetTextValue(row, col) # row는 숫자이다. col도 숫자이다. 처음에는 row단위로 반복하고, 다음은 col단위로 반복한다. 
            row_data.append(item)
        data.append(row_data)
        
    # 결과 출력
    for row in data:
        print(row)

    return data