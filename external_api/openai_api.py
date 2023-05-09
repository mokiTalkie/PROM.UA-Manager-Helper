import os

import openai
from dotenv import load_dotenv

from templates.text_templates import (CATEGORY_DESCRIPTION_PROMPT,
                                      CATEGORY_SEARCH_QUERIES_PROMPT,
                                      PRODUCT_DESCRIPTION_PROMPT,
                                      PRODUCT_SEARCH_QUERY_PROMPT)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class TextHelper:
    """
    A class that provides helper functions for generating product search queries and descriptions.
    """

    @staticmethod
    async def get_product_search_queries(product_name: str) -> str:
        """
        Generates search queries for a given product using OpenAI's text generation API.

        Parameters:
        -----------
        product : str
            The name of the product for which to generate search queries.

        Returns:
        --------
        str
            A string containing the generated search queries."""

        ai_response = await openai.Completion.acreate(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=PRODUCT_SEARCH_QUERY_PROMPT.format(product_name),
            temperature=0.5,
            max_tokens=2000,
            n=1,
            stop=None,
            timeout=None,
            presence_penalty=0.0,
            frequency_penalty=0.0,
            best_of=1,
            # user=None,
            logprobs=None,
            echo=False
        )

        return ai_response["choices"][0]["text"]

    @staticmethod
    async def get_product_description(product_name: str) -> str:
        """
        Generates a promotional description for a given product using OpenAI's text generation API.

        Parameters:
        -----------
        product : str
            The name of the product for which to generate a promotional description.

        Returns:
        --------
        str
            A string containing the generated promotional description.
        """

        ai_response = await openai.Completion.acreate(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=PRODUCT_DESCRIPTION_PROMPT.format(product_name),
            temperature=0.5,
            max_tokens=2000,
            n=1,
            stop=None,
            timeout=None,
            presence_penalty=0.0,
            frequency_penalty=0.0,
            best_of=1,
            # user=None,
            logprobs=None,
            echo=False
        )

        return ai_response["choices"][0]["text"]

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

        ai_response = await openai.Completion.acreate(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=CATEGORY_SEARCH_QUERIES_PROMPT.format(category_name),
            max_tokens=2000,
            temperature=0.5,
            n=1,
            stop=None,
            timeout=None,
            presence_penalty=0.0,
            frequency_penalty=0.0,
            best_of=1,
            # user=None,
            logprobs=None,
            echo=False
        )

        return ai_response["choices"][0]["text"]

    @staticmethod
    async def get_category_description(category_name: str) -> str:
        """
        Generate a description for the given product group. The description should not be redundant but should sell. Try to keep it to 2-3 paragraphs and about 100 words. Return only the description itself, without your own comments.

        Args:
        category_name (str): The name of the product group.

        Returns:
        str: A string containing the generated product group description."""

        ai_response = await openai.Completion.acreate(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=CATEGORY_DESCRIPTION_PROMPT.format(category_name),
            max_tokens=2000,
            temperature=0.5,
            n=1,
            stop=None,
            timeout=None,
            presence_penalty=0.0,
            frequency_penalty=0.0,
            best_of=1,
            # user=None,
            logprobs=None,
            echo=False
        )

        return ai_response["choices"][0]["text"]
