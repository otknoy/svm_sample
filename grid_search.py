#!/usr/bin/env python
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
import numpy

def grid_search(train_data, train_label):
    param_grid = [{'C': [1, 10, 100, 1000], 'kernel': ['linear']},
                  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},]
    clf = GridSearchCV(SVC(C=1), param_grid, n_jobs=-1)
    clf.fit(train_data, train_label, cv=5)
    return clf


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    
    import create_feature
    questions = create_feature.load_train_data(filename)
    label = create_feature.questions2labels(questions)
    data = create_feature.questions2dfvector(questions)
    print "number of labels: %d" % len(list(set(label)))
    print "number of data: %d" % len(label)
    print

    result = grid_search(data, label)

    print 'Best parameter'
    print result.best_estimator_
    print

    print 'score'
    for params, mean_score, all_scores in result.grid_scores_:
        print params, mean_score, all_scores
    print
    
    
