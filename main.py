import json

from Utils.get_stackoverflow_questions import get_stackoverflow_questions
from Utils.get_question_answer import get_question_answer



if __name__ == "__main__":
    # Get recent Python questions
    all_question_blocks = get_stackoverflow_questions("cadence", [1, 2, 3])

    # Get question and answers
    q_a_pairs = get_question_answer(all_question_blocks)

    # Saving to a json file
    with open("q_a_pairs.json", "w") as json_file:
        json.dump(q_a_pairs, json_file, indent=4)