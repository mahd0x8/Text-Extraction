import ast
import psycopg2
from configparser import ConfigParser

# function to read database configuration file
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


# //////////////////////////////////////////////

# get database details from configuration file
dbDet = config()

# connect to the database
conn = psycopg2.connect(
    host=dbDet['host'],
    database=dbDet['database'],
    user=dbDet['user'],
    password=dbDet['password']
)
cursor = conn.cursor()

# list of keys for each section of the form
impKeys = [
    ['Title', 'Name' ,'School / Dept', 'UOA', 'Research Centre / Institute'],
    ['Primary Institution', 'Participating Dept / Faculty', 'Ranking Times / QS', 'Key Contact (Name and title)', 'Research interest', 'Participating Institutions'],
    ['Description of planned Activity', "Collaboration's sustainability and strength", 'Risk Factors / Mitigation (Max. 100 words)'],
    ['Planned Date 3* / VA /RF / O Description', 'Do you wish to use this fund to support incoming visits to Huddersfield?', 'Are you exploring Horizon Europe / Newton / Global Challenge funding'],
    ['Funds requested and how to be spent Spending profile', 'SCHOOL SIGN OFF Dean / AD', 'Support', 'Sch. Rank', 'Comments']
]

# list of section headers
DataHeader = ['LEAD ACADEMIC', 'COLLABORATING INTERNATIONAL INSTITUTION/S', 'THE COLLABORATION', 'OUTPUTS', 'BUDGET', 'Additional Background Information']

# /////////////////////////////////////////////


# function to create tables in the database
def createDatabaseTables():
    try:
        sql = '''CREATE TABLE PERSON(
           PNAME CHAR(200) NOT NULL,
           Background CHAR(1200),
           PID SERIAL PRIMARY KEY
        )'''
        cursor.execute(sql)
    except:
        pass

    try:
        sql = '''CREATE TABLE ACADEMIC(
           Title CHAR(30) NOT NULL,
           Pname CHAR(100),
           School CHAR(300),
           UOA CHAR(300),
           Institute CHAR(300),
           AID INT PRIMARY KEY
        )'''
        cursor.execute(sql)
    except:
        pass

    try:
        sql = '''CREATE TABLE INTERNATIONAL_INSTITUTION(
           PrimaryIns CHAR(1300) NOT NULL,
           Participating CHAR(1300),
           Ranking CHAR(1300),
           Contact CHAR(1300),
           interest CHAR(1300),
           Institutions CHAR(1300),
           IIID INT PRIMARY KEY
        )'''
        cursor.execute(sql)
    except:
        pass

    try:
        sql = '''CREATE TABLE COLLABORATION(
           planned_Activity CHAR(1000),
           Risk_Factors CHAR(1000),
           Collaboration_matrics CHAR(1000),
           CID INT PRIMARY KEY
        )'''
        cursor.execute(sql)
    except:
        pass

    try:
        sql = '''CREATE TABLE OUTPUTS(
           O_planning CHAR(1000),
           tosupport CHAR(1000),
           exploring CHAR(1000),
           OID INT PRIMARY KEY
        )'''
        cursor.execute(sql)
    except:
        pass

    try:
        sql = '''CREATE TABLE BUDGET(
           B_planning CHAR(1200),
           SCHOOL_SIGN CHAR(1000),
           Support CHAR(1000),
           Rank CHAR(1000),
           Comments CHAR(1000),
           BID INT PRIMARY KEY
        )'''
        cursor.execute(sql)
    except:
        pass

    conn.commit()
    # Closing the connection

def InsertData(dataDictionary):
    cursor.execute('''INSERT INTO PERSON(PNAME, Background) VALUES ('{}', '{}')'''.format(dataDictionary['LEAD ACADEMIC'][0]+" "+dataDictionary['LEAD ACADEMIC'][1],dataDictionary['Additional Background Information'][0]))
    cursor.execute("""select PID from person where pname = '{}';""".format(dataDictionary['LEAD ACADEMIC'][0]+" "+dataDictionary['LEAD ACADEMIC'][1]))
    PID = list(cursor.fetchall()[0])[0]

    # ///////////////////////
    cursor.execute('''INSERT INTO ACADEMIC(AID, Title, PName, School, UOA, Institute) VALUES ({},'{}','{}','{}','{}','{}')'''.format(PID,dataDictionary['LEAD ACADEMIC'][0],dataDictionary['LEAD ACADEMIC'][1],dataDictionary['LEAD ACADEMIC'][2],dataDictionary['LEAD ACADEMIC'][3],dataDictionary['LEAD ACADEMIC'][4]))
    # ///////////////////////
    cursor.execute('''INSERT INTO INTERNATIONAL_INSTITUTION(IIID, PrimaryIns, Participating, Ranking, Contact,interest,Institutions) VALUES ({},'{}','{}','{}','{}','{}','{}')'''.format(PID,dataDictionary['COLLABORATING INTERNATIONAL INSTITUTION/S'][0],dataDictionary['COLLABORATING INTERNATIONAL INSTITUTION/S'][1],dataDictionary['COLLABORATING INTERNATIONAL INSTITUTION/S'][2],dataDictionary['COLLABORATING INTERNATIONAL INSTITUTION/S'][3],dataDictionary['COLLABORATING INTERNATIONAL INSTITUTION/S'][4],dataDictionary['COLLABORATING INTERNATIONAL INSTITUTION/S'][5]))
    # ///////////////////////
    cursor.execute('''INSERT INTO COLLABORATION(CID, planned_Activity, Risk_Factors, Collaboration_matrics) VALUES ({},'{}','{}','{}')'''.format(PID,dataDictionary['THE COLLABORATION'][0],dataDictionary['THE COLLABORATION'][1],dataDictionary['THE COLLABORATION'][2]))
    # ///////////////////////
    cursor.execute('''INSERT INTO OUTPUTS(OID, O_planning, tosupport, exploring) VALUES ({},'{}','{}','{}')'''.format(PID,dataDictionary['OUTPUTS'][0],dataDictionary['OUTPUTS'][1],dataDictionary['OUTPUTS'][2]))
    # ///////////////////////
    cursor.execute('''INSERT INTO BUDGET(BID, B_planning, SCHOOL_SIGN, Support, Rank, Comments) VALUES ({},'{}','{}','{}','{}','{}')'''.format(PID,dataDictionary['BUDGET'][0],dataDictionary['BUDGET'][1],dataDictionary['BUDGET'][2],dataDictionary['BUDGET'][3],dataDictionary['BUDGET'][4]))

    conn.commit()


