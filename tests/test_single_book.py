from requests_folder.get_a_single_book import get_a_single_book


class TestGetSingleBook:
    def test_get_single_book(self):
        response = get_a_single_book(2)
        assert response.status_code == 200, f"Error: Status code is not valid. Expected: 200, actual: {response.status_code}"
        assert response.json()["name"] == "Just as I Am", f"Error: Name is not valid. Expected: 'Just as I Am', actual: {response.json()['name']}"
        assert response.json()["type"] == "non-fiction", f"Error: Type is not valid. Expected: 'non-fiction', actual: {response.json()['type']}"

    def test_get_single_book_inexisting(self):
        response = get_a_single_book(15)
        assert response.status_code == 404, f"Error: Status code is not valid. Expected: 404, actual: {response.status_code}"
        assert response.json()["error"] == "No book with id 15", f"Error: Message error is not valid. Expected: 'No book with id 15', actual: {response.json()['error']}"
