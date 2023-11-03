import asyncio

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse

# from external_api.openai_api import OpenAITextHelper
from external_api.free_gpt_api import FreeGPTTextHelper
from routes import UserInput, templates

tools = APIRouter(prefix="/tools")


async def async_ai_request_for_product(user_input: str) -> list[str]:
    """
    Retrieves product search queries and descriptions for a given product name.

    Args:
        user_input (str): A string containing the name of the product to search for.

    Returns:
        A list of strings containing the search queries and descriptions for the specified product.
    """

    return await asyncio.gather(
        FreeGPTTextHelper.get_product_search_queries(product_name=user_input),
        FreeGPTTextHelper.get_product_description(product_name=user_input),
    )


async def openai_request_for_category(user_input: str) -> list[str]:
    """
    Send a request to the OpenAI API to get search queries and description for a given category.

    Args:
        user_input: A string representing the name of the category to search for.

    Returns:
        A list of two strings, representing the search queries and description for the specified category.
    """

    return await asyncio.gather(
        FreeGPTTextHelper.get_category_search_queries(category_name=user_input),
        FreeGPTTextHelper.get_category_description(category_name=user_input),
    )


@tools.get("/product")
async def get_product_page(request: Request) -> HTMLResponse:
    """
    Handler to return the HTML page for the product search tool.

    Args:
        request: FastAPI Request object.

    Returns:
        The rendered HTML template for the product search tool.
    """
    return templates.TemplateResponse(
        name="product_tool.html", context={"request": request}
    )


@tools.post("/product")
async def generate_product(user_input: UserInput) -> JSONResponse:
    """
    Handler to generate the AI response for the product search tool.

    Args:
        user_input: UserInput object containing the user's input.

    Returns:
        The AI response as a JSON response.
    """
    ai_response = await async_ai_request_for_product(user_input.input)
    return JSONResponse(
        {"tags": ai_response[0].strip(), "description": ai_response[1].strip()}
    )


@tools.get("/category")
async def get_category_page(request: Request) -> HTMLResponse:
    """
    Handler to return the HTML page for the category search tool.

    Args:
        request: FastAPI Request object.

    Returns:
        The rendered HTML template for the category search tool.
    """
    return templates.TemplateResponse(
        name="category_tool.html", context={"request": request}
    )


@tools.post("/category")
async def generate_category(user_input: UserInput) -> JSONResponse:
    """
    Handler to generate the AI response for the category search tool.

    Args:
        user_input: UserInput object containing the user's input.

    Returns:
        The AI response as a JSON response.
    """
    ai_response = await openai_request_for_category(user_input.input)
    return JSONResponse(
        {"tags": ai_response[0].strip(), "description": ai_response[1].strip()}
    )


@tools.post("/repeat")
async def repeat_request(user_input: UserInput) -> str:
    match user_input.target:
        case "product_tags":
            ai_response = await FreeGPTTextHelper.get_product_search_queries(
                product_name=user_input.input
            )
            return JSONResponse({"text": ai_response})
        case "product_description":
            ai_response = await FreeGPTTextHelper.get_product_description(
                product_name=user_input.input
            )
            return JSONResponse({"text": ai_response})
        case "category_tags":
            ai_response = await FreeGPTTextHelper.get_category_search_queries(
                category_name=user_input.input
            )
            return JSONResponse({"text": ai_response})
        case "category_description":
            ai_response = await FreeGPTTextHelper.get_category_description(
                category_name=user_input.input
            )
            return JSONResponse({"text": ai_response})
        case _:
            return
