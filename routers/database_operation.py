from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from dbconnect import get_session
from schemas import InputEmpDetails, InputTeamDetails

router=APIRouter()

@router.post("/members/store/employee/")
def get_data(new_emp:InputEmpDetails, session:Session=Depends(get_session))->InputEmpDetails:
    new_emp_data=InputEmpDetails.from_orm(new_emp)
    session.add(new_emp_data)
    session.commit()
    session.refresh(new_emp_data)
    return new_emp


@router.post("/members/store/team/")
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


@router.get("/get/employee")
def search_all_data(session:Session=Depends(get_session))->list[InputEmpDetails]:
    query=select(InputEmpDetails)
    return session.exec(query).all()


@router.get("/search/employee/id")
def search_employe(id:str, session: Session=Depends(get_session))->list[InputEmpDetails]:
    query=select(InputEmpDetails)
    if id:
        query=query.where(InputEmpDetails.employee_id==id)
        return session.exec(query).all()
    else:
        raise HTTPException(status_code=404, detail=f"No record with the id = {id}")
