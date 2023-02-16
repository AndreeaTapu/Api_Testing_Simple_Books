from requests_folder.update_order import update_order
from requests_folder.submit_order import submit_order


class TestUpdateOrder:
    def test_update_order(self):
        response = update_order("AndreeaT", submit_order(1, "Andreea").json()["orderId"])
        assert response.status_code == 204, f"Error: Status code is not valid. Expected: 204, actual: {response.status_code}"
        assert response.json() == ""
