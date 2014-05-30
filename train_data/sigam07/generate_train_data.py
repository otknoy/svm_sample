#!/usr/bin/env python
import csv
import unicodedata

def load_cleaned_data(filename):
    classification = {}
    for qid, question, label1, label2 in csv.reader(open(filename)):
        normalized_question = unicodedata.normalize('NFKC', question.decode('utf-8'))

        if not classification.has_key(label1):
            classification[label1] = {}
        if not classification[label1].has_key(label2):
            classification[label1][label2] = []
        classification[label1][label2].append(normalized_question)

    return classification
    

def output(classification_dict, filename):
    
    # output label file
    f = open(filename + '.label', 'w')
    f.write('ID-Label list for train file: ' + filename + '\n')
    label_ids = classification_dict.keys();
    for l in classification_dict.keys():
        f.write(str(label_ids.index(l)) + ': ' + l + '\n')
    f.close

    # output train file
    f = open(filename, 'w')
    for l, questions in classification_dict.items():
        for q in questions:
            f.write(str(label_ids.index(l)) + ',' + q.encode('utf-8') + '\n')
    f.close()

if __name__ == '__main__':
    classification = load_cleaned_data('./data/cleaned_data.csv')

    broad_classification = {}
    for label1, m_labels in classification.items():
        for label2, questions in m_labels.items():
            if not broad_classification.has_key(label1):
                broad_classification[label1] = []
            broad_classification[label1].extend(questions)
    detail_classification1, detail_classification2 = classification.values()
        
    # print len(broad_classification)
    # print len(detail_classification1)
    # print len(detail_classification2)
    # for label, q in detail_classification1.items():
    #     print label

    output(broad_classification, './data/all.train')
    output(detail_classification1, './data/bib.train')
    output(detail_classification2, './data/content.train')
    

