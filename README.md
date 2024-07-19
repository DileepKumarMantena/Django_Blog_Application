# Django Blog Application

This project is a simple Django-based blog application that supports creating, retrieving, updating, and deleting blog posts, as well as creating and listing comments for each post.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Dependencies](#dependencies)

## Project Overview

The project consists of the following models:

- **Post**: Represents a blog post with fields like title, content, author, and published date.
- **Comment**: Represents a comment on a blog post with fields like author, text, and created date. Each comment is linked to a post.

The project includes serializers for creating and retrieving posts and comments, and views to handle the corresponding API requests.

## Installation

1. **Clone the repository**:

```sh
git clone <repository_url>
cd <repository_name>
```

2. **Create a virtual environment**:

```sh
python -m venv venv
```

3. **Activate the virtual environment**:

- On Windows:

  ```sh
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```sh
  source venv/bin/activate
  ```

4. **Install the dependencies**:

```sh
pip install -r requirements.txt
```

## Configuration

### Database Configuration

Update the `DATABASES` setting in your `settings.py` file to match your MySQL configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Django_Blog_Database',
        'USER': 'root',
        'PASSWORD': 'Dileep@9505816053',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Django Settings

Ensure your `INSTALLED_APPS` in `settings.py` includes the necessary applications:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'your_app_name',
    ...
]
```

## Running the Application

1. **Apply the migrations**:

```sh
python manage.py migrate
```

2. **Run the development server**:

```sh
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Post Endpoints

- **Create a new post**:
  - URL: `/CreateNewPost/`
  - Method: `POST`
  - Payload:
    ```json
    {
        "title": "Sample Post",
        "content": "This is a sample post content.",
        "author": "John Doe",
        "published_date": "2024-07-03T12:34:56Z"
    }
    ```

- **Get all posts**:
  - URL: `/GetAllPostListApi/`
  - Method: `GET`

- **Get a post by ID**:
  - URL: `/GetPostsById/<int:id>/`
  - Method: `GET`

- **Update a post by ID**:
  - URL: `/UpdatePostDetailsById/<int:id>/`
  - Method: `PUT`
  - Payload:
    ```json
    {
        "title": "Updated Post",
        "content": "This is updated post content.",
        "author": "John Doe",
        "published_date": "2024-07-04T12:34:56Z"
    }
    ```

- **Delete a post by ID**:
  - URL: `/DeletePostDetails/<int:id>/`
  - Method: `DELETE`

### Comment Endpoints

- **Get comments for a post**:
  - URL: `/posts/<int:post_id>/comments/`
  - Method: `GET`

- **Create a comment for a post**:
  - URL: `/posts/<int:post_id>/comments/create/`
  - Method: `POST`
  - Payload:
    ```json
    {
        "author": "Jane Doe",
        "text": "This is a sample comment."
    }
    ```

## Running Tests

1. **Create a test file `test_views.py` in your `tests` directory**:

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Post
from django.utils import timezone

class CreateNewPostTest(APITestCase):

    def setUp(self):
        self.url = reverse('create-post')  # Ensure this matches the URL name in your URLconf
        self.valid_payload = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'author': 'John Doe',
            'published_date': timezone.now().isoformat()
        }
        self.invalid_payload = {
            'title': '',
            'content': 'This is a test post content.',
            'author': 'John Doe',
            'published_date': timezone.now().isoformat()
        }

    def test_create_post_valid_payload(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertIn('Result', response.data)
        self.assertFalse(response.data['HasError'])
        self.assertEqual(response.data['status'], 200)
        self.assertTrue(Post.objects.filter(title='Test Post').exists())

    def test_create_post_invalid_payload(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)
        self.assertIn('Result', response.data)
        self.assertTrue(response.data['HasError'])
        self.assertEqual(response.data['status'], 400)
        self.assertFalse(Post.objects.filter(content='This is a test post content.').exists())
```

2. **Run the tests**:

- Using `pytest`:
  ```sh
  pytest
  ```

- Using Django's built-in test runner:
  ```sh
  python manage.py test
  ```

## Dependencies

- Django
- Django REST Framework
- MySQL

Make sure to include all the dependencies in your `requirements.txt` file. For example:

```txt
Django>=3.2,<4.0
djangorestframework>=3.12,<4.0
mysqlclient>=2.0,<3.0
```

