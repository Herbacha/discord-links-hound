from src.generator_formats.generate_list_by_author import generate_list_by_author


def generate_list_by_date(linkdata_list):
    output_lines = []
    linkdata_list.reverse()

    links_by_date = {}

    for linkdata in linkdata_list:
        current_link_date = linkdata.date.strftime("%d/%m/%Y")
        if current_link_date not in links_by_date:
            links_by_date[current_link_date] = []
        links_by_date[current_link_date].append(linkdata)

    for date, links in links_by_date.items():
        output_lines.append(f'# {date}')
        output_lines.append(generate_list_by_author(links, '## Posted by'))

    return '\r'.join(output_lines)
