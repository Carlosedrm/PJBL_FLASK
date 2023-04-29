from re import template
from flask import Blueprint, render_template,redirect,url_for,request

iot = Blueprint("iot", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/Iot.html")