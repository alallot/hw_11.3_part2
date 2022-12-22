from flask import Flask, render_template

import utils
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)

@app.route("/")
def list_candidates():
    candidates = load_candidates_from_json('candidates.json')
    return render_template("index.html", candidates=candidates)

@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    candidate = get_candidate(candidate_id)
    return render_template("card.html", candidate=candidate)

@app.route("/skill/<string:skill_name>")
def get_candidates_by_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))

@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))

app.run()
