# WPSEO Redirect Automation Script

This script automates the process of adding redirects to a WordPress website using the WPSEO (Yoast SEO) plugin's AJAX endpoint.

## Features

- Reads links from a CSV file and adds them as redirects.
- Retries failed attempts up to a specified maximum number of retries.
- Uses authentication cookies for requests.

## Prerequisites

- Python 3
- `requests` library. Install it using:
  ```bash
  pip install requests
