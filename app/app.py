from flask import Flask
from app.views import NewsEnterView


app = Flask(__name__)

app.add_url_rule('/', view_func=NewsEnterView.as_view('news'))


#if __name__ == "__main__":
    #reader = DataReader()
    #data = reader.read()
    #judge = NewsJudge()
    #judge.run(runtype="TRAIN")
