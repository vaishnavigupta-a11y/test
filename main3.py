# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel
# class dictt(BaseModel):
#     username: str
#     rollnumber: int
#     password: str

# app=FastAPI()

# alldata=[]
# index=1

# @app.get("/")
# def home():
#     return {"message":"welcome to api world"}

# @app.get("/about")
# def about():
#     return {"message":"hello cutie this is about page"}

# @app.get("/get")
# def gettingalldata():
#     return alldata
# @app.get("/get/{id}")
# def gettingparticulardata(id:int):
#     for data in alldata:
#         if data["id"]==id:
#             return data
#     raise HTTPException(status_code=404,detail=f'no user found with user id {id}')
# @app.post("/post")
# def postingdata(p:dictt):
#     post=p.dict()
#     global index
#     post["id"]=index
#     index=index+1
#     alldata.append(post)
#     return {"message":"data addesd successfully"}
#     # alldata.add(post)
#     # for data in alldata:
#     #     data["username"]=post["username"]
#     #     data["rollnumber"]=post["rollnumber"]
#     #     data["password"]=post["password"]
#     #     alldata.add(data)
#     #     return {"message":"data added successfully"}
#     #porblem
# @app.put("/put/")
# def updatingwholedetail(id:int,p:dictt):
#     post=p.dict()
#     for data in alldata:
#         if data["id"]==id:
#             data["username"]=post["username"]
#             data["rollnumber"]=post["rollnumber"]
#             data["password"]=post["password"]
#             return { "message":"successfully updated data"}
#     raise HTTPException(status_code=404,detail=f'not found element with id {id}')

# @app.patch("/patch/{id}")
# def updatingpartialdetail(id:int,p:dictt):
#     post=p.dict()
#     for data in alldata:
#         if data["id"]==id:
#             if "username" in post:
#                 data["username"]=post["username"]
#             if "password" in post:
#                 data["password"]=post["password"]
#             if "rollnumber" in post:
#                 data["rollnumber"]=post["rollnumber"]
#             return {"message":"data updated successfully"}
      
#     raise HTTPException(status_code=404,detail=f'no user found with user id {id} so no partial updation is possible')

# @app.delete("/delete/{id}")
# def deleting(id:int):
#     for data in alldata:
#         if data["id"]==id:
#             alldata.remove(data)
#             return{"message":"successsfully deleted data yuhu!!"}
#     raise HTTPException(status_code=404,detail=f'user with that spefic user id {id} is not found in databse')

   
print("1")
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi import Depends
from database import Sessionlocal
from models import User
from sqlalchemy.orm import Session
import models
from database import engine
print("2")
# models.Base.metadata.create_all(bind=engine) — What It Means

# This one line tells SQLAlchemy:

# “Create the tables in the database based on my models.”
models.Base.metadata.create_all(bind=engine)
print("3")
# 4. Dependency (Depends) — Auto-Provide the DB Session
def get_db(): #each andd verytime when we want to exacute a query as sessional db is made which hep of thatthing we execute or apply quurye like
    # t stoe data in db eeveytime we use to buy new pen mnaully and then close that pen
    db=Sessionlocal()
    try:
       yield db
    finally:
        db.close()

class dictt(BaseModel):
    username: str
    rollnumber: int
    password: str

# soecuallyfor patch where allfileds are optional#
class PatchUser(BaseModel):
    username: str | None = None
    password: str | None = None
    rollnumber: int | None = None

app=FastAPI()
# print("3")
# alldata=[] #data stoed for temo so afeter refersh it loast
# index=1

@app.get("/")
def home():
    return {"message":"welcome to api world"}
print("4")
@app.get("/about")
def about():
    return {"message":"hello cutie this is about page"}
print("5")
# @app.get("/get")
# def gettingalldata():
#     return alldata
@app.get("/get")
def gettingalldata(db:Session=Depends(get_db)):
        # users = db.query(models.User).all()  # WHY? → SELECT * FROM userdetails
#dq.query means apply qurye 
# models.user emans on unser table presnte in models 
# .all means returning all data or we can say that all rows

    user=db.query(models.User).all()
    return user

print("6")
# @app.get("/get/{id}")
# def gettingparticulardata(id:int):
#     for data in alldata:
#         if data["id"]==id:
#             return data
#     raise HTTPException(status_code=404,detail=f'no user found with user id {id}')
@app.get("/get/{rollnumber}")
def gettingparticulardata(rollnumber:int, db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.rollnumber==rollnumber).first()
    if not user:
       raise HTTPException(status_code=404,detail=f'no user found with rollnu,mber {rollnumber}')
    return user



