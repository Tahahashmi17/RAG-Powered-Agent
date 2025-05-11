from flask import Blueprint, render_template, request
from .agent import handle_query
main = Blueprint('main', __name__)
@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    retrieved_docs = []
    decision = ""
    if request.method == 'POST':
        query = request.form['query']
        result, decision, retrieved_docs = handle_query(query)
    return render_template('index.html', result=result, decision=decision, retrieved_docs=retrieved_docs)
