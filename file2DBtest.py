import pyodbc
from datetime import datetime

def insert_data(group_list,name_list,score_list,date_list):
    dsn = 'tibero_local'
    user = 'sscs'
    password = 'sscs'    
    try:
        conn = pyodbc.connect(DSN=dsn, uid=user, pwd=password)
        print("Tibero에 성공적으로 연결되었습니다.")
        cursor = conn.cursor()
        '''
        한번에 한 줄씩 insert하는 코드
        for group_name, name, score, input_date in zip(group_list, name_list, score_list, date_list):
            input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
            cursor.execute('INSERT INTO TEST_TABLE (KEY, GROUP_NAME, NAME, SCORE, INPUT_DATE) VALUES (SEQ_TEST_TABLE.NEXTVAL, ?, ?, ?, ?)',
                           ( group_name, name, int(score), input_date))
        '''
        '''
        python executemany를 사용하여 시간 단축
        '''
        data = list(zip(group_list, name_list, score_list, map(lambda x: datetime.strptime(x, '%Y-%m-%d').date(), date_list)))
        cursor.executemany('INSERT INTO TEST_TABLE (KEY, GROUP_NAME, NAME, SCORE, INPUT_DATE) VALUES (SEQ_TEST_TABLE.NEXTVAL, ?, ?, ?, ?)', data)

        conn.commit()  # 변경 내용 커밋
        print("Tibero에 성공적으로 Insert 했습니다.")  
    except pyodbc.Error as ex:
        print("Tibero 연결 중 오류가 발생했습니다:", ex)    

def start_process():
    file_path = 'E:\python-sample-github\data_300000'
    group_list = []
    name_list = []
    score_list = []
    date_list = []
    with open(file_path, 'r') as fd:
        for line in fd:
            group_name, name, score, input_date = line.strip().split(',')            
            group_list.append(group_name)
            name_list.append(name)
            score_list.append(score)
            date_list.append(input_date)    
    insert_data(group_list,name_list,score_list,date_list)    

if __name__ == "__main__" :
    start_process()