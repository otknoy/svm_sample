# SVM sample

SVM sample written by python

## Requirement

* mecab-python
* scikit-learn

## How to use

### Cross validation

```
./cross_validation.py train_data/all.train
```

### Grid search

```
./grid_search.py train_data/all.train
```

## Train files

### For 5 class

* train_data/fukuda/5_class.csv

### For 11 class (multistage)

#### 1st stage
* train_data/riku/all.train

#### 2nd stage
* train_data/riku/bib.train
* train_data/riku/content.train
