import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_login_prevents_sql_injection(client, django_user_model):
    username = "testuser"
    password = "securepassword123"
    django_user_model.objects.create_user(username=username, password=password)

    sql_injection_input = "' OR 1=1; --"
    response = client.post(
        reverse('login'),
        {
            "username": sql_injection_input,
            "password": sql_injection_input,
        }
    )

    assert response.status_code == 200
    assert b"Oops!" in response.content


@pytest.mark.django_db
def test_login_prevents_xss(client, django_user_model):
    username = "testuser"
    password = "securepassword123"
    django_user_model.objects.create_user(username=username, password=password)

    xss_input = "<script>alert('XSS')</script>"
    response = client.post(
        reverse('login'),
        {
            "username": xss_input,
            "password": password,
        }
    )

    assert response.status_code == 200
    assert xss_input not in response.content.decode()


@pytest.mark.django_db
def test_login_prevents_broken_authentication(client, django_user_model):
    username = "testuser"
    password = "securepassword123"
    django_user_model.objects.create_user(username=username, password=password)

    response = client.post(
        reverse('login'),
        {
            "username": "wronguser",
            "password": "wrongpassword",
        }
    )

    assert response.status_code == 200
    assert b"Invalid username or password" in response.content


@pytest.mark.django_db
def test_login_does_not_expose_sensitive_data(client, django_user_model):
    username = "testuser"
    password = "securepassword123"
    django_user_model.objects.create_user(username=username, password=password)

    response = client.post(
        reverse('login'),
        {
            "username": username,
            "password": password,
        }
    )

    assert response.status_code == 200
    assert b"password" not in response.content


@pytest.mark.django_db
def test_login_prevents_idor(client, django_user_model):
    user1 = django_user_model.objects.create_user(username="user1", password="password123")
    user2 = django_user_model.objects.create_user(username="user2", password="password123")

    client.login(username="user1", password="password123")
    
    response = client.get(reverse('profile', args=[user2.id]))
    
    assert response.status_code == 403  # Acceso denegado
