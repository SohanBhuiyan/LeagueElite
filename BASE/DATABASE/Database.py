import mysql.connector

class Database:

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Bhuiyan2",
        database="leaguedb"
    )

    if mydb.is_connected():
        print("Database connected")

    mycursor = mydb.cursor()


    def insert_into_profile_table(self, summonername, summonerId, tier):
        sqlStmt = "INSERT INTO profiles (summonerId,summonername,tier) VALUES (%s,%s, %s)"
        params = (summonerId,summonername, tier)
        self.mycursor.execute(sqlStmt, params)
        self.mydb.commit()

    def insert_into_champion_mastery_table(self, summonername, score, champId):
        sqlStmt = "INSERT INTO champion_mastery (summonername,score,champId) VALUES (%s,%s, %s)"
        params = (summonername,score, champId)
        self.mycursor.execute(sqlStmt, params)
        self.mydb.commit()

    def select(self, command):
        self.mycursor.execute("SELECT " + command)
        results = self.mycursor.fetchall()
        """for result in results:
            print(result)"""
        return results

    def delete(self, command): #eg. "DELETE FROM customers WHERE address = 'Mountain 21'"
        self.mycursor.execute("DELETE " + command)
        self.mydb.commit()



