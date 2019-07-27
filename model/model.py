# -----------------------------------------------+
# Diving Class Custom Model                      +
# Flask Microframework - Accalina                +
# -----------------------------------------------+

# IMPORT ----------------------------------------+
import mysql.connector                  # connector for mysqls
import bcrypt                           # for secure hashing algoritm
import random

class Model:

    # AUTHENTICATION ----------------------------------------------------------------------------------+
    def register(self, username, password, fullname):
        """ 
        Create user data 
        
        Param:
        - username (str)
        - password (str)

        Return:
        - response (str) : a status response in which the operation is success or failed
        """
        try:

            try:
                db = mysql.connector.connect(       # database config
                    host="localhost",
                    user="root",
                    passwd="",
                    database="db_divingclass"
                )
                cursor = db.cursor(dictionary=True)
            except mysql.connector.errors.InterfaceError as e:
                print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
                import sys; sys.exit()


            # Generate Hash Password
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw( password.encode("utf-8"), salt )
            password = hashed.decode("utf-8")

            # Insert user account to Database
            sql = "INSERT INTO login (username, password, fullname, level) VALUES (%s,%s,%s,%s)"
            val = (username, password, fullname, 1)
            cursor.execute(sql, val)            
            db.commit()

            # Get User id
            cursor.execute(f"SELECT * FROM login WHERE username='{username}'" )
            result = cursor.fetchall()
            userid = result[0]['userid']

            # Insert Subscription info to Database
            subname = ['bab1', 'bab2', 'bab3', 'bab4', 'bab5', 'bab6', 'final']
            for item in subname:
                subsql = "INSERT INTO module_access (`userid`, `module`, `active`, `payment`) VALUES (%s,%s,%s,%s)"
                subvalue = (userid, item, 0, "...")
                cursor.execute(subsql, subvalue)
            db.commit()


            return "User %s has been created" % username
        except:
            return "Failed to create user %s" % username

    def login(self, username, password):
        """ 
        Check user credential 
        
        Param:
        - username (str)
        - password (str)

        Return:
        - (bool)
        """

        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)
        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            import sys
            sys.exit()

        # Get User Data
        cursor.execute(f"SELECT * FROM login WHERE username='{username}'" )
        result = cursor.fetchall()
        if len(result) == 1:
            # Check if Password Match
            if bcrypt.checkpw(password.encode(), result[0]['password'].encode()):
                return result # Return user data
            else:
                return False # Invalid Password
        else:
            return False # User not found


    # PROCESS USER DATA -------------------------------------------------------------------------------+
    def generateSoal(self, bab):
        """ 
        To randomize option and question every time 
        
        Param:
        - bab (str): a string of bab name e.g. bab1

        Return:
        - daftarSoal (list): a list of soal which has been randomize
        """

        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)
        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            import sys
            sys.exit()

        sql = "SELECT * FROM questions WHERE module = '{}'".format(bab)
        cursor.execute(sql)
        hasil = cursor.fetchall()

        daftarSoal = []
        for row in hasil:
            pertanyaan  = row['question']
            jawaban     = row['ans']
            opsi        = [ row['opt1'], row['opt2'], row['opt3'], row['opt4'] ]
            acakOpsi    = random.sample(opsi, 4)
            daftarSoal.append([pertanyaan, jawaban, acakOpsi])

        daftarSoal = random.sample(daftarSoal, 10)
        return daftarSoal


    def comparing(self, soal, jawab):
        """ 
        To compare soal and jawaban and get the score 
        
        Param:
        - soal (dict): a dictionary of soal
        - jawaban (dict): a dictionary of jawaban

        Return:
        - score (int): a solid score after comparation
        - wrongAns (list): a list of answer who failed to compare
        """

        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)
        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            import sys
            sys.exit()

        nilai = 0
        wrongAns = []
        for i in range(1,11):
            # Convert i into str to allow data processing
            i = str(i)

            # Checking for soal
            sql = "SELECT * FROM questions WHERE question = '{}'".format(soal[i])
            cursor.execute(sql)
            ans = cursor.fetchall()
            ans = ans[0]['ans']
            
            # Comparing answer and user input
            if ans == jawab[i]:
                nilai += 1
            else:
                wrongAns.append({'soal': soal[i], 'yourAns': jawab[i], 'dbAns': ans})
        return str(nilai), wrongAns

    # PAYMENT AND SERVICES ----------------------------------------------------------------------------+

    def subscription(self, userid):

        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)
        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            import sys
            sys.exit()

        sql = "SELECT * FROM module_access WHERE userid = '{}'".format( userid )
        cursor.execute(sql)
        userdata = cursor.fetchall()
        return userdata
        
    def getModule(self, userid):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)
        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            import sys
            sys.exit()

        sql = "SELECT * FROM `module_access` as a right join resource as b on a.module = b.module where a.userid = '{}'".format(userid)
        cursor.execute(sql)
        userdata = cursor.fetchall()
        return userdata

# RUN -------------------------------------------+
if __name__ == "__main__":
    m = Model()
    result = m.login("accalina","accalina")
    print(result)

# END -------------------------------------------+

# cursor.rowcount
