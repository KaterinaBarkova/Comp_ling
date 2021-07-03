import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('wordnet')

contractions = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how does",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
" u ": " you ",
" ur ": " your ",
" n ": " and ",
"won't": "would not",
"you're": "you are",
"you'll": "you will",
"you've": "you have",
"you'd": "you would",
"you'd've": "you would have",
"you'll've": "you will have",
"here's" : "here is",
"there's" : "there is",
"where's": "where is"
}

def proprocess(text):
    text = re.sub("[\W ]+", " ", text) # Удаляем специальные символы
    text = text.lower()
    for cont in contractions: # перебираем ключи словаря
        if cont in text:
            text = text.replace(cont, contractions[cont])
    return text

stop_words = stopwords.words('english')
def remove_stops(text):
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]
    return text

lemmatizer = nltk.stem.WordNetLemmatizer()
def lemmatize(text):
    text = [lemmatizer.lemmatize(word) for word in text]
    return text

def apply_prep(news):
    news["union_pr"] = news.apply(lambda x: x["headline"] + " " + x["short_description"], axis=1)
    news["union_pr"] = news["union_pr"].apply(lambda x: remove_stops(proprocess(x)))
    news["union_pr"] = news["union_pr"].apply(lambda x: " ".join(lemmatize(x)))
    return news