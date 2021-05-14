import pandas as pd
import numpy as np
from textblob import TextBlob
import mtranslate as translate
from langdetect import detect
import re

file = "chennai_reviews.xls"
hotel_name = "Accord Metropolitan"


def get_general_sentiment(opinions):
    pos = 0
    neg = 0
    neu = 0
    err = 0

    pos_cm = []
    neg_cm = []
    neu_cm = []
    count = 0

    if len(opinions) != 0:
        # np.shape(opinions)[0]
        for i in range(0, np.shape(opinions)[0]):
            print(i)
            opinion = opinions[i][1]

            if "<U+" not in opinion:
                if bool(re.match('.*[a-zA-Z].*', str(opinion))):
                    blob = TextBlob(opinion)
                    # lang = language_detect.detect_language(opinion)
                    lang = detect(opinion)

                    if lang != 'en':
                        # print(blob.detect_language())
                        # print(blob)

                        opinion_tr = translate.translate(str(opinion), "en")
                        blob = TextBlob(opinion_tr)
                    # print(str(i) + " " + str(blob))

                    if blob.sentiment.polarity > 0:
                        pos += 1
                        pos_cm.append([opinions[i][1], opinions[i][2]])
                    if blob.sentiment.polarity < 0:
                        neg += 1
                        neg_cm.append([opinions[i][1], opinions[i][2]])
                    if blob.sentiment.polarity == 0:
                        neu += 1
                        neu_cm.append([opinions[i][1], opinions[i][2]])
                    count += 1
            else:
                err += 1

        pr_pos = pos / count * 100;
        pr_pos = str(int(round(pr_pos, 0)))
        pr_neg = neg / count * 100;
        pr_neg = str(int(round(pr_neg, 0)))
        pr_neu = neu / count * 100;
        pr_neu = str(int(round(pr_neu, 0)))

        print("positive = {}% '45 Park , {} in {} opinions".format(pos / count * 100, pos, count))
        print("negative = {}% , {} in {} opinions".format(neg / count * 100, neg, count))
        print("neutre = {}% ,{} in {} opinions".format(neu / count * 100, neu, count))

        return [count, pos, neg, neu, pr_pos, pr_neu, pr_neg,pos_cm,neg_cm,neu_cm]
    else:
        return "error"


def get_general_review(file, hotel_name):
    hotel = []
    liste = []
    data = pd.read_excel(file)  # reading file

    exist = 0
    for i in data.index:
        if data['Hotel_name'][i] == hotel_name:
            exist = 1
            break

    if exist == 1:
        for i in data.index:
            if data['Hotel_name'][i] == hotel_name:
                # print(data[['Hotel_name', 'Review_Text']].ix[i])
                hn = data['Hotel_name'][i]
                htr = data['Review_Text'][i]
                htru = data['Review_Username'][i]
                hotel.append([hn, htr, htru])
                # liste.append(htr)

    list_pr = get_general_sentiment(hotel)
    return list_pr

# --------------------------------------

def get_filter_sentiment(opinions, filter):
    pos = 0
    neg = 0
    neu = 0
    err = 0
    pos_cm = []
    neg_cm = []
    neu_cm = []
    count = 0
    b=True

    if len(opinions) != 0:
        #np.shape(opinions)[0]
        for i in range(0, np.shape(opinions)[0]):
            opinion = opinions[i][1]

            if "<U+" not in str(opinion):
                if bool(re.match('.*[a-zA-Z].*', str(opinion))):
                    blob = TextBlob(opinion)
                    # lang = language_detect.detect_language(opinion)
                    lang = detect(opinion)

                    if lang != 'en':
                        # print(blob.detect_language())
                        # print(blob)

                        opinion_tr = translate.translate(str(opinion), "en")
                        blob = TextBlob(opinion_tr)

                    print(i)

                    for word in filter:
                        if word in str(blob):

                            if blob.sentiment.polarity > 0:
                                pos += 1
                                pos_cm.append([opinions[i][1], opinions[i][2]])
                            if blob.sentiment.polarity < 0:
                                neg += 1
                                neg_cm.append([opinions[i][1], opinions[i][2]])
                            if blob.sentiment.polarity == 0:
                                neu_cm.append([opinions[i][1], opinions[i][2]])
                                neu += 1
                            count += 1

                            # print(str(i) + " " + word + " " + str(blob))

                            break
            else:
                err += 1

        if count != 0:
            print("positive = {}% , {} in {} opinions".format(pos / count * 100, pos, count))
            print("negative = {}% , {} in {} opinions".format(neg / count * 100, neg, count))
            print("neutre = {}% ,{} in {} opinions".format(neu / count * 100, neu, count))

            pr_pos = pos / count * 100;
            pr_pos = str(int(round(pr_pos, 0)))
            pr_neg = neg / count * 100;
            pr_neg = str(int(round(pr_neg, 0)))
            pr_neu = neu / count * 100;
            pr_neu = str(int(round(pr_neu, 0)))

            return [count, pos, neg, neu, pr_pos, pr_neu, pr_neg, pos_cm, neg_cm, neu_cm]
        else:
            return [0,0,0,0,0,0,0,[],[],[]]
    else:
        return "error"


