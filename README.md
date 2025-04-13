# Flask CRUD with Weather API Integration and MySQL

A Flask web application demonstrating CRUD operations for items stored in a **MySQL database**, combined with integration to the WeatherAPI.com service.

## Features

*   **Item Management (CRUD):**
    *   View a list of items.
    *   Add new items with a name and optional description.
    *   Edit existing items.
    *   Delete items.
    *   Data is persistently stored in a **MySQL database** using Flask-SQLAlchemy.
*   **RESTful API Endpoints:** Provides JSON endpoints for managing items (`/items`).
*   **Weather Check:**
    *   Fetch current weather conditions for a given city using the WeatherAPI.
*   **Web Interface:**
    *   Single-page interface using Flask templates (Jinja2) and Bootstrap 5.
    *   Client-side interactions via vanilla JavaScript (Fetch API).

## Prerequisites

*   Python 3.x
*   pip
*   Git
*   **A running MySQL Server instance**
*   A WeatherAPI.com API Key

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shaunm1724/flask-ws.git
    cd flask-ws
    ```

2.  **Set up MySQL:**
    *   Ensure your MySQL server is running.
    *   Connect to MySQL (e.g., using the `mysql` command-line client or a GUI tool).
    *   **Create a database** for the application (e.g., `CREATE DATABASE flask_crud_db;`).
    *   **(Optional but Recommended)** Create a dedicated user and grant privileges for that database (e.g., `CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'your_password'; GRANT ALL PRIVILEGES ON flask_crud_db.* TO 'flaskuser'@'localhost'; FLUSH PRIVILEGES;`).

3.  **Create and activate a virtual environment:**
    *   macOS/Linux: `python3 -m venv venv && source venv/bin/activate`
    *   Windows: `python -m venv venv && .\venv\Scripts\activate`

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables:**
    *   Copy the example environment file: `cp .env.example .env`
    *   Edit the `.env` file:
        *   Set `WEATHER_API_KEY` with your key from WeatherAPI.com.
        *   **Update `DATABASE_URL`** with your MySQL connection string, using the database name, user, and password you set up in step 2. The format is `mysql+mysqlconnector://<user>:<password>@<host>/<database_name>`. Example: `mysql+mysqlconnector://flaskuser:your_password@localhost/flask_crud_db`
## Running the Application

1.  **Start the Flask development server:**
    ```bash
    flask run
    ```
    Or:
    ```bash
    python app.py
    ```
    The first time you run it, it should automatically create the `item` table in your MySQL database.

2.  **Access the application:**
    Open `http://127.0.0.1:5000` in your browser.

<!-- The application runs in debug mode. **Do not use debug mode in production.** -->

<!-- ## API Endpoints
(...keep existing API endpoint descriptions...)

## Project Structure
(...keep existing structure, maybe add note about database model...) -->

<!-- ## Notes

*   Item data is now **persistently stored** in the configured MySQL database.
*   Database table creation is handled automatically on the first run for development simplicity using `db.create_all()`. For production or more complex schema changes (migrations), consider using `Flask-Migrate`. -->