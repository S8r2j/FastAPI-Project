from fastapi.testclient import TestClient
from unittest.mock import Mock

from database_store import app
from routers.database_operation import get_team_data
from schemas import InputTeamDetails

client= TestClient(app)

def test_get_data():
    mock_session=Mock()
    response=InputTeamDetails(employee_id="Emp 4", employee_name= "Employee 4", team_name="Team-Frontend", team_manager="Manager 2")
    result=get_team_data(response, session=mock_session)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()
    assert isinstance(result,InputTeamDetails)
    assert result.employee_id=="Emp 4"
    assert result.employee_name=="Employee 4"
    assert result.team_name=="Team-Frontend"
    assert result.team_manager=="Manager 2"