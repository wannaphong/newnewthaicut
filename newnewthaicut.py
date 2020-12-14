from pythainlp.tag.named_entity import ThaiNameTagger

thainer = ThaiNameTagger()

def word_tokenize(text):
    global thainer
    _ws = thainer.get_ner(text, pos = False)
    list_w = []
    bi = ""
    tag = ""
    for i,t in _ws:
        if t.startswith('B-'):
            if bi!="":
                list_w.append(bi)
            bi=""
            bi += i
            tag = t.replace('B-','')
        elif t.startswith('I-') and t.replace('I-','')==tag:
            bi += i
        elif t == "O" and tag!="":
            list_w.append(bi)
            bi=""
            tag = ""
            list_w.append(i)
        else:
            bi=""
            tag = ""
            list_w.append(i)
    if bi!="":
        list_w.append(bi)
    return list_w