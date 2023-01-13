from app import app
from utils import *


def test_demo_json():
    response = app.test_client().get('/api/posts')
    assert response == get_posts_all()


def test_demoo_json():
    response1 = app.test_client().get('/api/posts/4')
    print(response1)
    assert response1 == get_post_by_pk(4)
