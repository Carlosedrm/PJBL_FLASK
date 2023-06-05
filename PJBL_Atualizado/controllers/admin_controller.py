from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth.user import User
from models.db import db

admin = Blueprint("admin", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@admin.route("/")
def admin_index():
    return render_template("/admin/admin_index.html")
