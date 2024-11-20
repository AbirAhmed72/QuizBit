# Display header
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Setting up the QuizBit Django Project  " -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# Activate the virtual environment
# Write-Host "Activating virtual environment..." -ForegroundColor Green
# & "venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# Run database migrations
Write-Host "Applying database migrations..." -ForegroundColor Green
python manage.py migrate

# Seed the database with initial data
Write-Host "Seeding the database with initial data..." -ForegroundColor Green
python manage.py seed_data

# Start the Django development server
Write-Host "Starting the development server..." -ForegroundColor Green
python manage.py runserver
