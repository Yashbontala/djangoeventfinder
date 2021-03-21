import re
from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer, SnowballStemmer
from nltk import word_tokenize
import csv


def normalize_text(text):
    stopwords_set= set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')
    text = text.replace('\n',' ').lower().strip()
    text = re.sub("[^a-zA-Z]+", " ", text).split()
    text = ' '.join(stemmer.stem(i) for i in text)
    stemmed = ' '.join([word for word in text.split() if word not in stopwords_set])
    return(stemmed)

def if_topic_in(topic):
    topic_list = []
    with open('app\groups.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in data:
            if not first_line:
                t=normalize_text(row[0])
                words=word_tokenize(t)
                words.append(row[0])
                topic_list.append(words)
            else:
                first_line = False
    ans=[]
    for topics in topic_list:
        ls = set(topic).intersection(topics)
        if ls:
            ans.append(topics[-1])

    # print(ans)
    return ans
def find_topic(t):
    t= normalize_text(t)
    words=word_tokenize(t)
    topic=if_topic_in(words)
    return topic