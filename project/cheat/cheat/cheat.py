import inspect

def cheat(code):
    cheat_dict = {
      't1w': "Paste the url into your browser, localhost:54321 or 127.0.0.1:54321",
      'i7b': '''test = h2o.import_file("data/mnist/mnist.test.csv.gz")
                train = h2o.import_file("data/mnist/mnist.train.csv.gz")''',
      '2if': '''train[-1] = train[-1].asfactor()
                test[-1] = test[-1].asfactor()''',
      'ot5': "train, valid = train.split_frame([0.8])",
      'j9s': '''from h2o.estimators import H2ORandomForestEstimator
                x = list(range(28*28))
                y = 28*28
                rf = H2ORandomForestEstimator()
                rf.train(x,y,training_frame=train, validation_frame=valid)''',
      'sj8': '''rf.model_performance(train)
                rf.model_performance(valid)
                rf.model_performance(test)'''
    }
    if code in cheat_dict:
        print(inspect.cleandoc(cheat_dict[code]))
    else:
        print('Invalid exercise id, Naughty cheater!')

def hint(code):
    hint_dict = {
      't1w': "Urls can be interesting :)",
      'i7b': "Use h2o.import_file",
      '2if': "In Python [-1] can be used to access the last column",
      'ot5': "Use df.split_frame(list_of_fractions)",
      'j9s': '''https://h2o-release.s3.amazonaws.com/h2o/rel-wolpert/11/docs-website/h2o-py/docs/modeling.html#h2o.estimators.estimator_base.H2OEstimator
                On the page search for 'Train the H2O model'.
                Then click on H2ORandomForestEstimator on the left pane.
                The full name of the model class you want is h2o.estimators.H2ORandomForestEstimator.''',
      'sj8': "model_performance works just as a java method (it is a method on the model/estimator), and it has one argument which is the dataframe to measure performance on."
    }
    if code in hint_dict:
        print(inspect.cleandoc(hint_dict[code]))
    else:
        print('Invalid exercise id. Did you type the id correctly?')

def skeleton(code):
    skel = {
        't1w': "Sorry no skeleton here",
        'i7b': '''test = h2o.{fill_in}("fill_in")
                  train = h2o.{fill_in}("fill_in")''',
        'j9s': '''from h2o.estimators import H2ORandomForestEstimator
                  x = fill_in 
                  y = fill_in
                  rf = H2ORandomForestEstimator()
                  rf.train(fill_in_here)''',
        'ot5': "train, valid = train.fill_in",
        '2if': '''train[fill_in] = train[fill_in].asfactor()
                  test[fill_in] = test[fill_in].asfactor()''',
        'sj8': "Sorry no skeleton here"
    }
    if code in skel:
        print(inspect.cleandoc(skel[code]))
    else:
        print('No skeletons in this wardrobe. Did you type the id correctly?')
        
        
