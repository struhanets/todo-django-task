# Django Todo List

A simple Todo List web application built with Django, Bootstrap 4, django-crispy-forms, Python 3.11, and SQLite3.
It lets you create, update, delete tasks and tags, and mark tasks as complete or incomplete.

### Features

**Home Page**
* Displays all tasks.
* Shows full task info: content, created date, optional deadline, status, and tags.
* Actions for each task: Add Task, Update, Delete, Complete / Undo.

**Tag List Page**
* Table view of all tags.
* Actions: Add Tag, Update, Delete.

**Sidebar**
Visible on all pages.
* Links to: Home Page, Tag List Page

### Tech Stack

* Python 3.11
* Django
* Bootstrap 4
* django-crispy-forms
* SQLite3

### Getting Started

#### 1. Clone the repository
`git clone https://github.com/your-username/your-todo-list-repo.git
cd your-todo-list-repo`

#### 2. Create and activate a virtual environment
`python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows`

#### 3. Install dependencies
`pip install -r requirements.txt`

#### 4. Apply migrations
`python manage.py migrate`

#### 5. Run the development server
`python manage.py runserver`

Open your browser at: http://127.0.0.1:8000/