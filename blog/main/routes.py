from flask import Blueprint, render_template, request
from blog.models import Post

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    # Sort posts by date in decending order.
    page = request.args.get("page", 1, type=int)
    posts = Post.objects.order_by("-date").paginate(page=page, per_page=10)
    return render_template("main/home.html", posts=posts)