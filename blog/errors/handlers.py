from flask import Blueprint, render_template, redirect, url_for, flash

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html"), 404

@errors.app_errorhandler(401)
def error_401(error):
    flash("Please login to access that page.", "warning")
    return redirect(url_for("users.login"))

@errors.app_errorhandler(403)
def error_404(error):
    return render_template("errors/403.html"), 403

@errors.app_errorhandler(500)
def error_404(error):
    return render_template("errors/500.html"), 500