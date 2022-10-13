from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import create_engine, SQLModel, Session

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