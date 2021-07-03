from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def classify(news):
    with open("Tfidfvocab", "r", encoding="utf-8") as f:
        vocab = f.read() # прочитали все слова в одну строку
        vocab = vocab.split("\n") # разбили на список (символ \n удалился)

    vectorizer = TfidfVectorizer(max_df=1, min_df=1, 
                                 vocabulary=vocab # классификация на словах, по которым обучались
                                )
    X = vectorizer.fit_transform(news["union_pr"])
    X = X.toarray()

    model = joblib.load("LinearSVCmodel_79%")
    return model.predict(X)

def get_news_by_cat(news, user_choice, cats):
    headlines = []
    short_descriptions = []
    for i, cat in enumerate(cats):
        if cat == user_choice:
            headline = news["headline"].iloc[i]
            short_desc = news["short_description"].iloc[i]
            headlines.append(headline) 
            short_descriptions.append(short_desc) 
    
    result = list(zip(headlines, short_descriptions))
    return result
    