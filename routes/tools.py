from flask import Blueprint, jsonify, render_template, request
import asyncio
from external_api.openai_api import TextHelper
from templates.text_templates import (
    PRODUCT_TOOL_HEAD,
    PRODUCT_TOOL_DESCRIPTION,
    CATEGORY_TOOL_HEAD,
    CATEGORY_TOOL_DESCRIPTION,
)

tools = Blueprint("tool", __name__, url_prefix="/tool/")


@tools.get("/product")
def product_load() -> str:
    return render_template(
        "main_template.html",
        route_product="product",
        route_category="category",
        content=render_template(
            "tool.html",
            source="product",
            tool_header=PRODUCT_TOOL_HEAD,
            tool_description=PRODUCT_TOOL_DESCRIPTION,
        ),
    )


async def async_ai_request_for_product(user_input: str) -> list[str]:
    return await asyncio.gather(
        TextHelper.get_product_search_queries(product_name=user_input),
        TextHelper.get_product_description(product_name=user_input),
    )


@tools.post("/product")
def generate_product() -> str:
    user_input = request.form.get("input")
    ai_response = asyncio.run(async_ai_request_for_product(user_input=user_input))
    return jsonify(
        {"tags": ai_response[0].strip(), "description": ai_response[1].strip()}
    )


@tools.get("/category")
def category_load() -> str:
    return render_template(
        "main_template.html",
        route_product="product",
        route_category="category",
        content=render_template(
            "tool.html",
            source="category",
            tool_header=CATEGORY_TOOL_HEAD,
            tool_description=CATEGORY_TOOL_DESCRIPTION,
        ),
    )


async def openai_request_for_category(user_input: str) -> list[str]:
    return await asyncio.gather(
        TextHelper.get_category_search_queries(category_name=user_input),
        TextHelper.get_category_description(category_name=user_input),
    )


@tools.post("/category")
def generate_category() -> str:
    user_input = request.form.get("input")
    ai_response = asyncio.run(openai_request_for_category(user_input=user_input))
    return jsonify(
        {"tags": ai_response[0].strip(), "description": ai_response[1].strip()}
    )
