import numpy as np
from sentiment_analy import utils
from sentiment_analy import project1 as p1

# loading and assigning data
train_data = utils.load_data(r'C:\Users\USER\PycharmProjects\project_1\sentiment_analy\reviews_train.tsv')
val_data = utils.load_data(r'C:\Users\USER\PycharmProjects\project_1\sentiment_analy\reviews_val.tsv')
test_data = utils.load_data(r'C:\Users\USER\PycharmProjects\project_1\sentiment_analy\reviews_test.tsv')

train_texts, train_labels = zip(*((sample['text'], sample['sentiment']) for sample in train_data))
val_texts, val_labels = zip(*((sample['text'], sample['sentiment']) for sample in val_data))
test_texts, test_labels = zip(*((sample['text'], sample['sentiment']) for sample in test_data))


#applying length of the text into the feature vector taking the same dictionary wt all the
# words and feeding info about the length of the words and sentences
# very low accurady around 0.5 something
def extract_bow_features_3(reviews,dictionary):
    num_reviews = len(reviews)
    feature_matrix = np.zeros([num_reviews, len(dictionary)+1])
    for i, text in enumerate(reviews):
        word_list = p1.extract_words(text)
        length=0
        for word in word_list:
            length+=1
            if word in dictionary:
                feature_matrix[i, dictionary[word]] = 1
        feature_matrix[i, len(dictionary)]=length
    return feature_matrix



# here all the cap words goes by the number 2 in the feature matrix pretty good accuracy of 0.81
def extract_bow_features_4(reviews,dictionary):
    num_reviews = len(reviews)
    feature_matrix = np.zeros([num_reviews, len(dictionary)])
    for i, text in enumerate(reviews):
        word_list = p1.extract_words(text)
        for word in word_list:
            if (word in dictionary) and (word.islower()==True):
                feature_matrix[i, dictionary[word]] = 1
            elif (word in dictionary) and (word.islower()==False) :
                feature_matrix[i, dictionary[word]] = 2
    return feature_matrix

