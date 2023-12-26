

## Creating a Simple Login Page with Flask, MySQL, and Docker

### 1. Set Up Flask Application

#### 1.1. Create a Project Directory:
```bash
mkdir Login_page_test
cd Login_page_test
```

#### 1.2. Create a Virtual Environment (Optional but Recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 1.3. Install Flask and PyMySQL:
```bash
pip install Flask pymysql
```

#### 1.4. Create Flask App (`app.py`):
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

#### 1.5. Create HTML Templates (`templates/index.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <h1>Welcome to the Login Page</h1>
</body>
</html>
```

#### 1.6. Run Flask App Locally:
```bash
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to see the login page.

### 2. Dockerize Flask Application

#### 2.1. Create Dockerfile (`Dockerfile`):
```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

#### 2.2. Create `requirements.txt`:
```txt
Flask==2.0.1
pymysql==1.0.2
```

#### 2.3. Build Docker Image:
```bash
docker build -t flask_app_image .
```

#### 2.4. Run Docker Container:
```bash
docker run -p 5000:5000 flask_app_image
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to see the login page served by the Docker container.

### 3. Set Up MySQL Database and Docker Container

#### 3.1. Update Flask App for MySQL (`app.py`):
```python
import pymysql
from flask import Flask, render_template

app = Flask(__name__)

# MySQL Configuration
db_host = 'mysql-db'
db_user = 'root'
db_password = 'password'
db_name = 'logintest'

# Connect to MySQL
db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

#### 3.2. Update Docker Compose (`docker-compose.yml`):
```yaml
version: '3'

services:
  flask-app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mysql-db

  mysql-db:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: logintest
      MYSQL_USER: root
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
```

#### 3.3. Build and Run Docker Compose:
```bash
docker-compose up --build
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to ensure the Flask app can connect to the MySQL container.

### 4. Push/Pull Docker Images

#### 4.1. Log in to Docker Hub (or Your Registry):
```bash
docker login
```
Enter your Docker Hub username and password.

#### 4.2. Tag Docker Images:
```bash
docker tag flask_app_image yourusername/flask_app_image:latest
docker tag mysql:latest yourusername/mysql:latest
```

#### 4.3. Push Docker Images:
```bash
docker push yourusername/flask_app_image:latest
docker push yourusername/mysql:latest
```

#### 4.4. Pull Docker Images on Another Server:
```bash
docker pull yourusername/flask_app_image:latest
docker pull yourusername/mysql:latest
```

