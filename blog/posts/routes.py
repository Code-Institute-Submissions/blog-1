from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from blog.posts.forms import CreatePostForm
from blog.models import Post, User

# Exporting post routes.
posts = Blueprint("posts", __name__)

# Post create route.
@posts.route("/post/create", methods=["GET", "POST"])
@login_required
def create_post():
    create_post_form = CreatePostForm()
    author = User.objects(id=current_user.id).first()
    if create_post_form.validate_on_submit():
        # Creating new Post.
        new_post = Post(
            title=create_post_form.title.data,
            content=create_post_form.content.data,
            author=author
        )
        # Saving Post to database.
        new_post.save()
        return redirect(url_for("main.home"))
    return render_template("posts/create_post.html", form=create_post_form)