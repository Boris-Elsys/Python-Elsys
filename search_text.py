def search_and_replace_text(search_sentence, text):
    if len(search_sentence) < 2:
        return 'too short'
    elif ' '.join(search_sentence) not in text:
        return 'not available'
    else:
        text = text.split(',')
        search_sentence = " ".join(search_sentence)
        text.append(search_sentence)
        text = ','.join(text)
        text = text.split(search_sentence)
        text.append(search.sentence)
        return ''.join(text)