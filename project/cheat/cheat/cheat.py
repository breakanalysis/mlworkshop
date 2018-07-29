import inspect

def cheat(code):
    cheat_dict = {
      'andy': "Paste the url into your browser, localhost:54321 or 127.0.0.1:54321",
      'mia': '''test = h2o.import_file("data/mnist/mnist.test.csv.gz")
                train = h2o.import_file("data/mnist/mnist.train.csv.gz")''',
      'sam': '''train[-1] = train[-1].asfactor()
                test[-1] = test[-1].asfactor()''',
      'anne': "train, valid = train.split_frame([0.8])",
      'jessie': '''from h2o.estimators import H2ORandomForestEstimator
                rf = H2ORandomForestEstimator()
                ''',
      'alfred': '''x = list(range(28*28))
                   y = 28*28
                   rf.train(x,y,training_frame=train, validation_frame=valid)''',
      'rick': '''rf.model_performance(train)
                rf.model_performance(valid)
                rf.model_performance(test)''',
      'kate': '''Y_train = train.iloc[:,28*28]
                X_train = train.drop(28*28, axis = 1)
                Y_test = test.iloc[:,28*28]
                X_test = test.drop(28*28, axis = 1)
                del train, test
             ''',
      'charlie': '''print(X_test[0].shape)
                  print(X_test[0][:,:,0].shape)''',
      'bella': '''model = Sequential()
                  model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                                   activation ='relu', input_shape = (28,28,1)))''',
      'george': "model.add(MaxPool2D(pool_size=(2,2)))",
      'eric': '''# you may leave out 'rate=' from the next line
                    model.add(Dropout(rate=0.25))''',
      'gabby': '''model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                      activation ='relu'))
                  model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                      activation ='relu'))
                  model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
                  model.add(Dropout(0.25))''',
      'may': '''model.add(Flatten())
                model.add(Dense(256, activation = "relu"))
                model.add(Dropout(0.5))
                model.add(Dense(10, activation = "softmax"))''',
      'pat': '''epochs = 1
                  batch_size = 86
                  history = model.fit(X_train, Y_train, batch_size = batch_size, epochs = epochs, 
                                      validation_data = (X_test, Y_test), verbose = 2)'''
    }
    if code in cheat_dict:
        print(inspect.cleandoc(cheat_dict[code]))
    else:
        print('Invalid exercise id, Naughty cheater!')

def hint(code):
    hint_dict = {
      'andy': "Urls can be interesting :)",
      'mia': "Use h2o.imp... (press tab see methods starting with imp)",
      'alfred': "Check out the help on range and list.",
      'sam': "In Python [-1] can be used to access the last column",
      'anne': "Use df.split_frame(list_of_fractions)",
      'jessie': '''call as a 0-argument constructor, but no "new" or semicolon.''',
      'rick': "model_performance works just as a java method (it is a method on the model/estimator), and it has one argument which is the dataframe to measure performance on.",
      'kate': "Hint 1: to select all rows, use colon. Hint 2: axis has to do with dropping rows vs columns.",
      'charlie': '''First part: X_test[0] extracts the first slice along the first dimension. This represents the first image. What is its shape?
                  Second part: Select a slice of X_test[0], where the first two dimensions take any value, and the last takes only value 0.''',
      'bella': "There are two hints! Run either of hint('bella_adding_layer'), hint('bella_create_layer') or hint('bella_kernel_size').",
      'bella_adding_layer': "use model.add(your_layer_here)",
      'bella_create_layer': "NameOfLayer(param1 , param2, ... , named_param1=value1, named_param2=value2, ...)",
      'bella_kernel_size': "kernel_size=(5,5), this is a python tuple",
      'george': "follow the solution of previous exercise, but use pool_size as the only parameter",
      'eric': "follow the solution of previous exercise, but use rate as the only parameter",
      'gabby': '''The convnets should have the parameters: filters, activation, padding and kernel_size.
                  The maxpooling layer should have pool_size and strides.
                  Dropout as before with parameter 0.25.''',
      'may': '''Follow previous exercises. Just like the rate parameter in Dropout can be used without name, the
                parameter controlling the number of units in a Dense layer can be used without name by placing it first.''',
      'pat': '''Use the training set as validation_data. This should be given as a tuple image data followed by targets.'''
    }
    if code in hint_dict:
        print(inspect.cleandoc(hint_dict[code]))
    else:
        print('Invalid exercise id. Did you type the id correctly?')

def skeleton(code):
    skel = {
        'andy': "Most exercises have skeletons, but sorry no skeleton here!",
        'mia': '''test = h2o.{fill_in}("fill_in")
                  train = h2o.{fill_in}("fill_in")''',
        'alfred': '''x = fill_in 
                     y = fill_in
                     rf.train(fill_in_here)''',
        'anne': "train, valid = train.fill_in",
        'sam': '''train[fill_in] = train[fill_in].asfactor()
                  test[fill_in] = test[fill_in].asfactor()''',
        'rick': "Most exercises have skeletons, but sorry no skeleton here!",
        'kate': '''Y_train = train.iloc[fill_in_to_select_all_rows,fill_in_to_select_target_column]
                  X_train = train.drop(fill_in)
                  Y_test = test.iloc[fill_in,fill_in]
                  X_test = test.drop(fill_in)
                  del train, test
               ''',
        'charlie': "No skeleton, but checkout the hint if needed.",
        'bella': '''model = Sequential()
                    model.add(__fill_in__(filters = __fill_in__, kernel_size = __fill_in__ ,padding = 'Same', 
                    activation =__fill_in__, input_shape = __fill_in__))''',
        'george': "model.add(MaxPool2D(__fill_in__))",
        'eric': "model.add(Dropout(__fill_in__))",
        'gabby': '''model.add(Conv2D(__fill_in__))
                    model.add(Conv2D(__fill_in__))
                    model.add(MaxPool2D(__fill_in__))
                    model.add(Dropout(__fill_in__))''',
        'may': '''model.add(__fill_in__)
                  model.add(__fill_in__)
                  model.add(__fill_in__)
                  model.add(__fill_in__)''',
        'pat': '''epochs = 1
                    batch_size = 86
                    history = model.fit(__fill_in__, __fill_in__, batch_size = __fill_in__, epochs = __fill_in__, 
                        validation_data = __fill_in__, verbose = 2)'''

    }
    if code in skel:
        print(inspect.cleandoc(skel[code]))
    else:
        print('No skeletons in this wardrobe. Did you type the id correctly?')
        
