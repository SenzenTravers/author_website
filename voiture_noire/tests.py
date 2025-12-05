from datetime import date
from django.test import TestCase
from django.urls import reverse
from accounts.models import Member
from .models import DiscordProfile


class DiscordProfilesBirthdatesTestCase(TestCase):
    def setUp(self):
        # Create 3 members
        self.member1 = Member.objects.create_user("user1", email="user1@test.com", password="pass")
        self.member2 = Member.objects.create_user("user2", email="user2@test.com", password="pass")
        self.member3 = Member.objects.create_user("user3", email="user3@test.com", password="pass")
        
        # Create 3 profiles:
        # - One without birthdate
        DiscordProfile.objects.create(member=self.member1, birthday=None)
        # - One with the requested birthdate (2024-12-25)
        DiscordProfile.objects.create(member=self.member2, birthday=date(2024, 12, 25))
        # - One with a different birthdate
        DiscordProfile.objects.create(member=self.member3, birthday=date(2024, 6, 15))

    def test_discord_profiles_birthdates_with_a_requesting_date(self):
        # Request with a specific date
        response = self.client.get(reverse('voiture_noire:birthdates'), {'date': '2024-12-25'})
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Should only return the profile with the matching birthdate
        self.assertEqual(len(data['members_birthdays']), 1)
        self.assertEqual(data['members_birthdays'][0]['member_username'], 'user2')
        self.assertEqual(data['members_birthdays'][0]['birthday'], '2024-12-25')
        self.assertEqual(data['query_date'], '2024-12-25')

    def test_discord_profiles_birthdates_without_a_requesting_date(self):
        # Request without a specific date
        response = self.client.get(reverse('voiture_noire:birthdates'), { })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Should only return the profile with the matching birthdate
        self.assertEqual(len(data['members_birthdays']), 0) 
        self.assertEqual(data['query_date'], date.today().isoformat())