from paths import USER, USER_CLIENT
from sqlite_db__function import SQLiteSensor


db = SQLiteSensor()
if USER ==USER_CLIENT:
    pass
    # UNCOMENT AND  RUN ONCE
    # 1.inital db

    # # 2.create table
    db.create_table()
    # # 3.copy csv
    # #db.csv__to_sqlite()
    #
    # # 4. create table outside
    db.create_table_outside()
    # 4.1. add column to outside
    db.add_column_to_table_outside()
    # 4.2. add column pressure to outside
    db.add_column_pressure__to_table_outside()
    # # 5. create table cpu
    db.create_table_cpu()

    #db.clear_table(db.NAME_TABLE_OUTSIDE)



# just debug if all is stored
#db.print_all_info_from_table()
#.add_column_pressure__to_table_outside()
db.print_all_info_from_table_outside()