# Dockerized fast api boilerplate [Incomplete]

### Building the Docker image from our Dockerfile

Go to folder where dockerfile is located and run the following command:
```
docker image build --tag fast-api-app-image .
```

### Running the Docker image as a container

```
docker container run --publish 80:80 --name fast-api-app fast-api-app-image
```

```
sudo docker run –d –v /home/<local-dir>:projects/<remote-dir> –p 8080:8080 <image-name>
```

## Run the flask app

pip install -r requirements.txt

Python app.py

or 

uvicorn app.main:app --reload

## docker compose

```
docker-compose up
```

## directory structure

- main.py: It serves as the entry point for your application where you can start the FastAPI server.
- api: This directory contains the API-related code.
- routes: Contains individual route handlers. In this case, you might have a predictions.py file to handle prediction requests.
- models: Contains code related to your ML models, such as inference.py for making predictions and training.py for training the models.
- schemas: Contains Pydantic models that define the input/output validation for API requests and responses.
- utils: Contains utility functions and helper modules that are not directly related to the API or models, such as preprocessing.py for data - preprocessing.
- tests: Contains unit tests for your codebase. You can have separate test files for different modules or routes.
- requirements.txt: Lists the Python dependencies required for your project.
- Dockerfile: If you plan to containerize your application using Docker, you can define the Docker configuration in this file.

