import inspect

def cheat(code):
    cheat_dict = {
        0: "This is a cheat for Exercise 0!",
        1: '''x = np.random.randn(1000)
              print(x)''',
        2: "df = pd.DataFrame(x)",
        3: '''hist, bins = np.histogram(x, bins=range(-3,4))
              df.hist()
              #in a new cell:
              plt.hist(x)''',
        4: "twoD = np.random.randn(1000,2)",
        5: '''x = twoD[:,0]
              y = twoD[:,1]
              plt.scatter(x,y)''',
        6: '''twoD *= 2
              twoD[:,0] += 5
              twoD[:,1] -= 5''',
        7: '''extra_rows = np.random.randn(1000,2)
              X = np.vstack([twoD, extra_rows])''',
        8: '''Y = np.vstack([np.ones((1000,1)),-1*np.ones((1000,1))])
              data = np.hstack([X, Y])''',
        9: '''plt.scatter(twoD[:,0], twoD[:,1], c='gray')
              plt.scatter(extra_rows[:,0], extra_rows[:,1], c='pink')''',
        10: '''perm = np.random.permutation(2000)
               data = data[perm]
               # shuffle again
               np.random.shuffle(data)''',
        11: '''reg.fit(features, labels)''',
        12: '''pred = reg.predict(features)
               acc = (pred == labels).mean()''',
        13: "cross_val_score(reg, features, labels, scoring='accuracy', cv=5)",
        14: '''# first cell:
               sizes, train_scores, test_scores = learning_curve(LogisticRegression(), features, labels, cv=5, scoring='accuracy', train_sizes=np.linspace(0.1,1.0,200))
               # second cell:
               train_scores_mean = train_scores.mean(axis=1)
               test_scores_mean = test_scores.mean(axis=1)
               # third cell:
               # like above but use scoring='neg_log_loss' instead of scoring='accuracy'.''',
        15: '''# loads hand written character image data
               digits = load_digits()
               X, y = digits.data, digits.target
        
               params = np.logspace(-4,1,6)
               train_scores, valid_scores = validation_curve(reg, X, y, 'C', params, cv=5,scoring='neg_log_loss')
        
               train_scores_mean = train_scores.mean(axis=1)
               valid_scores_mean = valid_scores.mean(axis=1)
               assert train_scores_mean.shape == (6,)
               assert valid_scores_mean.shape == (6,)
        
               plt.semilogx(params, -train_scores_mean, c='red', label='train')
               plt.semilogx(params, -valid_scores_mean, c='blue', label='validation')
               plt.legend()''',
        16: "parameters = [{'kernel':['poly'], 'degree':[1, 2,3]}, {'kernel': ['rbf'], 'C': [1,10]}, {'kernel': ['linear'], 'C': [1,10], 'gamma': [0.1,1]}]"
    }
    if code in cheat_dict:
        print(inspect.cleandoc(cheat_dict[code]))
    else:
        print('Invalid exercise id, Naughty cheater! Provide an integer from 0 to 16.')

def hint(code):
    hint_dict = {
        0: "This is a hint for Exercise 0!",
        1: "call the function np.random.randn with 1000 as argument",
        2: "pd.DataFrame acts both as the class and the constructor of the class. call the constructor as a method.",
        3: '''hist, bins = np.histogram(__fill_in__, bins=range(-3,4))
              hint(3.2) for next hint.''',
        3.2: '''
              #in a new cell:
              plt.hist(__fill_in__)''',
        4: "use two arguments for number of rows and number of columns",
        5: '''use some_array[row_selector, column_selector] for selection of rows and columns. colon (:) selects all rows or columns
              hint(5.2) for next hint''',
        5.2: "when you have sliced out onedimensional arrays with x-coordinates and y-coordinates, give these as arguments to plt.scatter.",
        6: '''to scale all of the points you want to scale all numbers in the matrix so use the *= operator.
              hint(6.2) for next hint''',
        6.2: "use column selection as above. this gives you one dimensional arrays. you can also assign things to this selection which updates a single column of the original matrix. use += for convenience",
        7: "vstack should be given a list of arrays to stack on top of eachother",
        8: '''when creating the ones, you can make it into a array of shape (1000,1) by passing this tuple to np.ones.
              for negative ones do the same and then use multiplication.
              finally hstack as the same signature as vstack.''',
        9: "You may use either twoD and extra_rows, or data. use plt.scatter in the same manner as before, and add color: plt.scatter(__fill_in__, c='gray')",
        10: '''perm = np.random.permutation(2000)
               try to change the order of a test list:
               li = np.array([10,100,1000])
               li[[1,0,2]]
               for the np.random.shuffle method please see the built-in help or cheat.''',
        11: '''Use the variables features and labels created above when calling reg.fit. You can always run help(reg.fit).''',
        12: '''pred = reg.predict(__fill_in__)
               for accuracy, you can first check when the predictions are correct with (pred==Y). you can then use .mean().''',
        13: "you should use the arguments scoring='accuracy' and cv=5. you can use a full class for the crossvalidation object but cv=5 is a lot simpler.",
        14: '''# first cell:
               this is very similar to previous exercise 
               # second cell:
               train_scores_mean = train_scores.mean(axis=__fill_in__)
               test_scores_mean = test_scores.mean(axis=__fill_in__)
               # third cell:
               # like above but use scoring='neg_log_loss' instead of scoring='accuracy'.''',
        15: '''# loads hand written character image data
               digits = load_digits()
               X, y = digits.data, digits.target
        
               params = np.logspace(-4,1,6)
               train_scores, valid_scores = validation_curve(reg, X, y, __string_name_of_the_parameter__, __the_values_of_the_parameter__, cv=5,scoring='neg_log_loss')
               # compute means as previous exercise 
        
               plt.semilogx(params, -train_scores_mean, c='red', label='train')
               plt.semilogx(params, -valid_scores_mean, c='blue', label='validation')
               plt.legend()''',
        16: '''use a list of dictionaries.  
               parameters = [{'kernel':['poly'], 'degree':[1, 2,3]}, __continue_with_the_other_kernels__]'''
    }
    if code in hint_dict:
        print(inspect.cleandoc(hint_dict[code]))
    else:
        print('Invalid exercise id. Did you type the id correctly?')

