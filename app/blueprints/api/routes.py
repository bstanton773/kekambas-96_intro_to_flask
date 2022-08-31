from . import api
from flask import jsonify
from app.models import Post


@api.route('/')
def index():
    names = ['Brian', 'Tatyana', 'Nate', 'Sam']
    return jsonify(names)


@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])


@api.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())
