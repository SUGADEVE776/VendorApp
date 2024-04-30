
#### SetUp and Running Locally ####

Follow these steps to run the project locally on your machine:

### 1. Prerequisites

- [Python](https://www.python.org/) (version 3.10.9)
- [Git](https://git-scm.com/) (optional, for cloning the repository)

### 2. Set Up Virtual Environment

Install `virtualenv` if you haven't already:

```bash
pip install virtualenv
```

Create and activate a virtual environment:

- **Windows:**
  ```bash
  virtualenv venv
  venv\Scripts\activate
  ```

### 3. Clone the Repository

```bash
git clone https://github.com/SUGADEVE776/VendorApp.git
```

Alternatively, you can download the code as a ZIP file and extract it.

### 4. Install Dependencies

Navigate to the project directory and install the required packages:

```bash
pip install -r requirements.txt
```

### 5. Database Migrations

Run the following commands to apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

### 7. Test in Postman

You can use [Postman](https://www.postman.com/) to test the API endpoints.

---


### About the Vendor Application ###

# 1. Vendor GET, POST, PUT, DELETE

```bash
{
    "name" : "newvendor",
    "email": "newvendor@mailinator.com",
    "address" : "north street of chicago",
    "contact_details" : "contact",
    "vendor_code" : "V52"
}
```

# 2. Purschase order GET, POST, PUT, DELETE

# a. Create Purchase Order.
```bash
{
    "po_number":11,
    "delivery_date":"2024-05-10",
    "items": {
        "item1":5,
        "item2" :8
    },
    "quantity": 111,
    "status": "pending"
}
```
# b. Issue to Vendor.

Add this to the previous body to issue the PO to vendor

```bash
{
  "vendor" : 2,
  "issue_date" : "2024-05-01"
}
```

# c. Acknowledgment by Vendor.

By calling the acknowledgment endpoint "acknowledgment_date" gets updated.

# d. Rating the Purchase Order.

Add this part to previous body to update quality rating

```bash
{
  "quality_rating" : 4.3
}
```

# 3. Vendor Performance metrics

By updating the purchase orders each will trigger the signal under certain condition and updated the Vendors performance Metrics
