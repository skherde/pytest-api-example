from jsonschema import validate, ValidationError
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200, f"Ecpected 200 , got {response.status_code}"

    data = response.json()


    # Validate the response schema against the defined schema in schemas.py
    try:
        validate(instance=data, schema=schemas.pet)
    except ValidationError as e:
        print("Schema validation error", e.message)
        assert False, f"Schema validation failed: {e.message}"

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code ==200, f"Expected 200, got {response.status_code}"

    pets = response.json()
    for pet in pets:
        assert pet["status"] == status, f"Expected status '{status}', got '{pet['status']}'"
        validate (instance=pet, schema=schemas.pet)

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
def test_get_by_id_404():
    
    endpoint = f"/pets/10"
    response = api_helpers.get_api_data(endpoint)

    assert response.status_code == 404 , f" Expected 404 for per={pet_id}, got (response.status_code)"
    data = response.json()
    if "message" in data:
        print(f" API reponse message for pet_id = (pet_id): (data('message'))")