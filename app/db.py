from peewee import Model, CharField, TextField
from peewee import SqliteDatabase

db = SqliteDatabase("news.db")


class Article(Model):
    class Meta:
        database = db

    title = CharField()
    text = TextField()
    label = CharField(null=True, default=False)

    def load_csv_data(self):
        pass

    def export_to_csv_data(self):
        pass


# db.connect()
# db.create_tables([Article], safe=True)
# db.close()
