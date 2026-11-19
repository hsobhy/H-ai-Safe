# H-ai-Safe
## Cybersecurity Awareness Web Application

**Course:** CGC 5003 – Application Programming  
**Project:** Project 2 – Phase 1  
**Semester:** Fall 2026

## 1. Project Overview
H-ai-Safe is a Django-based educational web application designed to improve cybersecurity awareness. It helps users recognize common cyber threats and understand practical ways to protect their digital information.

## 2. Project Objectives
- Raise awareness of common cybersecurity threats.
- Explain the risks associated with online attacks.
- Provide practical cybersecurity safety guidelines.
- Promote safer internet habits.

## 3. Target Audience
Students, beginners, and individuals interested in cybersecurity.

## 4. Application Pages

| Page | URL | Description |
|---|---|---|
| Home | `/` | Dashboard and project statistics |
| Cyber Threats | `/threats/` | Displays five common cyber threats |
| Safety Tips | `/safety-tips/` | Displays five cybersecurity guidelines |
| About | `/about/` | Project vision, objectives, and technologies |

## 5. Technologies Used
- Python
- Django
- HTML
- CSS
- Python mock data

## 6. Mock Data
The application uses sample data stored in `core/data.py`. Django views load the data and pass it to the HTML templates for dynamic display.

The mock data includes:
- Five cybersecurity threats.
- Five safety guidelines.
- Four threat categories.

## 7. Installation and Execution

1. Install Python.
2. Install Django:

   `pip install -r requirements.txt`

3. Run the application:

   `python manage.py runserver`

4. Open the browser at:

   `http://127.0.0.1:8000/`

## 8. Phase 1 Scope
This phase demonstrates a working Django application with four connected frontend pages, navigation, and dynamically displayed mock data.

Database integration, authentication, and advanced interactive features are outside the scope of this phase.

## 9. Project Structure

- `manage.py` – Django management script.
- `config/` – Django project configuration.
- `core/` – Main application.
- `core/data.py` – Mock data.
- `core/views.py` – Page views and data handling.
- `core/urls.py` – Application routes.
- `core/templates/` – HTML pages.
- `core/static/` – CSS styling.
- `PLAN.md` – Project planning document.