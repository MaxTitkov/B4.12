import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from users import request_data
from find_athelete import find



DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Athelete(Base):
	__tablename__ = "athelete"
	id = sa.Column(sa.INTEGER, primary_key=True)
	age = sa.Column(sa.INTEGER)
	birthdate = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)
	name = sa.Column(sa.TEXT)
	weight = sa.Column(sa.INTEGER)
	gold_medals = sa.Column(sa.INTEGER)
	silver_medals = sa.Column(sa.INTEGER)
	bronze_medals = sa.Column(sa.INTEGER)
	total_medals = sa.Column(sa.INTEGER)
	sport = sa.Column(sa.TEXT)
	country = sa.Column(sa.TEXT)

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.INTEGER, primary_key=True)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)


def connect_db():
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def main():
	session = connect_db()
	mode = input("Выбери режим.\n1 - ввести нового пользователя\n2 - найти ближайших по дате рождения и росту\n")
	if mode == "1":
		user = request_data()
		session.add(user)
		session.commit()
		print("Данные сохранены")
	elif mode == "2":
		user_id = input("Введите идентификатор пользователя: ")
		user_name = find(user_id, session)
	else:
		print("Некорректный режим")

if __name__ == "__main__":
	main()
