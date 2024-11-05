import bs4

def code_formatting(question_text: bs4.element.Tag) -> str:
    """
    Formats question text by wrapping code blocks in triple backticks.

    Args:
    question_text (bs4.element.Tag): BeautifulSoup tag containing question text.

    Returns:
    str: Formatted question text with code blocks.
    """
    result = ""

    # Find all code blocks, starts with <pre>
    code_blocks = question_text.find_all("pre")

    # Iterate over contents
    for elem in question_text.contents:
        if elem in code_blocks:
            # Add code block with triple backticks
            result += '\n```\n' + elem.get_text(strip=True) + '\n```\n\n'
        else:
            # Normal text
            result += elem.get_text(strip=True)

    return result