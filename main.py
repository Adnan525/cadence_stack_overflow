from Utils.get_stackoverflow_questions import get_stackoverflow_questions
from Utils.get_question_answer import get_question_answer



if __name__ == "__main__":
    # Get recent Python questions
    all_question_blocks = get_stackoverflow_questions("cadence", [1, 2, 3])
    for question in all_question_blocks:
        print(question)

    # # Get question and answers
    # q_a_pairs = get_question_answer(all_question_blocks)
    #
    # # Print first question and answer
    # print(q_a_pairs[0])
