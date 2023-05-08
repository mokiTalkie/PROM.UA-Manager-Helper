from flask import Blueprint, jsonify, render_template, request

from external_api.openai_api import TextHelper

tools = Blueprint("tool", __name__, url_prefix="/tool/")


@tools.get("/product")
def product_load() -> str:
    return render_template("main_template.html", content=render_template("tool.html"))


@tools.post("/product")
def generate_product() -> str:
    user_input = request.form.get("input")
    product_tags = TextHelper.get_product_search_queries(product_name=user_input)
    product_description = TextHelper.get_product_description(product_name=user_input)
    return jsonify(
        {"tags": product_tags.strip(), "description": product_description.strip()}
    )


@tools.get("/category")
def category_load() -> str:
    return render_template("main_template.html", content=render_template("tool.html"))

