def generate_table(linkdata_list):
    output_lines = []
    linkdata_list.reverse()
    for linkdata in linkdata_list:
        output_lines.append(
            f'| {linkdata.url} | {linkdata.author.display_name} | {linkdata.date.strftime("%d/%m/%Y - %H:%M")} |')
    return '| Link | Posted by | Date |\r| ---- | --------- | ---- |\r' + \
        '\r'.join(output_lines)
