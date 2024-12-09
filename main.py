from mysql.connector import connect

def main() -> None:
    conn = connect(user="root", password="", host="localhost", database="teste")
    curr = conn.cursor()

    curr.execute("SELECT * FROM user")

    for data in curr:
        print(data)

if(__name__ == "__main__"):
    main()