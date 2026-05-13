import os
import sys

# Add the project directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.contrib.auth.models import User
from registration.models import AdminUser, RegistrationStats

def seed():
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        AdminUser.objects.create(user=user, role='admin')
        print("Superuser 'admin' created with password 'admin123'")
    else:
        print("Superuser 'admin' already exists")
        
    if not RegistrationStats.objects.exists():
        RegistrationStats.objects.create()
        print("RegistrationStats created")
    else:
        print("RegistrationStats already exists")

if __name__ == '__main__':
    seed()
