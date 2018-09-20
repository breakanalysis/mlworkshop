import inspect

def cheat(code):
    cheat_dict = {
      'a': "Paste the url into your browser, localhost:54321 or 127.0.0.1:54321",
      'b': '''test = h2o.import_file("data/mnist/mnist.test.csv.gz")
              train = h2o.import_file("data/mnist/mnist.train.csv.gz")''',
      'c': '''train[-1] = train[-1].asfactor()
                test[-1] = test[-1].asfactor()''',
      'd': "train, valid = train.split_frame([0.8])",
      'e': '''from h2o.estimators import H2ORandomForestEstimator
              rf = H2ORandomForestEstimator()
           ''',
      'f': '''x = list(range(28*28))
              y = 28*28
              rf.train(x,y,training_frame=train, validation_frame=valid)''',
      'g': '''rf.model_performance(train)
              rf.model_performance(valid)
              rf.model_performance(test)''',
      'h': '''Y_train = train.iloc[:,28*28]
              X_train = train.drop(28*28, axis = 1)
              Y_test = test.iloc[:,28*28]
              X_test = test.drop(28*28, axis = 1)
              del train, test
             ''',
      'i': '''print(X_test[0].shape)
              print(X_test[0][:,:,0].shape)''',
      'j': '''model = Sequential()
              model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same',
                                   activation ='relu', input_shape = (28,28,1)))''',
      'k': "model.add(MaxPool2D(pool_size=(2,2)))",
      'l': '''# you may leave out 'rate=' from the next line
              model.add(Dropout(rate=0.25))''',
      'm': "The size of the data will be: ",
      'n': '''model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same',
                  activation ='relu'))
              model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same',
                  activation ='relu'))
              model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
              model.add(Dropout(0.25))''',
      'o': '''model.add(Flatten())
              model.add(Dense(256, activation = "relu"))
              model.add(Dropout(0.5))
              model.add(Dense(10, activation = "softmax"))''',
      'p': '''epochs = 1
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
      'a': "Urls can be interesting :)",
      'b': "Choose either hint('b_method_name') or hint('b_file_path).",
      'b_method_name': "Use h2o.imp... (press tab see methods starting with imp)",
      'b_file_path': "By running !cmd in a cell, cmd is executed in bash. You can therefore run !ls followed by !ls fill_in_folder_here.",
      'f': "The target column is the last one. To know how many columns there is use either train.describe() or train.ncols, or calculate it using that there are 28x28 pixels in each image.",
      'c': "In Python a[-1] can be used to access the last element of a",
      'd': "Use df.split_frame(list_of_fractions)",
      'e': '''see explaination above; the name of the class is H2ORandomForestEstimator.''',
      'g': "model_performance works just as a java method (it is a method on the model/estimator), and it has one argument which is the dataframe to measure performance on.",
      'h': "Hint 1: to select all rows, use colon. Hint 2: axis has to do with dropping rows vs columns.",
      'i': '''First part: X_test[0] extracts the first slice along the first dimension. This represents the first image. What is its shape?
              Second part: Select a slice of X_test[0], where the first two dimensions take any value, and the last takes only value 0.''',
      'j': "There are three hints. Run either of hint('j_adding_layer'), hint('j_create_layer') or hint('j_kernel_size').",
      'j_adding_layer': "use model.add(your_layer_here)",
      'j_create_layer': "the syntax is NameOfLayer(param1 , param2, ... , named_param1=value1, named_param2=value2, ...)",
      'j_kernel_size': "kernel_size=(5,5), this is a python tuple",
      'k': "For the name of the layer class check the imports above. Use pool_size=(2,2)" ,
      'l': "The only parameter you need is rate. For the name of the layer class check the imports above.",
      'm': '''Layers often have extra weights called biases which are additive constants. For example b is a bias weight in the expression ax+b.
              Convnets will have one separate bias for every filter. Maxpooling layers have the effect that they half the data's size across each axis if the pool_size is (2,2).
      ''',
      'n': '''The convnets should have the parameters: filters, activation, padding and kernel_size.
              The maxpooling layer should have pool_size.
              Dropout as before with parameter 0.25.''',
      'o': '''Dense(n) gives a dense layer with n units (neurons). Each neuron will have an incomming connection from each neuron in the previous layer,
              which is why it is called dense.
      ''',
      'p': '''Use the test set as validation_data. This should be given as a 2-tuple containing image data and targets.'''
    }
    if code in hint_dict:
        print(inspect.cleandoc(hint_dict[code]))
    else:
        print('Invalid exercise id. Did you type the id correctly?')
