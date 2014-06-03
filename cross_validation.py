#!/usr/bin/env python
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
import numpy


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    
    import create_feature
    questions = create_feature.load_train_data(filename)
    label = create_feature.questions2labels(questions)
    data = create_feature.questions2dfvector(questions)
    print "number of labels: %d" % len(list(set(label)))
    print "number of data: %d" % len(label)
    
    # split data for cross validation
    from sklearn import cross_validation
    skf = cross_validation.StratifiedKFold(label, n_folds=5)

    all_label_test = []
    all_label_predict = []
    for train_index, test_index in skf:
        # split train and test
        data_train, data_test = data[train_index], data[test_index]
        label_train, label_test = label[train_index], label[test_index]

        # svm classifier
        estimator = SVC(kernel='linear')
        
        # train
        estimator.fit(data_train, label_train)

        # predict
        label_predict = estimator.predict(data_test)

        # save results
        all_label_test += list(label_test)
        all_label_predict += list(label_predict)
        

    # evaluate
    print 
    print confusion_matrix(all_label_test, all_label_predict)
    print classification_report(all_label_test, all_label_predict)
        
