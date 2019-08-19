import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.INTEGER, primary_key=True)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)


def request_data():

	first_name = input("Введите имя: ")
	last_name = input("Введите фамилию: ")
	gender = input("Введите пол: 1-Мужской, 2-Женский; ")
	email = input("Введите почту: ")
	birthdate = input("Введите дату рождения в формате dd.mm.yyyy: ")
	height = input("Введите ваш рост (см): ")

	user = User(first_name = first_name,
		last_name = last_name,
		gender = gender,
		email=email,
		birthdate = birthdate,
		height = height)

	return user
