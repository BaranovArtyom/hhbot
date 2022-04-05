from peewee import Model, SqliteDatabase, IntegerField, TextField, AutoField, DateTimeField
from config import DB_NAME

db = SqliteDatabase(DB_NAME)


class User(Model):
    """
    id (int): автоинкремент
    user_id (int): ID пользователя
    chat_id (int): ID чата
    num_vacancies (int): количество вакансий в запросе
    vacancy_id (int): ID вакансии
    search_time (datetime): время запроса
    vacancy_url (list[str]): ссылки на найденные вакансии
    """
    id = AutoField(primary_key=True)
    user_id = IntegerField()
    chat_id = IntegerField()
    city = TextField(null=True)
    num_vacancies = IntegerField(null=True)
    vacancy_id = IntegerField()
    search_time = DateTimeField()
    vacancy_url = TextField()

    class Meta:
        database = db


db.connect()
User.create_table(True)
db.close()
