from somajo import Tokenizer, SentenceSplitter
from scripts.features import sent2features
from nltk.tokenize.treebank import TreebankWordDetokenizer

import pickle


model_name_anno = "f"

similarity_anno = dict()

model_path_anno = "scripts/models/crf-f.pkl"

# Rechtsprechung, Literatur, Richter, Verordnung, EU-Norm, Vorschrift, Vertrag, Gesetz
annotations = ["B-RS","I-RS","B-LIT","I-LIT","B-RR","I-RR","B-VO","I-VO","B-EUN","I-EUN","B-VS","I-VS","B-VT","I-VT","B-GS","I-GS"]


def detokenize(words):
    d = TreebankWordDetokenizer()
    detokenized = d.detokenize(words)
    return detokenized.replace(" .",".").replace(" ,", ",").replace("( ","(").replace(" )", ")")


def tokenSplit(text):
    tokenizer = Tokenizer(split_camel_case=False, token_classes=False, extra_info=False)
    tokens = tokenizer.tokenize(text)
    return tokens 

def splitSentTokenIdx(text):
    # generate tokens from text
    tokens = tokenSplit(text)

    # sort to sentences
    sentence_splitter = SentenceSplitter(is_tuple=False)
    sentences = sentence_splitter.split(tokens)

    # add start and end indexes of token in text
    endIdxUpdate = 0
    sents_idxd = []
    for sent in sentences:
        tokens_idxd = []
        for token in sent:
            startIdx = text.find(token, endIdxUpdate)
            endIdx = startIdx + len(token)
            if startIdx != -1:
                endIdxUpdate = endIdx
            tokens_idxd.append((token, startIdx, endIdx))
        sents_idxd.append(tokens_idxd)
    return sents_idxd

def get_words(doc_list):
    zipped = list(zip(*doc_list))
    zipped = zipped[0]
    zipped = list(zip(*zipped))
    return zipped[0]

def get_entities(doc_list):    
    entities = []
    for sent in doc_list:      
        for i, name in enumerate(sent):
            if name[1] in annotations:
                entities.append(name)
    return entities

def separate_entities(entities):
    entities_list = []
    idx = 0
    for i in range(len(entities)-1):
        if (entities[i][1].startswith("I") and entities[i+1][1].startswith("B")) or (entities[i][1].startswith("B") and entities[i+1][1].startswith("B")):
            ent = entities[idx:i+1] 
            entities_list.append(ent)
            idx += len(ent)
    entities_list.append(entities[idx:len(entities)])
    return entities_list


def extract_annotations_from_text(text):

    tokens_idxd = splitSentTokenIdx(text)

    sents_anno = []
    for sent in tokens_idxd:
        sent_tokens = []
        for token in sent:
            sent_tokens.append(token[0])
        sents_anno.append(sent_tokens)

    # prepare features 
    sents_anno_ = []
    for sent in sents_anno:
      sent_anno = []
      for token in sent:
        sent_anno.append((token,))
      sents_anno_.append(sent_anno)

    X_anno = [sent2features(s, model_name_anno, similarity_anno) for s in sents_anno_]

    # load model
    crf_anno = pickle.load(open(model_path_anno, 'rb'))

    # predict annotations
    y_pred_anno = crf_anno.predict(X_anno)

    results_anno = []
    for (sent, pred) in zip(tokens_idxd, y_pred_anno):
        annos = []
        for (s, p) in zip(sent, pred):
            annos.append((s, p))
        results_anno.append(annos)

    legal_tokens = get_entities(results_anno)

    # if no references found:
    if not legal_tokens:
        return None

    legal_tokens_sep = separate_entities(legal_tokens)

    legal_references = []
    for reference in legal_tokens_sep:
        words = get_words(reference)
        ref = detokenize(words)
        start = reference[0][0][1]
        end = reference[len(reference)-1][0][2]
        legal_references.append((ref, start, end))

    return legal_references

