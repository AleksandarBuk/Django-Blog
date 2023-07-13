from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')

    def test_register_view_post(self):
        # Test POST request with valid form data
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(self.register_url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/registration_success.html')

        # Check if the user is actually created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_profile_view_post(self):
        # Create a user for testing
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test POST request with valid form data
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            # Add other form fields as required
        }
        response = self.client.post(self.profile_url, form_data)
        self.assertEqual(response.status_code, 302)  # Redirects to 'profile'
        
        # Check if the user's profile has been updated in the database
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_profile_view_get(self):
        # Create a user for testing
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test GET request to the profile view
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')

        # Assert that the user update forms are present in the context
        self.assertIn('u_form', response.context)
        self.assertIn('p_form', response.context)
