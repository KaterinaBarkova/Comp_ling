from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
import re
import pymorphy2
from collections import Counter
from operator import itemgetter
from wordcloud import WordCloud
from matplotlib import pyplot as plt

morph = pymorphy2.MorphAnalyzer()

# обработка текста
def preprocessing(text):
    text = re.sub('''[№!"#$%&'()*+,./:;<=>?@[\]^_`{|}~…]''', ' ', text) # удалить знаки пунктуации
    text = re.sub('''[ё]''', 'е', text)
    text = text.lower() # преобразовать все буквы в нижний регистр
    text = word_tokenize(text)
    text = [word for word in text if len(word) > 1]
    _stopwords = stopwords.words('russian')
    _stopwords.extend(['который', 'это', 'также', 'свой'])
    text = [word for word in text if word not in _stopwords]
    return text # вернуть токены

# нормальная форма
def normalize(text):
    normalized = []
    for word in text:
        p = morph.parse(word)[0]
        p = p.normal_form
        normalized.append(p) 
    return " ".join(normalized)

neib_names = ["krl", "kuntsevo", "vnukovo", "Vernadskogo", "troparevo", "solntsevo", "ramenki", "ochakovo", "NP", "FP", "fili", "Dorogomilovo"]
corpus = ["", ""]
for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/news/kuntsevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[0] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/vnukovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/Vernadskogo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()        

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/troparevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/solntsevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/ramenki"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/ochakovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/NP"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/FP"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/fili"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()

for i in range(280):
    with open("/Users/Катя/Documents/КЛ2020/news/Dorogomilovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        corpus[1] += f.read()                                                

corpus[0] = normalize(preprocessing(corpus[0]))
corpus[1] = normalize(preprocessing(corpus[1]))
print("Corpus normalized")

_all = [corpus[0] + corpus[1]]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(corpus) 
feature_names = vectorizer.get_feature_names()
# print(feature_names) # получить все слова
# print(X.toarray()) # получить все веса 
# print(X.toarray()[0][feature_names.index('москва')])

dct = {"krl": [], "kuntsevo": [], "vnukovo": [], "Vernadskogo": [], "troparevo": [], "solntsevo": [], "ramenki": [], "ochakovo": [], "NP": [], "FP": [], "fili": [], "Dorogomilovo": []}

for i, document in enumerate(corpus):
    X = vectorizer.transform([document])

    tfidf_scores = [(feature_names[col], X[0, col]) for col in X.nonzero()[1]]
    freq_list = [(word, freq) for word, freq in sorted(tfidf_scores, 
                                                        key=itemgetter(1), 
                                                        reverse=True) if word not in ["который"]]

    print("freq_list counted")
    print(freq_list[:11]) # Самые значимые слова для одного района 
    dct[neib_names[i]] = freq_list[:11]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(_all) # самые важные слова для всех районов
feature_names = vectorizer.get_feature_names()

# print(X.toarray()[0][feature_names.index('москва')])
all_weigths = []

for i, document in enumerate(_all):
    X = vectorizer.transform([document])

    tfidf_scores = [(feature_names[col], X[0, col]) for col in X.nonzero()[1]]
    freq_list = [(word, freq) for word, freq in sorted(tfidf_scores, 
                                                        key=itemgetter(1), 
                                                        reverse=True) if word not in ["который"]]

    print("freq_list counted")
    print(freq_list[:11]) # Самые значимые слова для одного района 
    all_weigths = freq_list[:11]

print(dct)
print(all_weigths)

wc = WordCloud(width=2600, height=2200, background_color="white", relative_scaling=1.0,
            min_font_size=10).generate_from_frequencies(dict(dct['krl']))
plt.imshow(wc, interpolation="bilinear")

wc = WordCloud(width=2600, height=2200, background_color="white", relative_scaling=1.0,
            min_font_size=10).generate_from_frequencies(dict(all_weigths))
plt.imshow(wc, interpolation="bilinear")
plt.show()