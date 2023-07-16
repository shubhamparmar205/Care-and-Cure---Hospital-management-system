import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
)

print("DATABASE CONNECTION SUCCESSFUL")

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS PATIENT")
c.execute("""
    CREATE TABLE PATIENT (
        PATIENT_ID INT(10) PRIMARY KEY,
        NAME VARCHAR(20) NOT NULL,
        SEX VARCHAR(10) NOT NULL,
        BLOOD_GROUP VARCHAR(5) NOT NULL,
        DOB DATE NOT NULL,
        ADDRESS VARCHAR(100) NOT NULL,
        CONSULT_TEAM VARCHAR(50) NOT NULL,
        EMAIL VARCHAR(20) NOT NULL
    )
""")
print("PATIENT TABLE CREATED SUCCESSFULLY")

c.execute("DROP TABLE IF EXISTS CONTACT_NO")
c.execute("""
    CREATE TABLE CONTACT_NO (
        PATIENT_ID INT(10) PRIMARY KEY,
        CONTACTNO INT(15) NOT NULL,
        ALT_CONTACT INT(15),
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
    )
""")
print("CONTACT_NO TABLE CREATED SUCCESSFULLY")

c.execute("DROP TABLE IF EXISTS EMPLOYEE")
c.execute("""
    CREATE TABLE EMPLOYEE (
        EMP_ID VARCHAR(10) PRIMARY KEY,
        EMP_NAME VARCHAR(20) NOT NULL,
        SEX VARCHAR(10) NOT NULL,
        AGE INT(5) NOT NULL,
        DESIG VARCHAR(20) NOT NULL,
        SAL INT(10) NOT NULL,
        EXP VARCHAR(100) NOT NULL,
        EMAIL VARCHAR(20) NOT NULL,
        PHONE INT(12)
    )
""")
print("EMPLOYEE TABLE CREATED SUCCESSFULLY")

c.execute("DROP TABLE IF EXISTS TREATMENT")
c.execute("""
    CREATE TABLE TREATMENT (
        PATIENT_ID INT(10) PRIMARY KEY,
        TREATMENT VARCHAR(100) NOT NULL,
        TREATMENT_CODE VARCHAR(30) NOT NULL,
        T_COST INT(20) NOT NULL,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
    )
""")
print("TREATMENT TABLE CREATED SUCCESSFULLY")

c.execute("DROP TABLE IF EXISTS MEDICINE")
c.execute("""
    CREATE TABLE MEDICINE (
        PATIENT_ID INT(10) PRIMARY KEY,
        MEDICINE_NAME VARCHAR(100) NOT NULL,
        M_COST INT(20) NOT NULL,
        M_QTY INT(10) NOT NULL,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
    )
""")
print("MEDICINE TABLE CREATED SUCCESSFULLY")

c.execute("DROP TABLE IF EXISTS ROOM")
c.execute("""
    CREATE TABLE ROOM (
        PATIENT_ID INT(10) NOT NULL,
        ROOM_NO VARCHAR(20) PRIMARY KEY,
        ROOM_TYPE VARCHAR(10) NOT NULL,
        RATE INT(10) NOT NULL,
        DATE_ADMITTED DATE,
        DATE_DISCHARGED DATE NULL,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
    )
""")
print("ROOM TABLE CREATED SUCCESSFULLY")

c.execute("DROP TABLE IF EXISTS APPOINTMENT")
c.execute("""
    CREATE TABLE APPOINTMENT (
        PATIENT_ID INT(20) NOT NULL,
        EMP_ID VARCHAR(10) NOT NULL,
        AP_NO VARCHAR(10) PRIMARY KEY,
        AP_TIME TIME,
        AP_DATE DATE,
        DESCRIPTION VARCHAR(100),
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE,
        FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE (EMP_ID)
    )
""")
print("APPOINTMENT TABLE CREATED SUCCESSFULLY")

conn.commit()
conn.close()