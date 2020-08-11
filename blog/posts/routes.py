from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from blog.posts.forms import CreateOrUpdatePostForm
from blog.comments.forms import CommentForm
from blog.models import Post, User, Comment

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
    return render_template("posts/create_or_update_post.html", form=create_post_form, legend="New Post", title="New Post")

# Post update route.
@posts.route("/post/<post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    update_form = CreateOrUpdatePostForm()
    post = Post.objects.get_or_404(id=post_id)
    # Forbids other users to update posts.
    if post.author != current_user:
        abort(403)
    if update_form.validate_on_submit():
        post.title = update_form.title.data
        post.content = update_form.content.data
        post.save()
        flash("Your post has been updated.", "success")
        return redirect(url_for("posts.comment_post", post_id=post_id))
    # Populating form.
    elif request.method == "GET":
        update_form.title.data = post.title
        update_form.content.data = post.content
    return render_template("posts/create_or_update_post.html", form=update_form, legend="Update Post", title="Update Post")

# Post delete route.
@posts.route("/post/<post_id>/delete", methods=["GET"])
@login_required
def delete_post(post_id):
    # Deleting post and all related comments to it.
    post = Post.objects.get_or_404(id=post_id)
    # Forbids other users to delete posts.
    if post.author != current_user:
        abort(403)
    comments = Comment.objects(post=post)
    post.delete()
    comments.delete()
    flash("Your post has been deleted.", "danger")
    return redirect(url_for("main.home"))

# Comment post route.
@posts.route("/post/<post_id>", methods=["GET", "POST"])
@login_required
def comment_post(post_id):
    page = request.args.get("page", 1, type=int)
    post = Post.objects.get_or_404(id=post_id)
    comments = Comment.objects(post=post).order_by("-date").paginate(page=page, per_page=2)
    comment_form = CommentForm()
    comment_author = User.objects(id=current_user.id).first()
    if comment_form.validate_on_submit():
        new_comment = Comment(
            author=comment_author,
            post=post,
            content=comment_form.content.data
        )
        new_comment.save()
        return redirect(url_for("posts.comment_post", post_id=post_id))
    return render_template("posts/comment_post.html", post=post, form=comment_form, comments=comments, title="Post")