import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class TextHelper:
    """
    A class that provides helper functions for generating product search queries and descriptions.
    """

    @staticmethod
    def get_product_search_queries(product_name: str) -> str:
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

        PRODUCT_SEARCH_QUERY_PROMPT = f"""Need search queries for {product_name}:
    Use only those queries that will be used to search for your product.
    For example, long women's dress, green dress, cotton green dress...
    Enter the search terms separated by commas. The more queries you add, the better your product will appear.
    Do not use additional words like "buy", "order", "region" - they are added automatically.
    And make this queries in one line but separated with coma.
    """
        ai_response = openai.Completion.create(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=PRODUCT_SEARCH_QUERY_PROMPT,
            max_tokens=2000,
        )

        return ai_response["choices"][0]["text"]

    @staticmethod
    def get_product_description(product_name: str) -> str:
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

        PRODUCT_DESCRIPTION_PROMPT = f"""
        Write a promo description for the {product_name}. It should be concise, moderately brief, and salesy. 
        Try to keep it to 2-3 paragraphs and about 100 words. 
        Highlight the name of the product, and in the output, leave only the product description, without your own comments.
        """
        ai_response = openai.Completion.create(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=PRODUCT_DESCRIPTION_PROMPT,
            max_tokens=2000,
        )

        return ai_response["choices"][0]["text"]

    @staticmethod
    def get_category_search_queries(category_name: str) -> str:
        """
        Generate search tags for the given product category.
        These tags should be adapted for the e-commerce site.
        Return only the search tags themselves, separated by a comma and on a single line.

        Args:
        category_name (str): The name of the product category.

        Returns:
        str: A string containing the generated search tags."""

        CATEGORY_SEARCH_QUERIES_PROMPT = f"""
        Generate search tags for product category {category_name}. 
        These tags should be adapted for the e-commerce site. 
        Return only the search tags themselves, without their own comments, on a single line and separated by a comma.
        """
        ai_response = openai.Completion.create(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=CATEGORY_SEARCH_QUERIES_PROMPT,
            max_tokens=2000,
        )

        return ai_response["choices"][0]["text"]

    @staticmethod
    def get_category_description(category_name: str) -> str:
        """
        Generate a description for the given product group. The description should not be redundant but should sell. Try to keep it to 2-3 paragraphs and about 100 words. Return only the description itself, without your own comments.

        Args:
        category_name (str): The name of the product group.

        Returns:
        str: A string containing the generated product group description."""

        CATEGORY_DESCRIPTION_PROMPT = f"""
        Generate a description for a product group {category_name}. 
        The description should not be redundant, but it should sell.
        Try to keep it to 2-3 paragraphs and about 100 words.  
        Return only the description itself, without your own comments.
        """
        ai_response = openai.Completion.create(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=CATEGORY_DESCRIPTION_PROMPT,
            max_tokens=2000,
        )

        return ai_response["choices"][0]["text"]
