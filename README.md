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

### Project Structure
# Virtual Environment
- **focus**: This is my dedicated virtual environment for this Django project where all the modules for the project are installed.
# Main Application Folder
- **focusapp**: This is the main folder for this project that contains all the source code needed to run the application.
# Configuration and Settings
- **focusapp/focusapp**: This subdirectory holds important configuration files for the project.
  + hello
