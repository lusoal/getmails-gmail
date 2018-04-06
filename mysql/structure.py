from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy_utils import database_exists, create_database

def create_structure(user,password,host):
    engine = create_engine("mysql://"+user+":"+password+"@"+host+"/gmailusers")
    if not database_exists(engine.url):
        create_database(engine.url)
        # print(database_exists(engine.url))
        #creating session
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        sql = "CREATE TABLE usuarios(id int not null primary key auto_increment, email varchar(100) not null, subject varchar(30) not null, time varchar(30) not null)"
        result_proxy = session.execute(sql)
        session.commit()
        print "Structure Created"
    else:
        print "Database Already Exists"
