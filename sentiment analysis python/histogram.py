import matplotlib.pyplot as plt
from main import *
import hotels_list


file = "chennai_reviews.xls"


def histogram(file, filter, filter_pos_neg, list_hotel):
    service = ["service", "waiter", "waitress", "employee", "lobby", "welcome", "reception", "staff", "porter",
               "security", "room-service", "internet", "wifi", "wi-fi"]
    location = ["place", "environment", "location", "area", "position", "region", "neighborhood"]
    rooms = ["rooms", "bathrooms", "toilet", "bed", "sleep", "decoration", "room service", "views", "quiet", "chic",
             "comfort", "noisy"]
    food = ["food", "restaurant", "tea", "drinks", "coffee", "dinner", "lunch", "breakfast", "cuisine", "tasty",
            "kitchen", "buffet", "delicious"]
    cleanliness = ["clean", "concierge", "laundry", "dirty", "cleanliness", "smelly", "cleaness", "smell", "grose",
                   "stinky"]
    price = ["price", "money", "pricing", "pricey", "expensive", "cheap", "cost", "discount"]
    entertainment = ["entertainment", "pool", "bar", "theater", "party", "spectacle", "sport"]

    list_y = []

    if filter == "service":
        list_y = get_all_reviews(file, list_hotel, service)
    elif filter == "location":
        list_y = get_all_reviews(file, list_hotel, location)
    elif filter == "rooms":
        list_y = get_all_reviews(file, list_hotel, rooms)
    elif filter == "food":
        list_y = get_all_reviews(file, list_hotel, food)
    elif filter == "price":
        list_y = get_all_reviews(file, list_hotel, price)
    elif filter == "cleanliness":
        list_y = get_all_reviews(file, list_hotel, cleanliness)
    elif filter == "entertainment":
        list_y = get_all_reviews(file, list_hotel, entertainment)
    elif filter == "all":
        list_y = get_all_reviews(file, list_hotel, [])

    # x = ["h1","h2","h3","h4","h5","h6","h7","h8","h9","h10"]
    # y = [50.4,46.3,10,20,5,50,46,80,20,5]

    x = list_hotel
    xpos = np.arange(len(x))


    y1 = list_y[0]

    y2 = list_y[1]

    # x = ['Aadithya', 'Abu sarovar portico ex Abu Palace', 'Accord Metropolitan', 'Akash Inn']
    # y = [100, 57, 94, 100]
    plt.close('all')
    if filter_pos_neg == "posneg":
        plt.bar(xpos , y1, width=0.2, label="positive", color="green")
        plt.bar(xpos + 0.2, y2, width=0.2, label="negative", color="red")
    if filter_pos_neg == "positive":
        plt.bar(x, y1, label="positive",color="green")
    if filter_pos_neg == "negative":
        plt.bar(x, y2, label="negative",color="red")

    axes = plt.gca()
    axes.set_ylim([0,100])

    plt.xticks(rotation=90)
    plt.xticks(xpos, x)
    plt.xlabel("hotels")
    plt.ylabel("review %")
    if filter_pos_neg == "positive":
        plt.title("positive " + filter + " reviews histogram")
    if filter_pos_neg == "negative":
        plt.title("negative " + filter + " reviews histogram")
    if filter_pos_neg == "posneg":
        plt.title("positive & negative " + filter + " reviews histogram")

    plt.legend()
    plt.tight_layout()
    plt.show()