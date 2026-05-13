from django.test import TestCase
from .models import Registration

class RegistrationModelTest(TestCase):
    def test_create_registration(self):
        reg = Registration.objects.create(
            full_name='Ahmed Ali',
            age=25,
            gender='M',
            id_number='1234567890',
            nationality='Saudi',
            phone='0500000000',
            email='ahmed@example.com',
            category='D',
            has_driving_license=True,
            has_sports_license=False,
            has_previous_experience=False,
            desert_driving_rating=3,
            program_goal='Win Dakar',
            committed_to_5_days=True,
            residence_region='riyadh',
            can_travel=True
        )
        self.assertEqual(reg.status, 'P')
        self.assertEqual(reg.full_name, 'Ahmed Ali')
