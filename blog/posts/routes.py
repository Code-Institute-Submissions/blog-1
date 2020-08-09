from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from blog.posts.forms import CreateOrUpdatePostForm
from blog.models import Post, User

# Exporting post routes.
posts = Blueprint("posts", __name__)

# Post create route.
@posts.route("/post/create", methods=["GET", "POST"])
@login_required
def create_post():
    create_post_form = CreateOrUpdatePostForm()
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
    return render_template("posts/create_or_update_post.html", form=create_post_form, legend="New Post")

# Post update route.
@posts.route("/post/<post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    update_form = CreateOrUpdatePostForm()
    post = Post.objects.get_or_404(id=post_id)
    if update_form.validate_on_submit():
        post.title = update_form.title.data
        post.content = update_form.content.data
        post.save()
        return redirect(url_for("main.home"))
    # Populating form.
    elif request.method == "GET":
        update_form.title.data = post.title
        update_form.content.data = post.content
    return render_template("posts/create_or_update_post.html", form=update_form, legend="Update Post")

# Post delete route.
@posts.route("/post/<post_id>/delete", methods=["GET"])
@login_required
def delete_post(post_id):
    post = Post.objects.get_or_404(id=post_id)
    post.delete()
    return redirect(url_for("main.home"))