import requests
from requests_folder.get_token import generate_token


def update_order(customer_name, orderid):
    request_body = {
        "customerName": customer_name,
    }
    token = generate_token()
    header_params = {'Authorization': token}
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{orderid}", json=request_body, headers=header_params)
    return response
