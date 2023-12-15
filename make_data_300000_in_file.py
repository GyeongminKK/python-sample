import random
from datetime import datetime,timedelta

def makefile():
    group_name = random.randint(1000000,2000000)
    name = random.randint(1000,9999)
    score = random.randint(0,100)
    input_date = datetime(2023,12,1) + timedelta(days=random.randint(0,30))
    formatted_date = input_date.strftime('%Y-%m-%d')
    return f"{group_name},{name},{score},{formatted_date}\n"


if __name__ == "__main__" :
    file_path = 'E:\python-sample-github\\'
    file_name = 'data_300000'

    with open(file_path + file_name, 'w') as fd:
        data_list = [makefile() for _ in range(300000)]
        fd.writelines(data_list)


