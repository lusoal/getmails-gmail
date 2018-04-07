from sqlalchemy import *
from sqlalchemy.orm import *

def connect_to_db(host, user, password, db):
    #connection db
    try:
        engine = create_engine("mysql://"+user+":"+password+"@"+host+"/"+db)
        #creating session
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        return session
    except:
        return False

def insert_emails(session, time, email, subject):
    validate = validate_email(session, time)
    if session:
        if validate:
            insert = 'INSERT INTO usuarios(email, subject, time) VALUES('+'"'+email+'","'+subject+'","'+str(time)+'")'
            try:
                result_proxy = session.execute(insert)
                session.commit()
                print "New email added "+email
            except Exception as e:
                print e


def validate_email(session, time):
    if session:
        select = "SELECT email from usuarios where time="+"'"+str(time)+"'"
        result_proxy = session.execute(select)
        result = result_proxy.fetchall()
        if result:
            print "This mail "+str(result)+ " is already on database"
            return False
        else:
            return True
    else:
        return False
