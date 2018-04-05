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
        print "laco"
        stmt = "SELECT email from usuarios where time="+"'"+time+"'"
        result_proxy = session.execute(stmt)
        result = result_proxy.fetchall()
        if result:
            print result
            validate = True
        else:
            validate = False
        if not validate:
            print "entrei"
            stmt = 'INSERT INTO usuarios(email, subject, time) VALUES(+'+'"'+email+'","'+subject+'","'+time+'")'
            try:
                result_proxy = session.execute(stmt)
                if 'INSERT' in stmt or 'UPDATE' in stmt or 'DELETE' in stmt:
                    session.commit()
                    return True

                if 'SELECT' in stmt:
                    result = result_proxy.fetchall()
                    return result

            except Exception as e:
                print  e
                if '_mysql_exceptions.IntegrityError' in str(e):
                    return "Already here"

                else:
                    return False
        else:
            print "This email sent by "+ str(result[0]) + " is already in database"
