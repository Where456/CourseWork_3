import logging
from flask import Flask, render_template, request
from utils import *
from get_data_json import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)

logging.basicConfig(filename='logs/api.log', level=logging.INFO, filemode="w",
                    format='%(asctime)s [%(levelname)s] %(message)s')


@app.route("/")
def main_page():
    logging.info('Главная страница запрошена')
    bookmarks = get_bookmarks()
    text = get_posts_all()
    return render_template('index.html', text=text, bookmarks=bookmarks)


@app.route("/posts/<int:postid>")
def page_post(postid):
    logging.info('Запрос по посту')
    f = get_comments_by_post_id(postid)
    text = get_post_by_pk(postid)
    return render_template('post.html', comments=f, post=text)


@app.route("/search/")
def page_search():
    logging.info('Запрос поиска')
    w = request.args.get('s')
    word = search_for_posts(w)
    return render_template('search.html', word=word)


@app.route("/users/<username>")
def page_user(username):
    logging.info('Запрос по имени')
    names = get_posts_by_user(username)
    return render_template('user-feed.html', names=names)


@app.errorhandler(404)
def not_found_error(e):
    return 'Сервер не найден'


@app.errorhandler(500)
def internal_error(e):
    return 'Внутренняя ошибка сервера'


app.run()
