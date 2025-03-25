# Task Management API

A RESTful API built with Django and Django REST Framework to manage tasks and users. This API allows you to create tasks, assign tasks to users, register new users, and retrieve tasks or users as needed.

## Setup Instructions

1. Clone the Repository or Extract the Zip File
    git clone "https://github.com/kothapallyshivasai/Task-Management-API.git"

2. Navigate to the Project Directory
    cd task_management_api

3. Install Dependencies
    pip install -r requirements.txt

4. Apply Migrations
    python manage.py migrate

5. Run the Server
    python manage.py runserver

## API Endpoints

1. User Registration
URL: POST http://127.0.0.1:8000/register/

Description: Registers a new user for you if the users are not enough.

Sample JSON Body:
    {
        "username": "testuser2",
        "email": "testuser2@example.com",
        "password": "password123",
        "mobile": "1234567891"
    }


2. Create Task
URL: POST http://127.0.0.1:8000/tasks/create/

Description: Creates a new task.

Sample JSON Body:
    {
        "title": "Sample Task",
        "description": "This is a sample task description."
    }


3. Assign Task
URL: POST http://127.0.0.1:8000/tasks/{task_id}/assign/
Replace {task_id} with the actual task ID.

Description: Assigns users to an existing task.

Sample JSON Body:
    {
        "assigned_users": [1, 2]
    }

4. Get User Tasks
URL: GET /api/users/{user_id}/tasks/
Replace {user_id} with the actual user ID.

Description: Retrieves all tasks assigned to the specified user.


5. List All Users
URL: GET /api/users/

Description: Retrieves a list of all registered users. Mainly useful to get the id's of the users but not their passwords.


6. List All Tasks
URL: GET /api/tasks/

Description: Retrieves a list of all tasks. This is useful to get the id's of the tasks.


### Download Postman or Thunder Client to test this API.