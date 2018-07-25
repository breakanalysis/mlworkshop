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
                rf.model_performance(test)''',
      '2kj': '''Y_train = train.iloc[:,28*28]
                X_train = train.drop(28*28, axis = 1)
                Y_test = test.iloc[:,28*28]
                X_test = test.drop(28*28, axis = 1)
                del train, test
             ''',
      'kalle': '''print(X_test[0].shape)
                  print(X_test[0][:,:,0].shape)''',
      'bella': '''model = Sequential()
                  model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                  activation ='relu', input_shape = (28,28,1)))''',
      'giorgio': "model.add(MaxPool2D(pool_size=(2,2)))",
      'charles': '''# you may leave out 'rate=' from the next line
                    model.add(Dropout(rate=0.25))'''
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
      'sj8': "model_performance works just as a java method (it is a method on the model/estimator), and it has one argument which is the dataframe to measure performance on.",
      '2kj': "Hint 1: to select all rows, use colon. Hint 2: axis has to do with dropping rows vs columns.",
      'kalle': '''First part: X_test[0] extracts the first slice along the first dimension. This represents the first image. What is its shape?
                  Second part: Select a slice of X_test[0], where the first two dimensions take any value, and the last takes only value 0.''',
      'bella': "There are two hints! Run either of hint('bella_adding_layer'), hint('bella_create_layer') or hint('bella_kernel_size').",
      'bella_adding_layer': "use model.add(your_layer_here)",
      'bella_create_layer': "NameOfLayer(param1 , param2, ... , named_param1=value1, named_param2=value2, ...)",
      'bella_kernel_size': "kernel_size=(5,5), this is a python tuple",
      'giorgio': "follow the solution of previous exercise, but use pool_size as the only parameter",
      'charles': "follow the solution of previous exercise, but use rate as the only parameter"
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
        'sj8': "Sorry no skeleton here",
        '2kj': '''Y_train = train.iloc[fill_in_to_select_all_rows,fill_in_to_select_target_column]
                  X_train = train.drop(fill_in)
                  Y_test = test.iloc[fill_in,fill_in]
                  X_test = test.drop(fill_in)
                  del train, test
               ''',
        'kalle': "No skeleton, but checkout the hint if needed.",
        'bella': '''model = Sequential()
                    model.add(__fill_in__(filters = __fill_in__, kernel_size = __fill_in__ ,padding = 'Same', 
                    activation =__fill_in__, input_shape = __fill_in__))''',
        'giorgio': "model.add(MaxPool2D(__fill_in__))",
        'charles': "model.add(Dropout(__fill_in__))",

    }
    if code in skel:
        print(inspect.cleandoc(skel[code]))
    else:
        print('No skeletons in this wardrobe. Did you type the id correctly?')
