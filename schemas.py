from sqlalchemy import table
from sqlmodel import SQLModel, Field


class InputEmpDetails(SQLModel, table=True):
    employee_id: str=Field(primary_key=True)
    employee_name: str
    employee_position: str
    employee_depart: str


class InputTeamDetails(SQLModel, table=True):
    employee_id: str= Field(primary_key=True)
    employee_name: str
    team_name: str
    team_manager: str







