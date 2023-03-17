# Results

With the exception of F7, which has 0 accuracy, recall, and f1-score for the "hate" label, all feature sets consistently perform well using the logistic regression approach. The performance of the Random Forest classifier is significantly harmed when tf-idf scores are not included in the feature set, but it performs rather well when it comes to F1 and also exhibits substantial performance in all other feature sets. For the objective of categorising tweets into hate, offensive, or neither categories, the Nave Bayes classifier's overall performance is shown to be less significant; nevertheless, when compared to other feature sets, it performs noticeably better with the F7 feature set. The sentiment ratings demonstrate their value as a distinguishing factor between hate speech and offensive language. Doc2vec columns are not determined to be highly relevant for classification purposes because their removal from the feature set barely changes the results. When comparing all of the aforementioned graphs, Random Forest is by far the winner. 

## Before Sentiment Analysis

![alt text](https://github.com/huehue26/detoxer/blob/main/img/result.png?raw=true)

## After Sentiment Analysis

![alt text](https://github.com/huehue26/detoxer/blob/main/img/sentiment_result.png?raw=true)

## Testing

Discord Bot Testing

![alt text](https://github.com/huehue26/detoxer/blob/main/img/testing.png)
