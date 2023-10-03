from copy import deepcopy

def replace_tags(valid_tags, tokenized_text):
    tag_to_html = {
        '#': '<h1>',
        '/#': '</h1>',
        '##': '<h2>',
        '/##': '</h2>',
        '###': '<h3>',
        '/###': '</h3>',
        '####': '<h4>',
        '/####': '</h4>',
        '*': '<em>',
        '/*': '</em>',
        '{': '<span class="drop-capital">',
        '}': '</span>',
        '[cw:': '<p class="catch-word">',
        '[': '<p class="sig">',
        ']': '</p>',
        '\\': '<span class="side-note">',
        '/': '</span>',
        '$': '<h4>',
        '/$': '</h4>',
        '!!': '<sup>',
        '/!!': '</sup>'
    }

    tag_to_tei = {
        '#': '<head>',
        '/#': '</head>',
        '##': '<head>',
        '/##': '</head>',
        '###': '<head>',
        '/###': '</head>',
        '####': '<head>',
        '/####': '</head>',
        '*': '<hi>',
        '/*': '</hi>',
        '{': '<hi rend="drop-capital">',
        '}': '</hi>',
        '[cw:': '<p type="catch">',
        '[': '<fw type="sig">',
        ']': '</fw>',
        '\\': '<note>',
        '/': '</note>',
        '$': '<fw type="header">',
        '/$': '</fw>',
        '!!': '<hi type="sup">',
        '/!!': '</hi>'
    }
    
    tei_tokenized = deepcopy(tokenized_text)

    for tag in valid_tags:
        tokenized_text[tag[0]] = tag_to_html[tokenized_text[tag[0]]]
        tokenized_text[tag[1]-1] = tag_to_html[tokenized_text[tag[1]-1]]

    for tag in valid_tags:
        tei_tokenized[tag[0]] = tag_to_tei[tei_tokenized[tag[0]]]
        tei_tokenized[tag[1]-1] = tag_to_tei[tei_tokenized[tag[1]-1]]
    return tokenized_text, tei_tokenized

def add_outer_tags(converted_text, tei_tokenized):
    outer_tags = {
        '\r\n': '</p><p>',
        '\n': '</p><p>',
        '===': '<br/>',
        '~~~': '<br/>[Ornament]<br/>'
    }

    outer_tags_tei = {
        '\r\n': '</p><p>',
        '\n': '</p><p>',
        '===': '<pb/>',
        '~~~': '<figure>[Ornament]<figure/>'
    }
    converted_text = [outer_tags[tag] if tag in outer_tags.keys() else tag for tag in converted_text]
    tei_tokenized = [outer_tags_tei[tag] if tag in outer_tags_tei.keys() else tag for tag in tei_tokenized]
    # changes the first to just an open tag
    for i, token in enumerate(converted_text):
        if token == '</p><p>':
            converted_text[i] = '<p>'
            break

    for i, token in enumerate(tei_tokenized):
        if token == '</p><p>':
            tei_tokenized[i] = '<p>'
            break
    return converted_text, tei_tokenized