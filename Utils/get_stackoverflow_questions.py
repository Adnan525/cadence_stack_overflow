import requests
from bs4 import BeautifulSoup
from typing import List

# summary = """class="s-post-summary js-post-summary" """
# question_link = """s-link"""


def get_stackoverflow_questions(tag:str, pages: List[int], page_size:int = 50) -> List[dict]:
    # Store all questions
    questions = []

    for page in pages:
        base_url = f"https://stackoverflow.com/questions/tagged/{tag}?tab=newest&page={page}&pagesize={page_size}"
        response = requests.get(base_url)
        # Soup object with parser
        soup = BeautifulSoup(response.text, "html.parser")
        # All questions in that page
        all_question_summary = soup.find_all("div", class_="s-post-summary")

        for question_summary in all_question_summary:
            # Question href class, contains title and the link
            question_block = question_summary.find(class_ = "s-link")

            # Question title
            question_title = question_block.get_text()

            # Question link to get the question and answers
            question_link = question_block.get("href")

            # Number of answers
            # class="s-post-summary--stats-item has-answers has-accepted-answer"
            answer_count_tag = question_summary.find("div", class_="s-post-summary--stats-item",
                                            title=lambda x: x and "answer" in x)
            answer_count = int(answer_count_tag.find('span', class_='s-post-summary--stats-item-number').text)

            # Accepted answer
            is_accepted = question_summary.find("div", class_="has-accepted-answer")

            question = {
                "title": question_title,
                "link": question_link,
                "answer_count": answer_count,
                "is_accepted": False if is_accepted is None else True
            }

            questions.append(question)

    return questions