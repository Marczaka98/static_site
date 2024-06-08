def markdown_to_blocks(markdown):
    block_list = markdown.split('\n\n')
    filtered_list = []
    for block in block_list:
        if block == '':
            continue
        block = block.strip()
        filtered_list.append(block)
    return filtered_list