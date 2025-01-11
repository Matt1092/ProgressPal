# PROGRESSPAL

#### Video Demo
[![ProgressPal Demo](https://img.youtube.com/vi/k3J9H_JxUsM/0.jpg)](https://youtu.be/k3J9H_JxUsM)

### Description
ProgressPal is a full-stack web application I developed with Python and Django on the back-end, alongside a PostgreSQL database hosted through AWS. All code was produced through the CS50 Codespaces.

### Prerequisites
- Python 3.x
- Django
- PostgreSQL
- AWS account

### Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd progresspal
   ```
2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv focus
   source focus/bin/activate   # On Windows use `focus\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Project Structure
### Virtual Environment
- **focus**: This is my dedicated virtual environment for this Django project where all the modules for the project are installed.
### Main Application Folder
- **focusapp**: This is the main folder for this project that contains all the source code needed to run the application.
### Configuration and Settings
- **focusapp/focusapp**: This subdirectory holds important configuration files for the project.
  + **settings.py**:
       + PostgreSQL database configuration, including the database engine, name, user, password, host (Amazon Web Services), and port number (default 5432 for PostgreSQL).
       + Static file configurations to manage compilation and display of static files.
### Static Files
- **focusapp/static**: This is the static folder which contains our main CSS file. Running python manage.py collectstatic transfers our changes in the static files to the production files folder, used for running the web app.
     + **styles.css**: Contains all the stylistic choices for our HTML files in the accounts and tasks apps' respective templates.
### Accounts App
- **focusapp/accounts**: The accounts app is a core component of our project.
     + **apps.py**: Configures the accounts app in the Django project.
     + **models.py**: Defines database models for user accounts stored in the PostgreSQL database.
     + **views.py**: Defines logic for handling user authentication actions in the accounts app, including registration, login, logout, and home page rendering.
          + **UserViewSet**: Added for RESTful API implementation using Django Rest Framework (DRF).
     + **urls.py**: Defines URL routing for the accounts app, mapping URLs to specific view functions for registration, login, and logout.
     + **api_urls.py**: Defines RESTful API endpoints for user management using Django Rest Framework.
          + **UserViewSet**: Registered to handle CRUD operations on users.
     + **Templates**:
          + **main.html**: Homepage of ProgressPal.
          + **login.html**: Form for user login.
          + **register.html**: Form for user registration.
### Tasks App
- **focusapp/tasks**: The tasks app is another core component of our project.
     + **apps.py**: Configures the tasks app in the Django project.
     + **forms.py**: Defines a TaskForm for creating and validating tasks.
     + **models.py**: Defines the database structure for the tasks app, enabling CRUD operations on tasks.
     + **views.py**: Defines logic for handling task actions in the tasks app, including task progress, creation, and completion.
          + **TaskViewSet**: Added for RESTful API implementation using Django Rest Framework (DRF).
          + **task_progress_data**: Sends task data to the frontend in JSON format.
     + **urls.py**: Defines URL routing for the tasks app, mapping URLs to specific view functions for task list, creation, completion, and progress data.
     + **api_urls.py**: Defines RESTful API endpoints for task management using Django Rest Framework.
          + **TaskViewSet**: Registered to handle CRUD operations on tasks.
     + **Templates**:
          + **base.html**: Base structure of the tasks app.
          + **completed_tasks.html**: Displays a list of completed tasks.
          + **create_task.html**: Form for creating tasks.
          + **task_list.html**: Displays a list of current tasks.
          + **task_progress.html**: Interactive graph using Chart.js to visualize task progress.
