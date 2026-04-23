from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Member  
from voiture_noire.models import ExchangeParticipant


class BannerTestCase(TestCase):
    def setUp(self):
        Member.objects.create_user('NoDiscordProfile', email='luciedupont@mail.fr', password='motdepasse')
        user_with_discord = Member.objects.create_user('HasDiscordProfile', email='jeannedurant@mail.fr', password='motdepasse')
        ExchangeParticipant.objects.create(member=user_with_discord, is_creator=False)

    def test_banner_not_logged_in(self):
        response = self.client.get(reverse('voiture_noire:index'))

        self.assertContains(response, 'Se connecter</a></li>')
        self.assertNotContains(response, 'Thèmes</a></li>')
        self.assertNotContains(response, 'Membres</a></li>')
        self.assertNotContains(response, 'Mon profil</a></li>')
        self.assertEqual(response.status_code, 200)

    def test_banner_no_discord_profile(self):
        test_client = Client()
        test_client.login(username='NoDiscordProfile', password='motdepasse')
        response = test_client.get(reverse('voiture_noire:index'))

        self.assertContains(response, 'Se déconnecter</button>')
        self.assertNotContains(response, 'Thèmes</a></li>')
        self.assertNotContains(response, 'Membres</a></li>')
        self.assertNotContains(response, 'Mon profil</a></li>')
        self.assertEqual(response.status_code, 200)

    def test_banner_with_discord_profile(self):
        test_client = Client()
        test_client.login(username='HasDiscordProfile', password='motdepasse')
        response = test_client.get(reverse('voiture_noire:index'))

        self.assertContains(response, 'Se déconnecter</button>')
        self.assertContains(response, 'Thèmes</a></li>')
        self.assertContains(response, 'Membres</a></li>')
        self.assertContains(response, 'Mon profil</a></li>')
        self.assertEqual(response.status_code, 200)