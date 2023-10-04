import csv
import requests
import time

# Define the URL and the static payload data
URL = "https://domain.com/wp-admin/admin-ajax.php"
PAYLOAD = {
    "action": "wpseo_add_redirect_plain",
    "ajax_nonce": "ad2d1d3aa0",
    "redirect[target]": "",
    "redirect[type]": "410",
    "ignore_warning": "false"
}

# Define the authentication cookie
COOKIES = {
    'wordpress_logged_in_[hash]': 'insert_cookie_value_here'
}

MAX_RETRIES = 3
RETRY_DELAY = 5  # in seconds


def add_redirect(link):
    """
    Send a request to add a redirect for the given link.
    """
    # URL-encode the link and update the redirect origin
    #encoded_link = quote(link, safe='')
    PAYLOAD["redirect[origin]"] = link

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(URL, data=PAYLOAD, cookies=COOKIES)

            # Check if the request was successful
            if response.status_code == 200:
                print(f"Successfully added redirect for {link}")
                return
            else:
                print(f"Attempt {attempt + 1}: Failed to add redirect for {link}. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Error occurred while adding redirect for {link}. Error: {e}")

        # If not the last attempt, wait before retrying
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)

    print(f"Failed to add redirect for {link} after {MAX_RETRIES} attempts.")


def main():
    # Read the CSV file
    with open('links.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            link = row[0]  # Assuming the link is in the first column
            add_redirect(link)


if __name__ == "__main__":
    main()
