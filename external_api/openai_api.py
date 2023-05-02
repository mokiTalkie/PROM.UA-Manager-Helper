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
    def get_product_search_queries(product: str) -> str:
        '''
        Generates search queries for a given product using OpenAI's text generation API.

        Parameters:
        -----------
        product : str
            The name of the product for which to generate search queries.

        Returns:
        --------
        str
            A string containing the generated search queries.'''
        PRODUCT_SEARCH_QUERY_PROMPT = f"""Need search queries for {product}:
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
    def get_product_description(product: str) -> str:
        '''
        Generates a promotional description for a given product using OpenAI's text generation API.

        Parameters:
        -----------
        product : str
            The name of the product for which to generate a promotional description.

        Returns:
        --------
        str
            A string containing the generated promotional description.
        '''
        PRODUCT_DESCRIPTION_PROMPT = f"""
        Write a promo description for the {product}. It should be concise, moderately brief, and salesy. 
        Try to keep it to 2-3 paragraphs and about 100 words. 
        Highlight the name of the product, and in the output, leave only the product description, without your own comments.
        """
        ai_response = openai.Completion.create(
            engine=os.getenv("AI_TEXT_MODEL"),
            prompt=PRODUCT_DESCRIPTION_PROMPT,
            max_tokens=2000,
        )

        return ai_response["choices"][0]["text"]
