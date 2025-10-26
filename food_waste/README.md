# Food Waste App - Django Backend (Scaffold)

## What's included
- Django project `food_waste_backend`
- App `api` with models: FoodItem, Donation
- Django REST Framework serializers and ViewSets
- JWT auth using `djangorestframework-simplejwt` (setup included in settings)
- Example Dockerfile and docker-compose stub
- `requirements.txt` listing packages

## Quickstart (local)
1. Create a Python environment (Python 3.10+ recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables (use `.env`):
   - `DJANGO_SECRET_KEY`
   - `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` (if using Postgres)
   - Or use SQLite (default settings use sqlite for quick dev)
4. Run migrations and start server:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
5. API root: `http://127.0.0.1:8000/api/`

## Notes & Next steps
- Fill in production settings (ALLOWED_HOSTS, DEBUG=False, secure DB)
- Configure email, storage, and push notifications if needed
- I can expand this scaffold into a fully working repo with CI, unit tests, and deployment instructions — tell me which you'd like next.
