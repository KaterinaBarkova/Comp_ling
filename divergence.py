from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

krl = "" 
for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/news/krl"+str(i)+".txt", "r", encoding="utf-8") as f:
        krl += f.read() + "\n" 

all_news = "" 
for i in range(280):
    # with open("news/krl"+str(i)+".txt", "r") as f:
    #     all_news += f.read() + "\n" 

    with open("C:/Users/Катя/Documents/КЛ2020/news/news/kuntsevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/vnukovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/Vernadskogo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()        

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/troparevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/solntsevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/ramenki"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/ochakovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/NP"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/FP"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/fili"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/Dorogomilovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

corpus = [krl, all_news]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus) 

probs = [] 
freqs = X.toarray() 
for freq in freqs:
    amount = np.sum(freq)
    probs.append(freq / amount)

# print(probs)
a = probs[0]
b = probs[1]
 
d = distance.jensenshannon(a, b, 2.0) 
print(d) 