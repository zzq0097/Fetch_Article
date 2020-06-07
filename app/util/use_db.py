import pymysql

conn = pymysql.connect(
    host='122.51.73.146',
    user='root',
    password='zzq123456',
    db='test',
    use_unicode=True,
    charset='utf8'
)
cursor = conn.cursor(pymysql.cursors.DictCursor)


def insert_article(entity):
    cursor.execute('')
    return cursor.fetchall()


def select_rule(web_name):
    cursor.execute('select * from rule where web_name = %s', web_name)
    return cursor.fetchall()

