import uuid,MySQLdb

def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-',''))
    return key_list

def write_to_mysql(key_list):
    db = MySQLdb.connect("localhost","root","ourselec","mysql",charset='utf8mb4')
    cursor = db.cursor()

    cursor.execute("drop table if exists ukey")

    sql = """create table if not exists ukey(key_value char(40) not null)"""
    cursor.execute(sql)

    try:
        for i in range(200):
            cursor.execute('insert into ukey values("%s")' % (key_list[i]))

        db.commit()
    except:
        db.rollback()

    db.close()

if __name__ == "__main__":
    write_to_mysql(generate_key())
