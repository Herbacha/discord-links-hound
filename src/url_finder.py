import re
url_pattern = 'https?:[a-zA-Z0-9_.+-/#~]+'


def get_links(message, remove_tenor=True):
    results = re.findall(url_pattern, message)
    if len(results) > 0:
        if(remove_tenor):
            for r in results:
                if 'tenor.com' in r:
                    results.remove(r)
        return results
