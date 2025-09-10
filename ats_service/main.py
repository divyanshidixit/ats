from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ats_service.schema import Item,SumResponse
from ats_service.models import Base, User
from ats_service.database import engine, SessionLocal


# create tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get('/status')
def status():
    return {"status":"OK"}


@app.post('/sum', response_model=SumResponse)
def sum(item: Item):
    firstval = item.first
    secondval = item.second
    return {'sum':firstval + secondval}

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
