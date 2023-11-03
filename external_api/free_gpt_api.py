import g4f
from g4f.models import gpt_35_turbo

from templates.text_templates import (
    CATEGORY_DESCRIPTION_PROMPT,
    CATEGORY_SEARCH_QUERIES_PROMPT,
    PRODUCT_DESCRIPTION_PROMPT,
    PRODUCT_SEARCH_QUERY_PROMPT,
)


class FreeGPTTextHelper:
    """
    A class that provides helper functions for generating product search queries and descriptions.
    """

    @staticmethod
    async def get_product_search_queries(product_name: str) -> str:
        """
        Generates search queries for a given product using FreeGPT's text generation API.

        Parameters:
        -----------
        product : str
            The name of the product for which to generate search queries.

        Returns:
        --------
        str
            A string containing the generated search queries."""

        ai_response = await g4f.ChatCompletion.create_async(
            model=gpt_35_turbo,
            messages=[
                {
                    "role": "user",
                    "content": PRODUCT_SEARCH_QUERY_PROMPT.format(product_name),
                }
            ],
        )

        return ai_response

    @staticmethod
    async def get_product_description(product_name: str) -> str:
        """
        Generates a promotional description for a given product using FreeGPT's text generation API.

        Parameters:
        -----------
        product : str
            The name of the product for which to generate a promotional description.

        Returns:
        --------
        str
            A string containing the generated promotional description.
        """

        ai_response = await g4f.ChatCompletion.create_async(
            model=gpt_35_turbo,
            messages=[
                {
                    "role": "user",
                    "content": PRODUCT_DESCRIPTION_PROMPT.format(product_name),
                }
            ],
        )

        return ai_response

    @staticmethod
    async def get_category_search_queries(category_name: str) -> str:
        """
        Generate search tags for the given product category.
        These tags should be adapted for the e-commerce site.
        Return only the search tags themselves, separated by a comma and on a single line.

        Args:
        category_name (str): The name of the product category.

        Returns:
        str: A string containing the generated search tags."""

        ai_response = await g4f.ChatCompletion.create_async(
            model=gpt_35_turbo,
            messages=[
                {
                    "role": "user",
                    "content": CATEGORY_SEARCH_QUERIES_PROMPT.format(category_name),
                }
            ],
        )

        return ai_response

    @staticmethod
    async def get_category_description(category_name: str) -> str:
        """
        Generate a description for the given product group. The description should not be redundant but should sell. Try to keep it to 2-3 paragraphs and about 100 words. Return only the description itself, without your own comments.

        Args:
        category_name (str): The name of the product group.

        Returns:
        str: A string containing the generated product group description."""

        ai_response = await g4f.ChatCompletion.create_async(
            model=gpt_35_turbo,
            messages=[
                {
                    "role": "user",
                    "content": CATEGORY_DESCRIPTION_PROMPT.format(category_name),
                }
            ],
        )

        return ai_response
