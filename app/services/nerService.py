import spacy
from spacy.tokens import Span

class NerService():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg', disable=['tagger', 'parser', 'attribute_ruler', 'lemmatizer'])

    def process_text(self, text):
        doc1 = self.nlp(text)
        return self.show_ents(doc1)
    

    def show_ents(self, doc):
        ORG = doc.vocab.strings[u'ORG']
        new_ent = Span(doc, 0, 1, label=ORG)
        doc.ents = list(doc.ents) + [new_ent]

        result_list = []

        if doc.ents:
            for ent in doc.ents:
                ent_obj = {
                    'text': ent.text,
                    'start_char': ent.start_char,
                    'end_char': ent.end_char,
                    'label': ent.label_,
                    'explain': str(spacy.explain(ent.label_))
                }
                result_list.append(ent_obj)
        else:
            print('No named entities found.')
        return result_list
