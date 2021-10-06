from sentiment_analy import project1 as p1
from files import fea_eng_functions as fea
dictionary= p1.bag_of_words_2(fea.train_texts)

train_bow_features= fea.extract_bow_features_5(fea.train_texts, dictionary)
val_bow_features = fea.extract_bow_features_5(fea.val_texts, dictionary)
test_bow_features= fea.extract_bow_features_5(fea.test_texts, dictionary)
theta,theta_0=p1.pegasos(train_bow_features,fea.train_labels,T=25,L=0.0100)
preds=p1.classify(test_bow_features,theta,theta_0)
accuracy=p1.accuracy(preds,fea.test_labels)
print(accuracy)

