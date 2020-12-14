from wtforms import Form, BooleanField, StringField, validators, TextAreaField


class NewsForm(Form):
    title = StringField("Article title", [validators.length(min=3, max=255), validators.required()])
    text = TextAreaField("ArticleText", [validators.length(min=100, max=12000), validators.required()],
                         render_kw={'class': 'form-control', 'rows': 50, 'cols': 100})


class WasItFakeForm(Form):
    was_it_real = BooleanField("Was it real?", [validators.required()])
