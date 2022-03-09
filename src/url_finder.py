import re
url_pattern = 'https?:[a-zA-Z0-9_.+-/#~]+'


def get_links(message):
    results = re.findall(url_pattern, message)
    if len(results) > 0:
        return results
