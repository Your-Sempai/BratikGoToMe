import pymysql


def get_connection():
    con = pymysql.connect(
                                 host="remotemysql.com",
                                 port=3306,
                                 user="Wj94Ebbibp",
                                 passwd="2FuLXlXEnH",
                                 db="Wj94Ebbibp"
                                )
    return con