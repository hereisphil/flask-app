# Auth0 Flask Integration - Module 2.4

This repository contains a full-stack Python application utilizing the **Flask** framework and **Jinja2** templating engine to implement secure authentication via **[Auth0](https://auth0.com/)**. This project was developed as part of the *Application Integration and Security* course at **[Full Sail University](https://www.fullsail.edu/)**.

## 🚀 Overview

This app demonstrates basic protected routes (`/dashboard` and `/settings`) are by a custom decorator. It handles the OAuth 2.0 flow, retrieves user metadata, and displays it dynamically using Jinja templates.

### Key Features

* **Auth0 Integration**: Secure login using the `authlib` library.
* **Protected Routes**: A custom `@requires_auth` decorator to manage session states.
* **Dynamic Templating**: Optimized for Google and Email login providers to leverage profile data (names, pictures, and nicknames).
* **Session Management**: Configured for a 15-minute automatic session expiration.

-----

## 📂 Project Structure

```text
flask-app/
├── .venv/                  # Virtual environment (isolated dependencies)
├── templates/              # Jinja2 HTML templates
│   ├── base_template.html  # Parent layout with shared styles/headers
│   ├── index.html          # Public landing page
│   ├── dashboard.html      # Protected: displays raw session data
│   └── settings.html       # Protected: displays user profile information
├── .env                    # Environment variables (Sensitive Data)
├── .env.example            # Template for required environment variables
├── .gitignore              # Prevents sensitive files from being committed
└── app.py                  # Main Flask application entry point
```

-----

## 🛠️ Prerequisites

Before running the app, you must have the following:

1. **Python 3+** installed on your machine.
2. An **Auth0 Account**.
3. An **Auth0 Application** set up as a "Regular Web Application" with the following settings:
    * **Allowed Callback URLs**: `http://localhost:5005/callback`

-----

## ⚙️ Setup & Configuration

### 1\. Environment Variables

Create a `.env` file in the root directory (referencing your `.env.example`). You must populate it with your specific Auth0 credentials:

```bash
# Security key for Flask sessions
RANDOM_APP_KEY="your_generated_random_string"

# Auth0 Specific Data
AUTH0_BASE_URL="https://your-tenant.auth0.com"
AUTH0_CLIENT_ID="your_client_id"
AUTH0_CLIENT_SECRET="your_client_secret"
AUTH0_SERVER_METADATA_URL="https://your-tenant.auth0.com/.well-known/openid-configuration"
```

### 2\. Install Dependencies

It is highly recommended to use a virtual environment:

```bash
# Create and activate venv
python3 -m venv .venv
source .venv/bin/activate

# Install required packages
pip install flask authlib python-dotenv requests
```

-----

## 🏃 Running the Application

To start the Flask development server, run:

```bash
python3 app.py
```

Once the server is active, open your browser and navigate to:
**[http://localhost:5005](https://www.google.com/search?q=http://localhost:5005)**

-----

## 📝 Technical Notes

* **Data Sources**: This application is optimized for users logging in via **Google** or **Email**. Logging in via Google provides a richer JSON response (including `nickname` and `picture`), which the `settings.html` template is specifically designed to render.
* **Security**: The app uses `load_dotenv` to ensure that API secrets are never hardcoded in the source logic, following industry best practices for environment variable management.
* **Session Persistence**: The `permanent_session_lifetime` is set to 15 minutes to balance user convenience with security.

- **GitHub:** [hereisphil](https://github.com/hereisphil)
- **LinkedIn:** [phillipcantu](https://www.linkedin.com/in/phillipcantu/)
- **Email:** [thereisphil@gmail.com](mailto:thereisphil@gmail.com)
