from sqlalchemy import table
from sqlmodel import SQLModel, Field


class InputData(SQLModel, table=True):
    employee_id: str=Field(primary_key=True)
    employee_name: str
    employee_position: str
    employee_depart: str







