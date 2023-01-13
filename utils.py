import json
import os


def get_posts_all():
    with open(os.path.join("data", "posts.json"), 'r', encoding='utf-8') as f:
        posts = json.load(f)
    return posts


def get_posts_by_user(user_name):
    text = get_posts_all()
    spisok = []
    try:
        for i in text:
            if i['poster_name'] == user_name:
                spisok.append(i)
        return spisok
    except ValueError:
        return []


def get_comments_by_post_id(post_id):
    spisok = []
    with open(os.path.join("data", "comments.json"), 'r', encoding='utf-8') as f:
        comments = json.load(f)
    try:
        for i in comments:
            if i['post_id'] == post_id:
                spisok.append(i)
        return spisok
    except ValueError:
        return []


def search_for_posts(query):
    list_posts = []
    text = get_posts_all()
    for i in text:
        if query in i['content']:
            list_posts.append(i)
    return list_posts


def get_post_by_pk(pk):
    text = get_posts_all()
    for i in text:
        if i['pk'] == pk:
            return i


def get_bookmarks():
    with open(os.path.join("data", "bookmarks.json"), 'r', encoding='utf-8') as f:
        bookmarks = json.load(f)
    return bookmarks


def get_comments():
    with open(os.path.join("data", "comments.json"), 'r', encoding='utf-8') as f:
        comments = json.load(f)
    return comments
