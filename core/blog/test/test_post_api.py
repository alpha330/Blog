from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
import pytest
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="ali@ali.com", password="123qwe!@#", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    def test_get_response_401_status(self, api_client):
        url = reverse("blog:api_v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_get_response_200_status(self, api_client, common_user):
        user = common_user
        api_client.force_login(user=user)
        url = reverse("blog:api_v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self, api_client):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test mode test",
            "content": "test reason to write",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201(self, api_client, common_user):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test mode test",
            "content": "test reason to write",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400(self, api_client, common_user):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test mode test",
            "content": "test reason to write",
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
