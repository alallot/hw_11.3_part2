import json

def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None


def get_candidates_by_skill(skill_name):
    result = []
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')

        if skill_name.lower() in candidate_skills:
            result.append(candidate)

    return result


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            matches.append(candidate)
    return matches

