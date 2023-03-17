# What problem do we solve?

Detoxer detects hate speech in online communication platforms, which is a significant problem that causes harm and violence towards individuals and communities. The automated detection of hate speech helps to promote a more positive and respectful online culture and can be a useful tool for preventing hate crimes and discrimination.

Through advanced machine learning techniques, the project can identify patterns and trends in hate speech, providing insights to researchers and policymakers to combat it. Ultimately, the project aims to create a safer and more inclusive online environment for everyone.

# Description

Detoxer, a bot for detecting hate speech which utilizes natural language processing (NLP) techniques to identify harmful and offensive language in messages sent on the Discord platform. The bot is designed to automatically monitor text channels and flag any messages that contain hate speech or derogatory language based on race, gender, religion, sexual orientation, or disability.

Once identified, the bot can take action such as deleting the message or issuing a warning to the user. Additionally, the bot can be customized to adapt to the specific needs of a community, such as adding or removing specific terms or phrases that are considered offensive or derogatory. The aim of the project is to create a safer and more inclusive space for Discord users by promoting respect and tolerance for diversity while also preventing the spread of hate speech.

# Result

With the exception of F7, which has 0 accuracy, recall, and f1-score for the "hate" label, all feature sets consistently perform well using the logistic regression approach. The performance of the Random Forest classifier is significantly harmed when tf-idf scores are not included in the feature set, but it performs rather well when it comes to F1 and also exhibits substantial performance in all other feature sets. For the objective of categorising tweets into hate, offensive, or neither categories, the Nave Bayes classifier's overall performance is shown to be less significant; nevertheless, when compared to other feature sets, it performs noticeably better with the F7 feature set. The sentiment ratings demonstrate their value as a distinguishing factor between hate speech and offensive language. Doc2vec columns are not determined to be highly relevant for classification purposes because their removal from the feature set barely changes the results. When comparing all of the aforementioned graphs, Random Forest is by far the winner.

## Before Sentiment Analysis

![alt text](https://github.com/huehue26/detoxer/blob/main/img/result.png?raw=true)

## After Sentiment Analysis

![alt text](https://github.com/huehue26/detoxer/blob/main/img/sentiment_result.png?raw=true)

# How to run

## Step 1

Clone the repo using\
```
git clone https://github.com/huehue26/detoxer
```

## Step 2
Go to the cloned repository using
```
ls detoxer
```

## Step 3
Make a .env file and add the variables required 
```
MONGODB_URI - MongoDB URI for connection

TOKEN - Discord Bot token for authentication
```

## Step 4
Run the main.py script using
```
python main.py
```

## Testing

Discord Bot Testing

![alt text](https://github.com/huehue26/detoxer/blob/main/img/testing.png)