print("7")
# @app.post("/post")
# def postingdata(p: dictt, db: Session = Depends(get_db)):
#     new_user = models.User(
#         username=p.username,
#         password=p.password,
#         rollnumber=p.rollnumber
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return {"message": "data added successfully"}


@app.post("/post")
def postingdata(p:dictt,db:Session=Depends(get_db)):
    new_user=models.User( #new_user is model object like row data
        username=p.username,
        password=p.password,
        rollnumber=p.rollnumber
    )
    db.add(new_user) #user addesd in session for temp,rollbaxk is also possible
    db.commit() #user addd in adaded cimmited in database for perfmanant
    db.refresh(new_user) #the user dta is regfrsh so that some attribute default like id etc which is addd y serve ritslef is corrcet
    return {"message":"data added successfully"}
    # post=p.dict()
    # global index
    # post["id"]=index
    # index=index+1
    # alldata.append(post)
    # return {"message":"data addesd successfully"}

print("8")
# @app.post("/post")
# def postingdata(p:dictt):
#     post=p.dict()
#     global index
#     post["id"]=index
#     index=index+1
#     alldata.append(post)
#     return {"message":"data addesd successfully"}
    # alldata.add(post)
    # for data in alldata:
    #     data["username"]=post["username"]
    #     data["rollnumber"]=post["rollnumber"]
    #     data["password"]=post["password"]
    #     alldata.add(data)
    #     return {"message":"data added successfully"}
    #porblem
# @app.put("/put/")
# def updatingwholedetail(id:int,p:dictt):
#     post=p.dict()
#     for data in alldata:
#         if data["id"]==id:
#             data["username"]=post["username"]
#             data["rollnumber"]=post["rollnumber"]
#             data["password"]=post["password"]
#             return { "message":"successfully updated data"}
#     raise HTTPException(status_code=404,detail=f'not found element with id {id}')
@app.put("/put/")
def updatingwholedetail(rollnumber:int,p:dictt,db: Session=Depends(get_db)):
    # post=p.dict()
    user=db.query(models.User).filter(models.User.rollnumber==rollnumber).first()
    if not user:
        raise HTTPException(status_code=404,detail=f'user not found with roll number{rollnumber}')
    
    user.username=p.username
    user.rollnumber=p.rollnumber
    user.password=p.password
    db.commit()
    db.refresh(user)
    # )
    return {"message":"successfully updated whole data"}
print("9")
# @app.patch("/patch/{id}")
# def updatingpartialdetail(id:int,p:dictt):
#     post=p.dict()
#     for data in alldata:
#         if data["id"]==id:
#             if "username" in post:
#                 data["username"]=post["username"]
#             if "password" in post:
#                 data["password"]=post["password"]
#             if "rollnumber" in post:
#                 data["rollnumber"]=post["rollnumber"]
#             return {"message":"data updated successfully"}
      
#     raise HTTPException(status_code=404,detail=f'no user found with user id {id} so no partial updation is possible')
@app.patch("/patch/{rollnumber}")
def updatingpartialdetail(rollnumber:int,p:PatchUser,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.rollnumber==rollnumber).first()
    if not user:
        raise HTTPException(status_code=404,details=f'no user found with rollnumber{rollnumber} so sorry but no partial update can be possible')
    if p.username:
        user.username=p.username
    if p.rollnumber:
        user.rollnumber=p.rollnumber
    if p.password:
        user.password=p.password
    db.commit()
    return {"message":"data partially updated successfully"}
      
print("10")
# @app.delete("/delete/{id}")
# def deleting(id:int):
#     for data in alldata:
#         if data["id"]==id:
#             alldata.remove(data)
#             return{"message":"successsfully deleted data yuhu!!"}
#     raise HTTPException(status_code=404,detail=f'user with that spefic user id {id} is not found in databse')
@app.delete("/delete/{rollnumber}")
def deleting(rollnumber:int,db :Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.rollnumber==rollnumber).first()
    if not user:
        raise HTTPException(status_code=404,detail=f'no user foudn with rollnumber(rollnumber so no need of deletion)')
    # db.query(models.User).delete(user)
    db.delete(user)

    db.commit()
    return {"message":"data with rollnumber {rollnumber} deleted succesfully"}

      
    
print("11")

    

