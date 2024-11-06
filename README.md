# StackOverflow scrapper
### Usage
```bash
usage: main.py [-h] --tags TAGS [TAGS ...] [--pages PAGES [PAGES ...]]

StackOverflow Scraper

optional arguments:
  -h, --help            show this help message and exit
  --tags TAGS [TAGS ...]
                        Stackoverflow tags to scrape
  --pages PAGES [PAGES ...]
                        Specify the page numbers

```
Example:
```bash
python main.py --tags python --pages 1 2 3
```