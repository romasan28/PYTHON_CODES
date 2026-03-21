import pytest
from api_client import get_token, ProjectsAPI

@pytest.fixture(scope="session")
def api_client():
    token = get_token()
    client = ProjectsAPI(token)
    yield client
    