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


def sp_recog(word):
    stat=0
    for i in word:
        if i.isalpha()==True:
            stat=0
        else:
            stat=1
            break
    return stat

def cout_sp(words):
    count=0
    for word in words:
        for i in word:
            if i.isalpha()==False:
                count+=1
            else:
                count+=0
    return count

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

#checking for sspecial char   accuracy low!! 0.736(of course in test data)
def extract_bow_features_5(reviews,dictionary):
    num_reviews = len(reviews)
    feature_matrix = np.zeros([num_reviews, len(dictionary)+1])
    for i, text in enumerate(reviews):
        word_list = p1.extract_words(text)
        for word in word_list:
            value=sp_recog(word)
            if (word in dictionary) and (word.islower()==True) and (value==0): #lower and no sp_char in featu vec 1
                feature_matrix[i, dictionary[word]] = 1
            elif (word in dictionary) and (word.islower()==False) and (value==0): #upper and no sp_char in feat vec 2
                feature_matrix[i, dictionary[word]] = 2
            elif (word in dictionary) and (word.islower()==True) and (value==1): #lower and sp_char in feat vec 3
                feature_matrix[i, dictionary[word]] = 3
            elif (word in dictionary) and (word.islower()==False) and (value==1): #upper and sp_char in feat vec 4
                feature_matrix[i, dictionary[word]] = 4
        feature_matrix[i, len(dictionary)] = cout_sp(word_list)# also added the total number of char in sentance
    return feature_matrix
