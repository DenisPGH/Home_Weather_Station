from paths import USER, USER_CLIENT
from sqlite_db__function import SQLiteSensor


db = SQLiteSensor()
if USER ==USER_CLIENT:
    # run once
    # 1.inital db

    # 2.create table
    db.create_table()
    # 3.copy csv
    db.csv__to_sqlite()



# just debug if all is stored
db.print_all_info_from_table()