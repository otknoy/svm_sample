#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
import numpy


if __name__ == '__main__':
    # # init data
    # digits = load_digits()
    # data = digits.data
    # label = digits.target
    filename = 'train_data/questions_mod.csv'
    import create_feature
    questions = create_feature.load_train_data(filename)
    label = create_feature.questions2labels(questions, class_type='class')
    data = create_feature.questions2dfvector(questions)
    print "number of labels: %d" % len(list(set(label)))
    print "number of data: %d" % len(label)    

    # svm classifier
    estimator = SVC(kernel='linear')


    label_type_dict = {11: '書誌情報, 位置に関する質問',
                       12: '書誌情報, タイトル、作品目に関する質問',
                       13: '書誌情報, 発売日に関する質問',
                       14: '書誌情報, 掲載誌に関する質問',
                       15: '書誌情報, 作者に関する質問',
                       21: '内容情報, ストーリーの進展(結果、過程)に関する質問',
                       22: '内容情報, ストーリーに関する定義や、解釈の質問',
                       23: '内容情報, ストーリーに関する理由、原因の質問',
                       24: '内容情報, キャラクターの設定に関する質問',
                       25: '内容情報, オブジェクト、道具、技能の名称に関する2質, 内容情報, セリフに関する質問'}


    exit()
    while 1:
        input = raw_input()
        features = create_feature.questions2dfvector(questions)
        label_predict = estimator.predict(input)
        print label_type_dict[int(label)]

        

        
