PRODUCT_TOOL_HEAD = "Генератор опису товару"
PRODUCT_TOOL_DESCRIPTION = "Представляємо наш потужний інструмент на основі штучного інтелекту, який генерує переконливі описи товарів та ефективні пошукові запити за лічені секунди!"

CATEGORY_TOOL_HEAD = "Генератор опису категорії"
CATEGORY_TOOL_DESCRIPTION = "Представляємо вам наш генератор описів категорій на основі штучного інтелекту - просто введіть назву вашої категорії і дозвольте нашій моделі виконати роботу по створенню високоякісних, переконливих описів для ваших категорій товарів."

PRODUCT_SEARCH_QUERY_PROMPT = """Need search queries for {}:
    Use only those queries that will be used to search for your product.
    For example, long women's dress, green dress, cotton green dress...
    Enter the search terms separated by commas. The more queries you add, the better your product will appear.
    Do not use additional words like "buy", "order", "region" - they are added automatically.
    And make this queries in one line but separated with coma.
    In response leave only search queries, without your personal comments.
    """

PRODUCT_DESCRIPTION_PROMPT = """
        Write a promo description for the {}. It should be concise, moderately brief, and salesy. 
        Try to keep it to 2-3 paragraphs and about 100 words. 
        Highlight the name of the product, and in the output, leave only the product description, without your own comments.
        """

CATEGORY_SEARCH_QUERIES_PROMPT = """
        Generate search tags for product category {}. 
        These tags should be adapted for the e-commerce site. 
        Return only the search tags themselves, without their own comments, on a single line and separated by a comma.
        """

CATEGORY_DESCRIPTION_PROMPT = """
        Generate a description for a product group {}. 
        The description should not be redundant, but it should sell.
        Try to keep it to 2-3 paragraphs and about 100 words.  
        Return only the description itself, without your own comments.
        """
