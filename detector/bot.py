import sklearn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle

from detector.input_output_manager import DataReader


class NewsJudge:
    """
    This class is responsible for detecting validity of the news
    """
    # During news Judge run you should give the correct runtype.
    # TRAIN - causes training data model, once again, using newly collected_data (#TODO run it automatically in future)
    # JUDGE - type invoked by end user which wants to know if his news was correct or not.
    AVAILABLE_RUNTYPES = ["TRAIN", "JUDGE"]

    def __init__(self, *args, **kwargs):
        self.reader = DataReader()

    def judge(self, article_object):
        """
        Tells if given article is an True or False one
        :return:
        """
        pass

    def test_model(self, model, x_test, y_test):
        """
        This method simply tests model and returns its accuracy.
        """
        y_prediction = model.predict(x_test)
        score = sklearn.metrics.accuracy_score(y_test, y_prediction)
        return score

    def check_if_model_better(self, new_model, x_test, y_test):
        """
        This compares new and old models accuracy and returns True if new_model is better, else it returns False
        """
        try:
            pickle_in = open("fakeReviewer.pickle", "rb")
        except FileNotFoundError:
            return True
        old_model = pickle.load(pickle_in)
        new_acc = self.test_model(new_model, x_test, y_test)
        old_acc = self.test_model(old_model, x_test, y_test)

        if new_acc > old_acc:
            return True
        return False

    def train(self, data, labels):
        """
        Trains new model, if its better than the old one, it saves it to a file.
        """
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            data['text'], labels, test_size=0.2, random_state=7)
        vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
        x_train = vectorizer.fit_transform(x_train)
        x_test = vectorizer.transform(x_test)
        model = PassiveAggressiveClassifier(max_iter=1000)

        model.fit(x_train, y_train)

        if self.check_if_model_better(model, x_test, y_test):
            self.save_model(model)

        return model

    def save_model(self, model):
        """
        Saves given model into a pickle file.
        """
        with open("fakeReviewer.pickle", "wb") as file:
            pickle.dump(model, file)

    def run(self, runtype="JUDGE", news_data=None):
        """
        Runs the whole circus
        """
        try:
            assert runtype in self.AVAILABLE_RUNTYPES
        except AssertionError as e:
            print("Wrong given runtype! Available runtypes are: {}". format(self.AVAILABLE_RUNTYPES))
            return

        if runtype == "TRAIN":
            data = self.reader.read()
            labels = data.label
            self.train(data, labels)
        else:
            assert news_data
            self.judge(news_data)
