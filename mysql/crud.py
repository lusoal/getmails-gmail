from sqlalchemy import *
from sqlalchemy.orm import *

def insert_table(host, user, password, db, dicionario):
    validate = ""
    #connection db
    engine = create_engine("mysql://"+user+":"+password+"@"+host+"/"+db)
    #creating session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for time, email, subject in zip(dicionario['Time'],dicionario['Email'],dicionario['Subject']):
        print time, email, subject
        stmt = "SELECT email from usuarios where time="+"'"+time+"'"
        result_proxy = session.execute(stmt)
        result = result_proxy.fetchall()
        print result
        if result:
            validate = True
        else:
            print "nao valido"
            validate = False
        if validate == False:
            print "entrei"
            insert = 'INSERT INTO usuarios(email, subject, time) VALUES('+'"'+email+'","'+subject+'","'+time+'")'
            print insert
            try:
                result_proxy = session.execute(insert)
                session.commit()
            except Exception as e:
                print e

        else:
            print "This email sent by "+ str(result[0]) + " is already in database"
