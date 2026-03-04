# Personal Music Diary

A cloud-based web application to track daily mood through music.
Built with Python and Flask, with planned cloud deployment on AWS.

## Project Idea

Users select a daily mood and add a song.
Entries are stored and displayed as a simple timeline.

Each entry includes:
- Date
- Mood tag
- Song title and link
- Optional image

---

## Architecture Overview

**Phase 1: Local MVP**
- Flask (Python)
- SQLite
- HTML templates
- Basic timeline view

**Phase 2: Cloud Deployment**
- AWS EC2 (App hosting)
- AWS RDS (PostgreSQL)
- S3 (optional image storage)
- IAM roles

---

## Project Roadmap

**MVP:**
- Input form for daily mood and track
- Local SQLite persistence
- Timeline view for stored entries

**Cloud:**
- PostgreSQL via AWS RDS
- Deployment on AWS EC2

**Optional:**
- Spotify API integration
- Docker containerization
- CI/CD with GitHub Actions
- Mood visualization (Chart.js / Plotly)
- User authentication (Cognito)
- Hybrid timeline and album-art view
- Terraform IaC deployment

--- 

## Tech Stack
- Python + Flask
- SQLite / PostgreSQL
- AWS (EC2, RDS, S3, IAM)
- GitHub

---

## Status 
Development began in November 2025 and is ongoing.

**Current Progress (MVP Phase 1):**
- Flask base structure completed
- First route rendering successfully
- Project structure and documentation initialized
- GitHub issues and labels organized
- Base template implemented (Jinja template inheritance)
- Index page connected to base template
![First UI Screenshot](docs/screenshots/Cloud-Music-Diary-SS-1.png)

**Next:**
- Implement form submission
- Add SQLite persistence
- Build timeline view

---

## Contact

Feel free to connect via GitHub or LinkedIn. 
