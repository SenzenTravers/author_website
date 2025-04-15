from django.urls import reverse
from django.test import Client, TestCase
from voiture_noire.models import DiscordMember


class CoreTestCase(TestCase):
    # Views
    def setUp(self):
        DiscordMember.objects.create_user("Jean-Bob", email="jeanbobdupont@mail.fr", password="motdepasse")

    def test_call_view_fail_blank(self):
        #response = self.client.post('/url/to/view', {}) # blank data dictionary
        response = self.client.get('/url/to/view') # blank data dictionary
        self.assertContains(response, 'Malheureusement, cette page n\'existe pas !')
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, 'Autrice M/M | Romans BL et fantasy')
        self.assertContains(response, 'Aux nouvelles')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, 'Bibliographie')
        self.assertEqual(response.status_code, 200)

    def test_archives_view(self):
        response = self.client.get(reverse("archives:index"))
        self.assertContains(response, 'Fics M/M et F/F')
        self.assertEqual(response.status_code, 200)

    def test_gadget_view(self):
        response = self.client.get(reverse("gadgets:index"))
        self.assertContains(response, 'Coquecigrues : trucs, gadgets et machins')
        self.assertEqual(response.status_code, 200)




    # def setUp(self):
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')
    #     url = reverse('homepage')

    # def test_call_view_deny_anonymous(self):
    #     response = self.client.get('/url/to/view', follow=True)
    #     self.assertRedirects(response, '/login/')
    #     response = self.client.post('/url/to/view', follow=True)
    #     self.assertRedirects(response, '/login/')

    # def test_call_view_load(self):
    #     self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
    #     response = self.client.get('/url/to/view')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'conversation.html')

    # def test_call_view_fail_invalid(self):
    #     # as above, but with invalid rather than blank data in dictionary

    # def test_call_view_success_invalid(self):
    #     # same again, but with valid data, then
    #     self.assertRedirects(response, '/contact/1/calls/')

