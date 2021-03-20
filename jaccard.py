from sklearn.metrics import jaccard_score
from sklearn.feature_extraction.text import CountVectorizer

krl = "" 
for i in range(280):
    with open("C:/Users/Катя/Documents/КЛ2020/news/news/kuntsevo"+str(i)+".txt", "r", encoding="utf-8") as f:
        krl += f.read() + "\n" 

all_news = "" 
for i in range(280):
    # with open("news/krl"+str(i)+".txt", "r") as f:
    #     all_news += f.read() + "\n" 

    with open("C:/Users/Катя/Documents/КЛ2020/news/news/krl"+ str(i) + ".txt", "r", encoding="utf-8") as f:
        all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/vnukovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/Vernadskogo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()        

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/troparevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/solntsevo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/ramenki"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/ochakovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/NP"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/FP"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/fili"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()

# for i in range(280):
#     with open("C:/Users/Катя/Documents/КЛ2020/news/Dorogomilovo"+ str(i) + ".txt", "r", encoding="utf-8") as f:
#         all_news += f.read()      

corpus = [krl, all_news] 

vectorizer = CountVectorizer(binary =True) 
X = vectorizer.fit_transform(corpus) 
# print(vectorizer.get_feature_names())
# print(X.toarray())

A = X.toarray()[0]
B = X.toarray()[1]

jacc = jaccard_score(A,B)
print("Jaccard similarity: %.7f" % jacc)