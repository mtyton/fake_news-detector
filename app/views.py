from flask.views import View
from flask.templating import render_template
from flask import request
from detector.input_output_manager import DataReader
from detector.bot import NewsJudge
from app.forms import NewsForm
from app.db import Article


class NewsEnterView(View):
    methods = ['GET', 'POST']

    def get_template_name(self):
        return "form.html"

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {}
        form = NewsForm(request.form)
        if request.method == 'POST':
            article = Article(title=form.data.get('title'), text=form.data.get('text'))
            article.save()
        context['form'] = form
        return self.render_template(context)


class NewsRecognizedView(View):
    methods = ['GET', 'POST']

    def get_template_name(self):
        return "success.html"

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {}
        form = NewsForm(request.form)
        if request.method == 'POST':
            article = Article(title=form.data.get('title'), text=form.data.get('text'))
            article.save()
        context['form'] = form
        return self.render_template(context)
