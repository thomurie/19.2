from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def create_form():

    return render_template('form.html', curr_story=story.prompts)

@app.route('/story')
def response():
    responses = {}
    for word in story.prompts:
        responses[str(word)] = request.args[word]

    return render_template('response.html', responses=story.generate(responses))