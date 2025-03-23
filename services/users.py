from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name:str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Created user succesfully"}

async def update_user (id: int, email:str, db: Session):
        statement = select(User) .where(User.id == id)
        result = db.exec(statement)
        user = result.one()
        user.email = email
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"message": "Updated succesfully"}

def delete_user(id:int, db:Session):
    sql_select = select(User).where(User.id == id)
    user_db = db.exec(sql_select).one()

    db.delete(user_db)
    db.commit()
    return {"message":"Deleted user succesfully"}
