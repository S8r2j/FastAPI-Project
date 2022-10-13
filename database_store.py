from fastapi import FastAPI, Depends
from sqlmodel import create_engine, SQLModel, Session

from schemas import InputData

app=FastAPI()

engine=create_engine(
    "sqlite:///database.db",
    connect_args={"check_same_thread": False},
    echo=True
)


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/members/store/employee")
def get_data(new_emp:InputData, session:Session=Depends(get_session))->InputData:
    new_emp_data=InputData.from_orm(new_emp)
    session.add(new_emp_data)
    session.commit()
    session.refresh(new_emp_data)
    return new_emp


