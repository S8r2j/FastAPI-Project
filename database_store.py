from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import create_engine, SQLModel, Session, select

from schemas import InputEmpDetails, InputTeamDetails

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

@app.post("/members/store/employee/")
def get_data(new_emp:InputEmpDetails, session:Session=Depends(get_session))->InputEmpDetails:
    new_emp_data=InputEmpDetails.from_orm(new_emp)
    session.add(new_emp_data)
    session.commit()
    session.refresh(new_emp_data)
    return new_emp


@app.post("/members/store/team/")
def get_team_data(new_team:InputTeamDetails, session: Session=Depends(get_session))->InputTeamDetails:
    team=session.get(InputEmpDetails,new_team.employee_id)
    if team:
        new_team_data=InputTeamDetails.from_orm(new_team)
        session.add(new_team_data)
        session.commit()
        session.refresh(new_team_data)
        return new_team
    else:
        raise HTTPException(status_code=404, detail=f"No Employee with id= {new_team.employee_id} found")

@app.get("/get/employee")
def search_all_data(session:Session=Depends(get_session))->list[InputEmpDetails]:
    query=select(InputEmpDetails)
    return session.exec(query).all()

@app.get("/search/employee/id")
def search_employe(id:str,session: Session=Depends(get_session))->list[InputEmpDetails]:
    query=select(InputEmpDetails)
    if id:
        query=query.where(InputEmpDetails.employee_id==id)
        return session.exec(query).all()
    else:
        raise HTTPException(status_code=404, detail=f"No record with the id = {id}")