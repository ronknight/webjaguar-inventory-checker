<h1 align="center">🦈 <a href="https://github.com/ronknight/webjaguar-inventory-checker">WebJaguar Inventory Checker</a></h1>

<h4 align="center">🔍 A Python script to validate the inventory status of products on WebJaguar by checking SKUs against their API and logging results to CSV and log files.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/webjaguar-inventory-checker/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/webjaguar-inventory-checker/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/webjaguar-inventory-checker/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/webjaguar-inventory-checker/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

---

<p align="center">
  <a href="#project-overview">Project Overview</a> •
  <a href="#features">Features</a> •
  <a href="#setup">Setup</a> •
  <a href="#usage">Usage</a> •
  <a href="#files">Files</a> •
  <a href="#diagram">Diagram</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## 📖 Project Overview

The **WebJaguar Inventory Checker** is a Python script designed to streamline inventory management. It reads a list of product SKUs from a CSV file, fetches their statuses from the WebJaguar API, and writes the results to a new CSV file while also logging the responses for debugging purposes.

---

## ✨ Features

- **SKU Status Validation**: Check the `active` status of products on WebJaguar.
- **CSV Input and Output**: Input SKUs via a CSV file and output results with additional columns indicating inventory statuses.
- **Logging**: Logs all API responses to a timestamped log file for transparency and debugging.
- **Environment Variables**: Secures sensitive credentials using a `.env` file.

---

## ⚙️ Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ronknight/webjaguar-inventory-checker.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd webjaguar-inventory-checker
   ```

3. **Install Dependencies**:
   Make sure Python 3.6+ is installed. Install required packages using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project directory with the following content:
   ```env
   API_URL=https://your-webjaguar-api-url.com
   AUTH_CREDENTIALS=your-username:your-password
   COOKIE=your-session-cookie
   ```

---

## 🚀 Usage

1. **Prepare the Input CSV File**:
   - Create a file named `product_id.csv` with the following format:
     ```csv
     4SGM_SKU
     SKU123
     SKU456
     SKU789
     ```

2. **Run the Script**:
   - Execute the script to validate product statuses:
     ```bash
     python check_inventory_status.py
     ```

3. **Review the Outputs**:
   - **`product_id_with_status_<timestamp>.csv`**: Contains the original SKUs with an additional `inventory_active` column indicating the product status (`True` or `False`).
   - **`response_log_<timestamp>.txt`**: Logs all API responses for auditing or troubleshooting.

---

## 📂 Files

### Key Files
- **`check_inventory_status.py`**: The main Python script for inventory validation.
- **`.env`**: File for securely storing API credentials and other sensitive configuration values.
- **`requirements.txt`**: Lists Python dependencies required to run the script.

### Example/Generated Files
- **`product_id.csv`**: Example input file containing SKUs to validate.
- **`product_id_with_status_<timestamp>.csv`**: Output file with validated statuses.
- **`response_log_<timestamp>.txt`**: Logs API responses for each SKU.

---

## 📊 Diagram

```mermaid
graph TD
    A[Start: User Executes Script] -->|Reads| B[Input CSV File (product_id.csv)]
    B -->|Extracts SKUs| C[Check SKU Status via WebJaguar API]
    C -->|Sends API Request| D[WebJaguar API]
    D -->|Returns Response| E[Parse API Response]
    E -->|Extract Status| F[Write to Output CSV]
    F -->|Save Logs| G[Log API Responses to response_log.txt]
    G --> H[End: Results Saved]

```

## ⚠️ Disclaimer

This script interacts with WebJaguar's API using sensitive credentials (API keys and cookies). Ensure proper security measures, such as excluding `.env` files from version control, and comply with the WebJaguar terms of service. Use at your own risk.

---