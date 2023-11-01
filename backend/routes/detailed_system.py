from flask import jsonify, render_template, request, redirect, url_for, Blueprint
from main import detail


@detail.route("/", methods=['POST'])
def display():
    # page not built yet, return to index with nothing for now
    return render_template("index.html")


@detail.route("/add", methods=['POST', 'GET'])
def add_entry():
    """Adds new comment to the comment section."""
    data = request.get_json()
    comment_title = data.get('Title')
    comment_content = data.get('Content')

    if (comment_title) and (comment_content):
        return redirect(url_for("detail.display"))

    return jsonify({'message': 'Empty field not allowed'}), 406
