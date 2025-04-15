from django.urls import reverse
from django.test import Client, TestCase
from voiture_noire.models import DiscordMember


class VoitureNoireTestCase(TestCase):
    # Views
    def setUp(self):
        DiscordMember.objects.create_user("Jean-Bob", email="jeanbobdupont@mail.fr", password="motdepasse")

    def test_voiture_noire_view(self):
        response = self.client.get(reverse("voiture_noire:index"))
        self.assertContains(response, 'La bibliothèque de la Petite Voiture Noire')
        self.assertEqual(response.status_code, 200)

    def test_voiture_noire_prompts_get_unlogged(self):
        response = self.client.get(reverse("voiture_noire:prompts"))
        self.assertContains(response, 'Les thèmes de la Petite Voiture Noire')
        self.assertEqual(response.status_code, 302)

    def test_voiture_noire_profile_get_unlogged(self):
        response = self.client.get(reverse("voiture_noire:profile"))
        self.assertContains(response, 'Votre profil')
        self.assertEqual(response.status_code, 302)

    def test_voiture_noire_prompts_get_logged(self):
        test_client = Client()
        test_client.login(username="Jean-Bob", password="motdepasse")
        response = test_client.get(reverse("voiture_noire:prompts"))
        self.assertContains(response, 'Les thèmes de la Petite Voiture Noire')
        self.assertEqual(response.status_code, 200)