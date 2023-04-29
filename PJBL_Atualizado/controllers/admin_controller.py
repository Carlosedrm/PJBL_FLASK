from flask import Blueprint

admin = Blueprint("admin", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@admin.route("/")
def admin_index():
    return "Admin Blueprint"