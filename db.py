import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect("androidBug.db")
    cursor = conn.cursor()
    tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='bug_table'"
    if not conn.execute(tb_exists).fetchone():
        conn.execute(
            'create table bug_table (id  integer PRIMARY KEY autoincrement, url varchar(100),result varchar(100),description varchar(100),state varchar(20),value integer)')
        conn.commit()
    while True:
        url = input('url:')
        result = input('结果：')
        des = input('描述：')
        state = input('状态：')
        value = input('评价')
        sql = ''' insert into bug_table
              (url,result,description,state,value)
              values
              (:st_url,:st_result,:st_desc,:st_state,:st_value)'''
        cursor.execute(sql,
                       {'st_url': url, 'st_result': result, 'st_desc': des, 'st_state': state, 'st_value': value})
        conn.commit()
        print("=====================================")
