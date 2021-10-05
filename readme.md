# train_data = utils.load_data('reviews_train.tsv')
# val_data = utils.load_data('reviews_val.tsv')
# test_data = utils.load_data('reviews_test.tsv')
#
# train_texts, train_labels = zip(*((sample['text'], sample['sentiment']) for sample in train_data))
# val_texts, val_labels = zip(*((sample['text'], sample['sentiment']) for sample in val_data))
# test_texts, test_labels = zip(*((sample['text'], sample['sentiment']) for sample in test_data))
#
# dictionary_2 = p1.bag_of_words_2(train_texts)
#
# train_bow_features_2 = p1.extract_bow_feature_vectors_2(train_texts, dictionary_2)
# val_bow_features_2 = p1.extract_bow_feature_vectors_2(val_texts, dictionary_2)
# test_bow_features_2 = p1.extract_bow_feature_vectors_2(test_texts, dictionary_2)
# theta_2,theta_0_2=p1.pegasos(train_bow_features_2,train_labels,T=25,L=0.0100)
# preds_2=p1.classify(test_bow_features_2,theta_2,theta_0_2)
# accuracy=p1.accuracy(preds_2,test_labels)
# print(accuracy)



#1.  the given data can be loaded from utils.load_data(data_file _name)
#2. the data contains texts and curesp labels those have to extracted and assigned to text and labels by this codes i ddont understand
#3. now this part does most of the work, making he feature vector!
    # general aproach is by makin a dictionary that has  all the words and making a feature vector of the legth of the dictionary
    # but we are free to make whatever the kind of dictoionary
    # best ways to feature eengineer are either by making diffenrt ssort of feature vectors from adictionary of making very differen
    # sort of dictionary ad feature engineer on that

    # train bow features function makes the feature vector from dictionary
    # also it takes a lot of functions(helper functions)-look at how it is written y'll understad
#4. then we'll apply those feature vectors(training feature vectors, this is training!) in the pegasos algorithm (which is by far the best algorithm
# which uses the gradient descent sort of update based on each data poit it encounters)
#5. finally a function called classify takes this output and (theta nd theta_0 from the pegasos mensioned above)and
# clssifies the test _feature vectors theis is the output we have produced from the ml algo and now this is compared
# with its original labels since its a superwised learning problem using  an accuracy function