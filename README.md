
## Running Locally

Follow these steps to run the project locally on your machine:

### 1. Prerequisites

- [Python](https://www.python.org/) (version X.X.X)
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
