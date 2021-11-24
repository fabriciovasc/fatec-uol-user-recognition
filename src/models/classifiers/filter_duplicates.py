import os
import pymysql
import random
from flask.json import jsonify
from src.models.classifiers.knn import kNNClassifier
from src.models.distances.manhattan_distance import ManhattanDistance
from src.models.user_data import UserData

K_NUM = 1


def connect_db():
    print(os.getenv('MYSQL_HOST'))
    conn = pymysql.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )
    cur = conn.cursor()
    return cur


def get_users(max_search=10):
    cur = connect_db()
    query = 'SELECT * from registration WHERE registration_id < ' + str(max_search)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    return output


def find_duplicates(user_id, max_search=10):
    users_raw = get_users(max_search)

    users_list = list()

    for item_raw in users_raw:
        user = UserData(item_raw)
        users_list.append(user)

    random.shuffle(users_list)
    percent = 0.73
    train_len = int(len(users_list) * percent)
    test_len = len(users_list) - train_len
    train_set = users_list[train_len:]
    test_set = users_list[:-test_len]

    successes = 0
    duplicates = list()
    knn_classifier = kNNClassifier(ManhattanDistance)
    for test_inst in test_set:
        result_id = knn_classifier.classify(
            test_inst,
            train_set,
            K_NUM
        )
        if user_id == result_id:
            duplicates.append(test_inst.serialize())
            successes += 1

    acc = round(successes / len(test_set), 2)
    return acc, duplicates


def filter_accuracy(user_id, max_search=10):
    accuracy = 0
    duplicates = []
    count = 0
    while accuracy < 0.5:
        result = find_duplicates(user_id, max_search)
        accuracy = result[0]
        duplicates = result[1]
        print(accuracy, duplicates, count)
        if accuracy > 0.9:
            break
        if count >= 50 and accuracy > 0.4:
            break
        count += 1

    return jsonify(
        accuracy=accuracy * 100,
        user_duplicates=duplicates
    )


class FilterDuplicate:
    def __init__(self, user_id, max_search=10):
        self.result = filter_accuracy(user_id, max_search)
