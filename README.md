# AmaniAI Case / URL Shortener Project Documentation

This document provides technical documentation for the project, including URL examples, instructions for running tests, and steps for setting up the project using Docker.

## URLs

The project includes the following URLs:

- **API for creating short URLs:**
  - Endpoint: `/api`
  - Method: POST
  - Payload: `{"original_url": "https://www.example.com"}`
  - Response: `{"original_url": "https://www.example.com", "short_url": "http://localhost:8000/abcd"}`

- **Redirection to original URL:**
  - Endpoint: `/<str:short_code>`
  - Method: GET
  - Example: `/abcd` (where `abcd` is the short code)
  - Response: Redirects to the original URL associated with the short code.

- **Web page for creating short URLs:**
  - Endpoint: `/`
  - Method: GET
  - Renders a form where users can enter the original URL and submit it to generate a short URL.

## Running the Tests

To run the tests for this project, follow these steps:

1. Make sure you have the project dependencies installed. You can install them using the following command:
  `pip install -r requirements.txt`
2. Open a terminal or command prompt and navigate to the project's root directory.

3. Run the following command to execute the tests:

   ```shell
   python manage.py test

## Setting Up the Project with Docker
Run the following command to build and run the Docker containers:
   ```shell
 docker-compose up
 ```

## Run Project Manually
1. Run the following command to apply migrations
   ```shell
    python manage.py migrate
2. Run the following command for run server
   ```shell
    python manage.py runserver
