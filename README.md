# Movie_Table_API

A movie database management project built with Python and FastAPI.

## Overview

This project provides an API for working with movie information
stored in a database.

It was developed to practice backend development, API design,
and database integration using FastAPI.

## Features

- Add movie records
- Retrieve all movies
- Search for a movie by ID or title
- Update a movie's IMDb rating and release year
- Delete a movie by ID
- Store movie information in an SQLite database
- Provide a Python client for sending HTTP requests to the API

## Technologies

- Python
- FastAPI
- SQLite
- Requests
- Uvicorn

## Project Structure

├── README.md

├── .gitignore

├── requirements.txt

├── MoviesInfo.db

└── src/

        ├── app.py
        └── app_api.py

## Requirements

- Python
- pip

The Python packages required to run the project are listed in
`requirements.txt`.

## How to get started:

### 1. Clone the repository

    git clone YOUR_GITHUB_REPOSITORY_URL
    cd Movie_table

Replace the example repository URL with your actual GitHub URL.

### 2. Create a virtual environment

    python -m venv .venv

### 3. Activate the environment

    .venv\Scripts\Activate.ps1

If PowerShell blocks activation, you can use the Command Prompt
activation script instead:

    .venv\Scripts\activate.bat

### 4. Install dependencies

    python -m pip install -r requirements.txt

### 5. Start the API server

    python -m uvicorn src.app:app --reload

The API should be available at:

    http://127.0.0.1:8000

## API Documentation

When the server is running, open:

- Interactive API documentation: http://127.0.0.1:8000/docs
- Alternative API documentation: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /insert/{title}/{country}/{year}/{imdb_rate} | Add a movie |
| GET | /select_all/ | Retrieve all movies |
| GET | /select_by_id/{id} | Find a movie by ID |
| GET | /select_by_name/{title} | Find a movie by title |
| PUT | /update_by_id/{id}/{new_imdb_rate}/{new_year} | Update rating and year |
| DELETE | /delete_by_id/{id} | Delete a movie |

## Python Client

`src/app_api.py` contains Python functions that send HTTP requests
to the running API server.

Start the API server before using the client.