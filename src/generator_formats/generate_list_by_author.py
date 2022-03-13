def generate_list_by_author(linkdata_list, author_md_prefix='#'):
    output_lines = []
    links_by_author = {}

    for linkdata in linkdata_list:
        if linkdata.author not in links_by_author:
            links_by_author[linkdata.author] = []
        links_by_author[linkdata.author].append(linkdata.url)

    for author, links in links_by_author.items():
        output_lines.append(f'{author_md_prefix} {author.display_name}')
        for link in links:
            output_lines.append(f'- {link}')

    return '\r'.join(output_lines)
