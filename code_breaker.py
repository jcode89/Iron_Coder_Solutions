def _decode(text_phrase):
    code_table = str.maketrans('nopqrstuvwxyzabcdefghijklm', 'abcdefghijklmnopqrstuvwxyz')
    text = text_phrase
    new_word = text.translate(code_table)
    return new_word

def _encode(text_phrase):
    code_table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'nopqrstuvwxyzabcdefghijklm')
    text = text_phrase.lower()
    new_word = text.translate(code_table)
    return new_word

print(_decode('pbqrarjovrf ner gur zbfg fhccbegvir pbzzhavgl\n'))
print(_encode('no one can read this secret message\n'))
print(_encode('it is so super secret\n'))
print(_encode('only a CodeNewbie can figure it out\n'))
