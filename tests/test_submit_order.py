from requests_folder.submit_order import submit_order, submit_order_with_errors


class TestSubmitOrder:
    def test_submit_order(self):
        response = submit_order(1, "Andreea")
        assert response.status_code == 201, f"Error: Status code is not valid. Expected: 201, actual: {response.status_code}"
        assert response.json()["created"] == True, f"Error: Order creation status is not correct. Expected: True, Actual: {response.json()['created']}"
        assert len(response.json()["orderId"]) > 0, f"Error: Order id is invalid. Expected length greater than zero. Actual length: {len(response.json()['orderId'])} "

    def test_submit_order_with_authorization_header(self):
        response = submit_order_with_errors(1, "Andreea")
        assert response.status_code == 401, f"Error: Status code is not valid. Expected: 401, actual: {response.status_code}"
        assert response.json()["error"] == "Missing Authorization header.", f"Error: Message error is invalid. Expected: 'Missing Authorization header.' Actual: {response.json()['error']}"

    def test_submit_order_inexisting_book(self):
        response = submit_order(8, "Andreea")
        assert response.status_code == 400, f"Error: Status code is not valid. Expected: 400, actual: {response.status_code}"
        assert response.json()["error"] == "Invalid or missing bookId.", f"Error: Message error is invalid. Expected: 'Invalid or missing bookId' Actual: {response.json()['error']}"

    def test_submit_order_bookid_with_letters(self):
        response = submit_order("lkjgto", "Andreea")
        assert response.status_code == 400, f"Error: Status code is not valid. Expected: 400, actual: {response.status_code}"
        assert response.json()["error"] == "Invalid or missing bookId.", f"Error: Message error is invalid. Expected: 'Invalid or missing bookId' Actual: {response.json()['error']}"

    def test_submit_order_bookid_with_special_characters(self):
        response = submit_order("%&@#)_8", "Andreea")
        assert response.status_code == 400, f"Error: Status code is not valid. Expected: 400, actual: {response.status_code}"
        assert response.json()["error"] == "Invalid or missing bookId.", f"Error: Message error is invalid. Expected: 'Invalid or missing bookId' Actual: {response.json()['error']}"
