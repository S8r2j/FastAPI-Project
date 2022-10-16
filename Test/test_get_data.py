from fastapi.testclient import TestClient
from unittest.mock import Mock

from database_store import app
from routers.database_operation import get_data
from schemas import InputEmpDetails

client= TestClient(app)

def test_get_data():
    mock_session=Mock()
    response=InputEmpDetails(employee_id="Emp 6", employee_name= "Employee 6", employee_position= "Senior Developer", employee_depart= "Quality Assurance")
    result=get_data(response, session=mock_session)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()
    assert isinstance(result,InputEmpDetails)
    assert result.employee_id=="Emp 6"
    assert result.employee_name=="Employee 6"
    assert result.employee_position=="Senior Developer"
    assert result.employee_depart=="Quality Assurance"