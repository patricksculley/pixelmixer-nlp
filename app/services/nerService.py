import spacy
from spacy.tokens import Span

class NerService():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg', disable=['tagger', 'parser', 'attribute_ruler', 'lemmatizer'])

    def process_text(self, text):
        doc = self.nlp(text)
        return self.create_entity_list(doc)
    

    def create_entity_list(self, doc):
        doc.ents = list(doc.ents)
        entity_list = []

        if doc.ents:
            for ent in doc.ents:
                ent_obj = {
                    'text': ent.text,
                    'type': ent.label_,
                    'description': str(spacy.explain(ent.label_)) 
                }
                entity_list.append(ent_obj)
        else:
            print('No named entities found.')
        return entity_list
