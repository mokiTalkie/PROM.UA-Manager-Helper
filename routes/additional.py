from flask import Blueprint, render_template


additional = Blueprint("/", import_name=__name__)


@additional.route("/", methods=["GET"])
def index() -> str:
    """
    Render the main HTML template with the content of the index page.

    Returns:
        str: The rendered HTML content of the main template with the content of the index page.
    """

    return render_template("main_template.html", route_product='tool/product', route_category='tool/product', content=render_template("index.html"))


@additional.route("/about", methods=["GET"])
def about() -> str:
    """
    Handles GET requests to the '/about' endpoint.

    Returns:
        str: The HTML content of the 'about.html' template rendered inside the 'main_template.html' template.
    """

    return render_template("main_template.html", route_product='tool/product', route_category='tool/product', content=render_template("about.html"))


@additional.route("/contacts", methods=["GET"])
def contacts() -> str:
    """
        Handles GET requests to the "/contacts" endpoint of the Flask app.

    Returns:
        A string representing the rendered template that includes the "contacts.html" file as content
        within the "main_template.html" file.
    """
    return render_template(
        "main_template.html", route_product='tool/product', route_category='tool/product', content=render_template("contacts.html")
    )
