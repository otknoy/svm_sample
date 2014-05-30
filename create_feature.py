#!/usr/bin/env python
import MeCab
import numpy

def load_train_data(filename):
    questions = []
    f = open(filename)
    import csv
    import unicodedata
    for label, text in csv.reader(f):
        norm_text = unicodedata.normalize('NFKC', text.decode('utf-8'))
        questions.append((int(label), norm_text))
    f.close()
    return questions
    

def tokenizer(s):
    uni = s.encode('utf-8')
    tagger = MeCab.Tagger("-Ochasen")
    node = tagger.parseToNode(uni)

    terms = []
    while node:
        features = node.feature.split(',')
        basic_form = features[6]
        if basic_form == '*':
            basic_form = node.surface

        noun_id_list = range(36, 67+1)
        if node.posid in noun_id_list:
            terms.append(basic_form)

        terms.append(basic_form)
        node = node.next
    return terms[1:-1]

def term_frequency(terms):
    tf = {}
    for t in terms:
        if not tf.has_key(t):
            tf[t] = 0
        tf[t] += 1
    return tf

def ngram(terms, n=2):
    ret = []
    i = 0
    while i+n < len(terms):
        ret.append(' '.join(terms[i:i+n]))
        i += 1
    return ret

def questions2labels(questions):
    labels = numpy.array([l for l, q in questions])
    return labels

    
def questions2dfvector(questions):
    tf_list = []
    # all_terms = []
    for l, q in questions:
        terms = tokenizer(q)
        tf = term_frequency(terms)
        tf_list.append(tf)
    #     all_terms += terms
    # all_terms = list(set(all_terms))

    all_tf = {}
    for tf in tf_list:
        for t, f in tf.items():
            if not all_tf.has_key(t):
                all_tf[t] = 0
            all_tf[t] += f
    all_terms = [t for t, f in all_tf.items()]
    # all_terms = [t for t, f in all_tf.items() if f >= 2]
    
    features = []
    for tf in tf_list:
        feature = []
        for t in all_terms:
            if not tf.has_key(t):
                feature.append(0)
            else:
                feature.append(tf[t])
        features.append(numpy.array(feature))
    return numpy.array(features)

 
def questions2features(questions):
    labels = questions2labels(questions)
    dfvector = questions2dfvector(questions)
    return labels, dfvector


if __name__ == '__main__':
    filename = 'train_data/questions.csv'

    questions = load_train_data(filename)
    label = questions2labels(questions, class_type='class')
    data = questions2dfvector(questions)
    print "number of labels: %d" % len(list(set(label)))
    print "number of data: %d" % len(label)    

    # print len(labels)
    # print len(dfvector)

    # for label, question in sorted(questions):
    #     print label, question.encode('utf-8')

