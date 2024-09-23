# News Service

## Description

This is an API for managing news articles, developed using Django and Django REST Framework. The API supports basic CRUD operations (Create, Read, Update, Delete) for news objects.

## Technologies

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- Redis (for caching)
- Docker (for containerization)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vadzimbudnikau/news_service_test.git
   cd news_service_test
   
2. Сreate and activate a virtual environment:
    
    ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows use .venv\Scripts\activate
   
3. Install dependencies:
    
    ```bash
   pip install -r requirements.txt
   
## Running the Application

1. Start the containers using Docker Compose:

    ```bash
   docker-compose up --build
   
2. The API will be available at http://localhost:8000.

## Endpoints

    POST /news/create/ - Create a news article.
    GET /news/<id>/ - Retrieve a news article by ID.
    PUT /news/<id>/update/ - Update a news article by ID.
    DELETE /news/<id>/delete/ - Delete a news article by ID.

## Testing

1. To run the tests, execute the command:

    ```bash
   python manage.py test
   
## Logging

Application logs are saved in the file django_debug.log.

## Notes

    PostgreSQL database and Redis cache are run using Docker containers.
    Database and Redis settings can be changed in the docker-compose.yml file.