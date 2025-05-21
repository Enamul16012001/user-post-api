# User Post API

A FastAPI-based REST API for managing users and posts.

## Setup Instructions

### Local Development

#### 1. Clone the Repository

```bash
git clone https://github.com/Enamul16012001/user-post-api.git
cd user-post-api
```

#### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

This will:
- Start the development server
- Enable auto-reload for code changes
- Make the API available at http://localhost:8000

Access the API documentation at http://localhost:8000/docs

### Docker Setup

#### Building the Docker Image

Build the Docker image from the Dockerfile:

```bash
docker build -t user-post-api .
```

#### Running the Docker Container

Run the container from your locally built image:

```bash
docker run -p 8000:8000 user-post-api
```

Make the API available at http://localhost:8000

### Using DockerHub Image

#### Pulling the Image

Pull the pre-built Docker image from DockerHub:

```bash
docker pull enamulatiq/user-post-api:latest
```

#### Running the Container from DockerHub Image

```bash
docker run -p 8000:8000 enamulatiq/user-post-api
```

## API Usage

Once the application is running (locally or via Docker), you can access:

- API documentation: http://localhost:8000/docs
- Alternative documentation: http://localhost:8000/redoc