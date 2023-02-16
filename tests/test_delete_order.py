from requests_folder.submit_order import submit_order
from requests_folder.delete_order import delete_order


class TestDeleteOrder:
    def test_delete_order(self):
        response = delete_order(submit_order(1, "AndreeaT").json()["orderId"])
        assert response.status_code == 204, f"Error: Status code is not valid. Expected: 204, actual: {response.status_code}"
        assert response.json() == ""
