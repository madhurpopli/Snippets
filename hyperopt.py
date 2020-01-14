def objective(params):
    
    params = {'n_estimators': int(params['n_estimators']), 
              'max_depth': int(params['max_depth']),
              'min_samples_leaf': int(params['min_samples_leaf'])}
    
    clf = RandomForestClassifier(n_jobs=-1, random_state=42,class_weight='balanced', **params)
    score = cross_val_score(clf, X, Y, scoring=auc_scorer, cv=StratifiedKFold(n_splits=3)).mean()
    print("AUC {:.3f} params {}".format(score, params))
    return score

space = {
    'n_estimators': hp.quniform('n_estimators', 25, 500, 25),
    'max_depth': hp.quniform('max_depth', 1, 10, 1),
    'min_samples_leaf' : hp.quniform('min_samples_leaf', 1000, 10000, 100)
}

best = fmin(fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=10)

for i in best.keys():
    best[i] = int(best[i])
