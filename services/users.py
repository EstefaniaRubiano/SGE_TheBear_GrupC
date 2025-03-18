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
    with Session(engine) as session:
        statement = select(User) .where(User.id == id)
        result = Session.exec(statement)
        user = result.one()
        user.email = "abigail@gmail.com"
        Session.add(user)
        Session.commit()
        Session.refresh(user)
        return {"message": "Updated succesfully"}
