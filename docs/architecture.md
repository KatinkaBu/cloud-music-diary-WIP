## Cloud Music Diary - System Architecture 


## Current Structure

```
cloud-music-diary/
├── LICENSE
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── routes/
│   │   └── main.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       └── index.html
├── docs/
│   ├── architecture.md
│   └── screenshots/
│       ├── Cloud-Music-Diary-SS-1.png
│       └── Cloud-Music-Diary-SS-2.png
└── tests/
    └── test_basic.py
```


## Folder Responsibilities

app/
Flask backend code, application factory, routes (later Blueprints) and view logic.

app/templates/
HTML templates for rendering the UI.

app/routes/
Route handlers and logic. (Currently empty, to be implemented in Issue 1.)

docs/
Documentation files such as architecture, diagrams and notes.

docs/screenshots/
Stored UI screenshots or visual states.

tests/
Unit or integration tests (planned for later).

requirements.txt
Python dependencies.

README.md
High-level project description, setup instructions, current status and screenshot.


## Backend and Frontend Overview

Frontend:
- Simple Flask-powered HTML interface
- Form for date, mood tag and track
- Display page for entries or timeline
- CSS minimal for now (React optional in future)

Backend:
- Flask for routing and form processing
- SQLite for local development database
- Later integration of Spotify Web API for track metadata
- Later upgrade to PostgreSQL (AWS RDS)
- Optional image upload to S3


## Data and Storage

Phase 1:
- Local SQLite database storing:
- Date
- Mood tag
- Song title + link

Phase 2:
- Migration to AWS RDS PostgreSQL
- Optional S3 bucket for user-uploaded images or static files

---

## Cloud Music Diary - Infrastructure Roadmap

Phase 1 - Local:
- Local development on macOS with Flask + SQLite

Phase 2 - Cloud:
- Deploy Flask app on AWS (EC2 or Elastic Beanstalk)
- RDS PostgreSQL for persistent storage
- S3 for static assets (optional)
- IAM roles for secure access

Phase 3 - Optional, advanced infra:
- Docker containerization
- Terraform for infrastructure as code
- CI/CD pipeline with GitHub Actions

---

## Cloud Music Diary - Project Status

## Current State
- Repository initialized
- Basic project structure created
- First minimal UI (“Cloud Music Diary” placeholder) visible in the browser
- README updated with screenshot and short project status
- Issues for upcoming steps created
- Core Flask folder structure completed (routes, templates, static, tests fully initialized) and first route renders successfully in the browser.
- Added GitHub labels for workflow organization.
- Issue 2 completed: Base template (base.html) implemented using Jinja template inheritance, index page now extends the base template & layout renders correctly in the browser via Flask
- Issue 3 completed: Form (mood, track, artist) added; POST request received and logged in Flask (see Screeshots UI & terminal).

## Planned Next Steps
- Implement Issue 4: local SQLite integration
- Implement Issue 5: Spotify API (PoC)
- Implement Issue 6: Create route to receive and display form data
- Implement Issue 7: README Update + Screenshot + Architektur-Update
- Create deployment pipeline:  
  - Deploy version to Google Cloud  
  - Deploy version to Azure
 
## Stretch Ideas (Post-MVP)
- Mood graph (Chart.js / Plotly)
- Album covers
- Authentication
- Docker (see 'Phase 3 - Optional, advanced infra')
- CI/CD (see 'Phase 3 - Optional, advanced infra')
