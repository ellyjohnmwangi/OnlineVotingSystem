# Online Voting System

A Django-based online voting application for university elections. It allows administrators to define positions and candidates, and provides a web interface for students to participate in elections remotely.

## Tech Stack

- Python 3
- Django
- SQLite (default Django database)

## Project Structure

- `manage.py` - Django management entry point.
- `Voting_System/` - project settings and root URL configuration.
- `Candidates/` - main app containing models, views, URL routes, and admin registration.
- `templates/` - base and index templates.

## Prerequisites

- Python 3.8+ installed
- `pip` available

## Setup

1. Clone the repository and move into it:

   ```bash
   git clone https://github.com/ellyjohnmwangi/OnlineVotingSystem.git
   cd OnlineVotingSystem
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows (PowerShell):

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. (Optional) Create an admin user:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the app in your browser:

   - Main site: `http://127.0.0.1:8000/`
   - Admin portal: `http://127.0.0.1:8000/admin/`

## Current Routes

- `/` - index page.
- `/admin/` - Django admin interface.

## Development Notes

- Static/media settings are configured in `Voting_System/settings.py` and URL routing in `Voting_System/urls.py`.
- Candidate, position, and profile models are defined in `Candidates/models.py`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This repository currently does not include a formal open-source license file.
