# -----------------------------------------------+
# Diving Class Custom Model                      +
# Flask Microframework - Accalina                +
# -----------------------------------------------+

# IMPORT ----------------------------------------+
import mysql.connector                  # connector for mysqls
import bcrypt                           # for secure hashing algoritm
import random
import sys

class Model:

    # AUTHENTICATION ----------------------------------------------------------------------------------+
    def register(self, username, password, fullname, admin=False):
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
                sys.exit()

            # Generate Hash Password
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw( password.encode("utf-8"), salt )
            password = hashed.decode("utf-8")

            if admin == False: # Check for admin creation
                # Insert user account to Database
                sql = "INSERT INTO login (username, password, fullname, level) VALUES (%s,%s,%s,%s)"
                val = (username, password, fullname, 1)
                cursor.execute(sql, val)
                db.commit()

                # Get User id
                cursor.execute(f"SELECT * FROM login WHERE username='{username}'" )
                result = cursor.fetchall()
                userid = result[0]['userid']
                subname = ['bab1', 'bab2', 'bab3', 'bab4', 'bab5', 'bab6', 'final']

                # Insert Subscription info to Database
                for item in subname:
                    subsql = "INSERT INTO module_access (`userid`, `module`, `active`, `payment`) VALUES (%s,%s,%s,%s)"
                    subvalue = (userid, item, 0, "...")
                    cursor.execute(subsql, subvalue)
                db.commit()

                # Insert Scoring info to Database
                for item in subname:
                    scoresql = "INSERT INTO scores (`userid`, `module`, `testscore`) VALUES (%s,%s,%s)"
                    scorevalue = (userid, item, 0)
                    cursor.execute(scoresql, scorevalue)
                db.commit()
            else:
                # Insert user account to Database
                sql = "INSERT INTO login (username, password, fullname, level) VALUES (%s,%s,%s,%s)"
                val = (username, password, fullname, 9)
                cursor.execute(sql, val)
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

    def saveScore(self, userid, bab, score):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            try:
                sql = "UPDATE `scores` SET testscore=%s WHERE userid = %s AND module = %s"
                val = (score, userid, bab)
                cursor.execute(sql, val)
                db.commit()
                return True
            except:
                return False

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()

    def getUserScore(self, userid):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            sql = "SELECT * FROM `scores` WHERE userid = '{}'".format(userid)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()

    def updateProfile(self, userid, username, fullname):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            try:
                sql = "UPDATE `login` SET username=%s, fullname=%s  WHERE userid = %s"
                val = (username, fullname, userid)
                cursor.execute(sql, val)
                db.commit()
                return True
            except:
                return False

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()
    

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
            sys.exit()

        sql = "SELECT * FROM `module_access` as a right join resource as b on a.module = b.module where a.userid = '{}'".format(userid)
        cursor.execute(sql)
        userdata = cursor.fetchall()
        return userdata

    def buyModule(self, userid, module, filename):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            try:
                sql = "UPDATE `module_access` SET payment=%s WHERE userid = %s AND module = %s"
                val = (filename, userid, module)
                cursor.execute(sql, val)
                db.commit()
                return True
            except:
                return False

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()

    def checkPreviousScore(self, userid, currentbab):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            bablist = ['bab1','bab2', 'bab3', 'bab4', 'bab5', 'bab6', 'final']
            mybab = (bablist.index(currentbab)) - 1
            mybab = bablist[mybab]
            sql = "SELECT * FROM scores WHERE userid = '{}' AND module = '{}'".format(userid, mybab)
            cursor.execute(sql)
            userdata = cursor.fetchall()
            previousNilai = str(userdata[0]['testscore'])
            if previousNilai != "0" and int(previousNilai) >= 7:
                return True
            else:
                return False

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()

        


    # PROCESS ADMIN DATA ------------------------------------------------------------------------------+

    def getAdminInfo(self):
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
            sys.exit()
        
        # Get Userlist
        sql = "SELECT * FROM login WHERE level != 9"
        cursor.execute(sql)
        userlist = cursor.fetchall()

        sql = "SELECT * FROM login WHERE level = 9"
        cursor.execute(sql)
        adminlist = cursor.fetchall()

        return userlist, adminlist

    def getUnverifiedPayment(self):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            # Get Userlist
            sql = "SELECT a.no, b.username ,a.module, a.active, a.payment FROM module_access as a left join login as b on a.userid = b.userid WHERE a.payment != '...' AND a.active = '0'"
            cursor.execute(sql)
            paymentlist = cursor.fetchall()
            return paymentlist

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()

    def verified(self, userid):
        try:
            db = mysql.connector.connect(       # database config
                host="localhost",
                user="root",
                passwd="",
                database="db_divingclass"
            )
            cursor = db.cursor(dictionary=True)

            try:
                sql = "UPDATE module_access SET active=1 WHERE no = {}".format(userid)
                cursor.execute(sql)
                db.commit()
                return True
            except:
                return False

        except mysql.connector.errors.InterfaceError as e:
            print("Mysql is not connected, Please start the mysql on XAMPP Control Panel")
            sys.exit()
        



# RUN -------------------------------------------+
if __name__ == "__main__":
    m = Model()
    print("Admin creation system v1.0 \n")
    fullname = input("Fullname: ")
    username = input("Username: ")
    password = input("Password: ")
    result = m.register(username, password, fullname, True)
    print(result)

# END -------------------------------------------+

# cursor.rowcount
