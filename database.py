# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker,declarative_base

# DATABASE_URL="postgresql://postgre:vaishnavi@localhost/firstpost"
# engine=create_engine(DATABASE_URL)
# SessionLocal=sessionmaker(autocommit=False,autoflush=False)
# Base=declarative_base()
# from sqlalchemy import create_engine #crete negine store the connecrtion link and use to conncet the databse to the python
# from sqlalchemy.orm import sessionmaker,declarative_base #sessionmaker s use to make a session which is called in every interation or qury exution and declaartive base is user to make a nrml vlas sinto table format all the class who wnatto because a tale inherit the base 
# DATABASE_URL="postgresql://vaihsnavi:vaishnavi@localhost/firstpost" #it store the database connection link
# engine=create_engine(DATABASE_URL)  #shows the connection ansstore connecrion url
# SessionLocal=sessionmaker (autocommit=False,autoflush=False) #session wjhi h is called in every wyry execution
# Base=declarative_base() #base class wich is inherited by all the other claasses who wnat to becasme table







# for main3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
DATABASE_URL="postgresql://vaishnavi:vaishnavi@localhost/firstpostactual"
engine=create_engine(DATABASE_URL)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()