from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

    @pytest.fixture
    def test_order_id():

        return 1 #In real world,we can use post API to create new order and return ID

    def test_patch_order_by_id(test_order_id):
    
    endpoint = f"/store/order/(test_order_id)"
    payload = ("status": "sold")

    response = api_helpers.patch_api_data(endpoint, payload)
    assert response.status_code == 200 , f"Expected 200, got (response.status_code)"

    body = response.json

    assert body.get("message") == "Order and pat status updated successfully", f"Unexpected message: (body.get('message))"

    assert body.get("status") == "sold", f" Expected status 'sold, got (body.get('status'))"

