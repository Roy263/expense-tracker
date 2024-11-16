
# Expense Tracker

A simple web application for tracking expenses, built with Python, FastAPI, and Docker. This app allows users to manage their financial records efficiently by adding, updating, and viewing expense data.

## Features

- **FastAPI Framework**: A modern, fast web framework for building APIs.
- **MongoDB Integration**: Store and manage expense data using MongoDB.
- **MongoDB Express**: Simple GUI for interacting with the MongoDB database.
- **User-Friendly Interface**: HTML templates for an intuitive user experience.
- **Dockerized Deployment**: Easily run the application and database in a containerized environment.
- **Modular Codebase**: Organized into controllers, constants, and templates for maintainability.

## Project Structure

```
expense-tracker/
├── constants/          # Constants used across the application
├── controllers/        # Business logic and request handling
├── templates/          # HTML files for frontend views
├── app.py              # Main entry point for the FastAPI application
├── requirements.txt    # Dependencies for the application
├── docker-compose.yml  # Docker Compose setup for app and MongoDB
├── Dockerfile          # Docker setup for containerized deployment
└── .gitignore          # Git ignore rules
```

## Prerequisites

- Python 3.11 or later
- Docker and Docker Compose

## Installation and Usage

### Running Locally with MongoDB

1. Clone the repository:
   ```bash
   git clone https://github.com/Roy263/expense-tracker.git
   cd expense-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run MongoDB and MongoDB Express with Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Run the application:
   ```bash
   uvicorn app:app --reload
   ```

5. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

6. Access MongoDB Express at [http://127.0.0.1:8081](http://127.0.0.1:8081).

### Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t expense-tracker .
   ```

2. Run the application container:
   ```bash
   docker-compose up -d
   ```

3. Connect the application docker to the same network as the MongoDB:
   ```bash
   docker network ls
   docker network connect <<mongodb_network>> <<application_docker_name>>
   ```

4. Access the application at [http://localhost:8000](http://localhost:8000).

5. Access MongoDB Express at [http://localhost:8081](http://localhost:8081).

## Docker Compose Setup

The `docker-compose.yml` file is used to set up the application and MongoDB with MongoDB Express:

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    depends_on:
      - mongodb
    environment:
      MONGO_URI: mongodb://mongodb:27017/expense-tracker
    command: uvicorn app:app --host 0.0.0.0 --port 8000

  mongodb:
    image: mongo:latest
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

  mongo-express:
    image: mongo-express:latest
    container_name: mongo-express
    ports:
      - "8081:8081"
    environment:
      ME_CONFIG_MONGODB_SERVER: mongodb

volumes:
  mongo-data:
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
