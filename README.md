# 🏦 Monthly Cash Book Data Splitter

This application is designed to help accounting teams quickly separate **Mpesa** transactions from **Non-Mpesa** transactions across multiple months in a single Excel Cash Book.

## 📋 What this site does
Manual reconciliation is difficult when different payment types are mixed. This tool:
1. **Reads all sheets** in your Excel file (e.g., January through December).
2. **Filters transactions** by scanning the "Particulars" column for the keyword "- MPESA".
3. **Generates two separate files** for download so you can reconcile them independently.

---

## ⚠️ Important Rules for your Data
To ensure the system works correctly, your Excel file must follow these rules:

* **The First Row Rule:** The very first row of every sheet **must** contain the column headers (e.g., Date, Particulars, Receipts, etc.). 
    * *Warning:* If there are titles, empty rows, or "Summary" text at the very top (above the headers), the system will not be able to find your columns.
* **Selection Persistence:** When you switch from one month (sheet) to another, the "Particulars" column selector will **reset to the first column**. 
    * *Action:* Always double-check that you have re-selected the "Particulars" column every time you change the month.

---

## 🚀 How to Use

1. **Upload:** Click the "Browse files" button in the sidebar and upload your Reconciled Cash Book.
2. **Select Month:** Use the dropdown menu at the top to choose the month (Sheet) you want to work on.
3. **Map Column:** Under "Select the Particulars Column," choose the column that contains the names and the "- MPESA" text.
4. **Download:** * Click **Download [Month]-mpesa-entries.csv** for your mobile money records.
    * Click **Download [Month]-non-mpesa-entries.csv** for all other records (Bank transfers, checks, etc.).
5. **Repeat:** Simply change the month in the dropdown to continue with the next sheet without re-uploading.

---

## 🛠️ Technical Setup (For Developers)
If running locally:
1. Install requirements: `pip install streamlit pandas openpyxl`
2. Run app: `streamlit run app.py`