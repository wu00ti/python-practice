#-*- coding:UTF-8 -*-

import uuid
import pymysql

def generaterActivationCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-','').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-','').upper()
        codeList.append(code)

    return codeList

def storeInMysql(codelist):
    try:
        conn = pymysql.connect(host = 'localhost',user='root',passwd='ourselec',db='mysql')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            
            cur.execute('USE activation_code')
            
            for code in codelist:
                cur.execute('INSETR INTO code1(code VALUES',(code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    storeInMysql(generaterActivationCode(200))
    print('OK!')
