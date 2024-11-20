import os
import csv
import requests
from base64 import b64encode
from urllib.parse import quote
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration from .env
API_URL = os.getenv("API_URL")
AUTH_CREDENTIALS = os.getenv("AUTH_CREDENTIALS")
COOKIE = os.getenv("COOKIE")

# Ensure all required environment variables are available
if not API_URL or not AUTH_CREDENTIALS or not COOKIE:
    raise EnvironmentError("Missing required environment variables in .env file")

# Generate headers for the API request
HEADERS = {
    "Content-Type": "text/plain",
    "Authorization": f"Basic {b64encode(AUTH_CREDENTIALS.encode()).decode()}",
    "Cookie": COOKIE,
}

# Generate timestamp for filenames
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE_PATH = f"response_log_{timestamp}.txt"
OUTPUT_CSV_PATH = f"product_id_with_status_{timestamp}.csv"


def log_response(sku, response):
    """Log the response of each API request to a log file."""
    with open(LOG_FILE_PATH, mode='a') as log_file:
        log_entry = f"[{datetime.now()}] SKU: {sku}, Status Code: {response.status_code}, Response: {response.text}\n"
        log_file.write(log_entry)


def check_product_status(sku):
    """Check the status of a product by SKU."""
    # Payload for the request body
    data = {
        "supplierIds": [1, 2],
        "name": "product12",
        "sku": sku,
    }
    try:
        # Perform the GET request with headers and data
        response = requests.get(API_URL, headers=HEADERS, json=data, params={"sku": quote(sku)})
        response.raise_for_status()

        # Log the response
        log_response(sku, response)

        # Extract the "active" field from the response
        product_data = response.json()
        return product_data.get("product", {}).get("active", False)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error for SKU {sku}: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error for SKU {sku}: {req_err}")
    except Exception as e:
        print(f"Unexpected error for SKU {sku}: {e}")

    # Log the error response
    if 'response' in locals():
        log_response(sku, response)
    return None


def process_csv(input_file, output_file):
    """Parse CSV file, check the status of each SKU, and write results to a new CSV."""
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["inventory_active"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            sku = row.get("4SGM_SKU")
            if sku:
                status = check_product_status(sku)
                row["inventory_active"] = status
            else:
                row["inventory_active"] = None
            writer.writerow(row)


if __name__ == "__main__":
    # Input CSV file path
    input_csv_path = "product_id.csv"

    # Clear the log file before starting
    open(LOG_FILE_PATH, 'w').close()

    # Process the input CSV and generate output
    process_csv(input_csv_path, OUTPUT_CSV_PATH)
    print(f"Processing complete. Results saved to {OUTPUT_CSV_PATH}. Responses logged in {LOG_FILE_PATH}.")