def get_filter_review(file, hotel_name, filter):
    hotel = []
    liste = []
    data = pd.read_excel(file)  # reading file

    exist = 0
    for i in data.index:
        if data['Hotel_name'][i] == hotel_name:
            exist = 1
            break

    if exist == 1:
        for i in data.index:
            if data['Hotel_name'][i] == hotel_name:
                # print(data[['Hotel_name', 'Review_Text']].ix[i])
                hn = data['Hotel_name'][i]
                htr = data['Review_Text'][i]
                htru = data['Review_Username'][i]
                hotel.append([hn, htr, htru])
                liste.append(htr)

    return get_filter_sentiment(hotel, filter)

# ----------------------------------------

def get_all_reviews(file, hotels, filter):

    list_pos_y = []
    list_neg_y = []

    list_x = []

    i = 0
    for hotel in hotels:
        print(i)
        print(hotel)
        if filter != []:
            list_pr = get_filter_review(file, hotel, filter)
        else:
            list_pr = get_general_review(file, hotel)
        list_pos_y.append(int(list_pr[4]))
        list_neg_y.append(int(list_pr[6]))
        list_x.append(hotel)
        i += 1

    # print(list_x)
    # print(list_pos_y)

    return [list_pos_y,list_neg_y,list_x]

# --------------------------------------
if __name__ == '__main__':

    file = "chennai_reviews.xls"
    hotel_name = "The Park Chennai"

    filter = " "
    service = ["service", "waiter", "waitress", "employee", "lobby", "welcome", "reception", "staff", "porter",
               "security", "room-service", "internet", "wifi", "wi-fi"]
    location = ["place", "environment", "location"]
    rooms = ["rooms", "bathrooms", "toilet", "bed","sleep", "deco", "decoration", "room-service", "views","view", "quiet","noisy","compfort", "chic"]
    food = ["food", "restaurante", "tea", "drinks", "dinner", "lunch", "breackfast", "cuisine", "kitchen", "buffet"]
    cleanliness = ["clean", "concierge", "laundry", "dirty", "cleanliness", "smell", "cleaness","grose"]
    price = ["price", "moneye", "pricing", "pricey", "expensive", "super-expensive", "cheap"]
    entertainment = ["pool", "bar", "theater", "party", "spectacle", "sport"]

    if filter == " ":
        get_general_review(file, hotel_name)
    else:
        if filter == "service":
            get_filter_review(file, hotel_name, service)
        elif filter == "location":
            get_filter_review(file, hotel_name, location)
        elif filter == "rooms":
            get_filter_review(file, hotel_name, rooms)
        elif filter == "food":
            get_filter_review(file, hotel_name, food)
        elif filter == "price":
            get_filter_review(file, hotel_name, price)
        elif filter == "cleanliness":
            get_filter_review(file, hotel_name, cleanliness)
        elif filter == "entertainment":
            get_filter_review(file, hotel_name, entertainment)

    # data = pd.read_excel("london_reviews.xls")
    # print(data)
