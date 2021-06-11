from utl.database import DataBase


def main():
    db = DataBase()
    data = db.exec_sql("get_data")
    # do something next 

if __name__ == "__main__":
    main()
 