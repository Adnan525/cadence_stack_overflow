import requests
from typing import List
from bs4 import BeautifulSoup

from Utils.code_formatting import code_formatting

def get_question_answer(all_question_blocks: List[dict]) -> List[dict]:
    q_a_pairs = []
    no_answer_count = 0
    base_url = "https://stackoverflow.com/"

    for question_block in all_question_blocks:
        question_page = requests.get(base_url + question_block["link"])
        soup = BeautifulSoup(question_page.text, "html.parser")

        # Full question text
        question_html = soup.find("div", class_="s-prose")
        question = code_formatting(question_html)

        # Check if there is no answer
        if question_block["answer_count"] == 0:
            q_a_pair = {
                "title": question_block["title"],
                "question": question,
                "accepted_answer": None,
                "all_answers": None
            }
            q_a_pairs.append(q_a_pair)
            no_answer_count += 1
            continue

        # All answers
        all_answer_html = soup.find("div", id = "answers") # this will pull all answers
        all_extracted_answers = []
        accepted_answer = None
        if question_block["is_accepted"]:
            accepted_answer_html = all_answer_html.find("div", class_="accepted-answer")
            accepted_answercell_html = accepted_answer_html.find("div", class_="answercell")
            accepted_answer_text_html = accepted_answercell_html.find("div", class_="s-prose")
            accepted_answer = accepted_answer_text_html.get_text(strip=True)

        else:
            all_answers = all_answer_html.find_all("div", class_="answer")
            for answer in all_answers:
                answercell_html = answer.find("div", class_="answercell")
                answer_text_html = answercell_html.find("div", class_="s-prose")
                answer = code_formatting(answer_text_html)
                all_extracted_answers.append(answer)

        q_a_pair = {
            "title": question_block["title"],
            "question": question,
            "accepted_answer": accepted_answer,
            "all_answers": all_extracted_answers
        }
        q_a_pairs.append(q_a_pair)

    print(f"[INFO] Total questions scraped: {len(q_a_pairs)}")
    print(f"[INFO] Total questions without answers: {no_answer_count}")
    print(f"[INFO] Total questions with answers: {len(q_a_pairs) - no_answer_count}")
    return q_a_pairs