from flask import Blueprint, render_template
from blog.models import Post

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    posts = Post.objects()
    return render_template("main/home.html", posts=posts)