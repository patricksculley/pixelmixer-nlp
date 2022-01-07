import spacy
from spacy.tokens import Span
import logging

class NerService():
    def __init__(self):
        logging.info('Init NerService.')
        self.nlp = spacy.load('en_core_web_lg', disable=['tagger', 'parser', 'attribute_ruler', 'lemmatizer'])

    def process_text(self, text):
        return self.generate_entity_list(self.nlp(text))
    
    def generate_entity_list(self, doc):
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
            logging.info('No named entities found.')
        return entity_list
