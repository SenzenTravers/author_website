from django.urls import reverse

def test_homepage(client):
    url = reverse('homepage')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Autrice M/M & fantasy" in response.content
    assert b"Quoi de neuf ?" in response.content

def test_about(client):
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200
    assert b"propos" in response.content
    assert b"Bibliographie" in response.content

def test_archives_index(client):
    url = reverse('archives:index')
    response = client.get(url)
    assert response.status_code == 200
    assert b"venir" in response.content

def test_404(client):
    url = '/wrong_url'
    response = client.get(url)
    assert b"cette page n'existe pas" in response.content
    assert response.status_code == 200

# @pytest.fixture
# def function_fixture():
#    print('Fixture for each test')
#    return 1


# from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_user_create():
#   User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#   assert User.objects.count() == 1