def GetData(data):
    # This function receives a dictionary of data from the application's form
    # and stores it into the PostgreSQL database.

    dataDictionary = {}  # Initialize an empty dictionary to hold the data

    Keys = list(data.keys())  # Get the keys (field names) from the data dictionary

    # Loop through the first 5 keys (fields)
    for i in range(5):
        lst = []  # Initialize an empty list to hold the data for this field

        temp = []
        # Loop through the values for this field
        for j in data[Keys[i]]:
            temp.append(j)
            # Add the value to the list, removing any bullet points
            lst.append([j, str(data[Keys[i]][j]).replace("\uf0b7", "")])

        # Add the list of values for this field to the data dictionary,
        # stripping any single quotes from the values and converting them
        # to double quotes (for consistency with JSON format)
        dataDictionary[Keys[i]] = [str(k[1]).replace("'", "\"").strip() for k in lst]

    # Add the value for the last key (field) to the data dictionary,
    # removing any bullet points and stripping leading/trailing whitespace
    dataDictionary[Keys[-1]] = [data[Keys[-1]].replace("\uf0b7 ", "").strip()]

    # Call the InsertData function to insert the data into the database
    InsertData(dataDictionary)


def getUserID(name):
    # This function retrieves the user ID (PID) from the database
    # based on the user's name

    # Execute a SELECT query to retrieve the PID for the given name
    cursor.execute("""select pid from person where pname= '{}';""".format(name))

    # Fetch the results and store them in a list
    dta = [x[0] for x in list(cursor.fetchall())]

    # Return the PID
    return (dta[0])

def getUserData(name):
    # get data for the given name from each table
    # id = getUserID(name) # this line is commented out, and is replaced by the next line for testing purposes
    id = name
    dictionary = {}

    # get data from ACADEMIC table
    cursor.execute("""select * from ACADEMIC where aid= '{}';""".format(id))
    ACADEMIC = [str(x).strip() for x in list(cursor.fetchall())[0]][:-1]

    # get data from INTERNATIONAL_INSTITUTION table
    cursor.execute("""select * from INTERNATIONAL_INSTITUTION where iiid= '{}';""".format(id))
    INTERNATIONAL_INSTITUTION = [str(x).strip() for x in list(cursor.fetchall())[0]][:-1]

    # get data from COLLABORATION table
    cursor.execute("""select * from COLLABORATION where cid= '{}';""".format(id))
    COLLABORATION = [str(x).strip() for x in list(cursor.fetchall())[0]][:-1]

    # get data from OUTPUTS table
    cursor.execute("""select * from OUTPUTS where oid= '{}';""".format(id))
    OUTPUTS = [str(x).strip() for x in list(cursor.fetchall())[0]][:-1]

    # get data from BUDGET table
    cursor.execute("""select * from BUDGET where bid= '{}';""".format(id))
    BUDGET = [str(x).strip() for x in list(cursor.fetchall())[0]][:-1]

    # get data from PERSON table
    cursor.execute("""select * from PERSON where pid= '{}';""".format(id))
    PERSON = [str(x).strip() for x in list(cursor.fetchall())[0]][:-1]

    # combine all data into a single list
    dbdata = [ACADEMIC, INTERNATIONAL_INSTITUTION, COLLABORATION, OUTPUTS, BUDGET]

    # convert OUTPUTS[0] and BUDGET[0] from string representation to Python objects
    OUTPUTS[0] = ast.literal_eval(OUTPUTS[0])
    BUDGET[0] = ast.literal_eval(BUDGET[0])

    temp = []
    for i, x in enumerate(impKeys):
        for j, y in enumerate(x):
            try:
                # assign data to dictionary using the corresponding keys in impKeys
                dictionary[impKeys[i][j]] = dbdata[i][j]
            except:
                # if there's an error, print it out
                print("\nERROR\n__________________________ ",impKeys[i][j])
        temp.append(dictionary)
        dictionary = {}

    # combine all dictionaries into a single dictionary
    for i,x in enumerate(DataHeader[:-1]):
        dictionary[x] = temp[i]

    dictionary[DataHeader[-1]] = PERSON[-1]

    return dictionary

def getAllData():
    cursor.execute("""select pname,pid from PERSON""")
    PERSON = [x for x in list(cursor.fetchall())]

    for i in range(len(PERSON)):
        x,y = PERSON[i]
        PERSON[i] = [str(x).strip(),str(y).strip()]

    return (PERSON)

try:
    createDatabaseTables()
except:
    pass

def CloseDatabase():
    conn.close()

