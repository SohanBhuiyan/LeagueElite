from BASE.User import User
import mysql.connector
from BASE.ProPlayerFinder import *

class DatabaseService:


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Bhuiyan2",
        database="leaguedb"
    )

    if mydb.is_connected():
        print("Database connected")

    mycursor = mydb.cursor()


    def insertIntoProfile(self,summonername,tier):
        sql = "INSERT INTO profiles (summonername,tier) VALUES (%s, %s)"
        val = (summonername, tier)
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")


    def select(self, command):
        self.mycursor.execute("SELECT " + command)
        results = self.mycursor.fetchall()
        for result in results:
            print(result)

    def delete(self, command): #eg. "DELETE FROM customers WHERE address = 'Mountain 21'"
        self.mycursor.execute("DELETE " + command)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) deleted")




db = DatabaseService()
db.delete("FROM profiles WHERE tier = 'silver'")
db.select("SELECT * FROM profiles")
