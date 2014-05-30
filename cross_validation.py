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
    
    # cross validation
    from sklearn import cross_validation
    skf = cross_validation.StratifiedKFold(label, n_folds=5)
    # kf = cross_validation.KFold(len(data), n_folds=10)    

    prf = []
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

        # estimate
        print confusion_matrix(label_test, label_predict)
        print classification_report(label_test, label_predict)
        p, r, f, s = precision_recall_fscore_support(label_test, label_predict, average='weighted')
        print p, r, f, s
        prf.append([p, r, f])


    print 
    matrix = numpy.matrix(prf).T
    print 'averaege'
    print "precision:\t%f" % numpy.average(matrix[0])
    print "recall:\t\t%f" % numpy.average(matrix[1])
    print "fscore:\t\t%f" % numpy.average(matrix[2])
        
