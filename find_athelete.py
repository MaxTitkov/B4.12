import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from collections import defaultdict


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

def convert_datetime(date):
	datetime_format = '%d.%m.%Y'
	datetime_object = datetime.strptime(date, datetime_format)
	return datetime_object


def closest_date(users, checking_user):
	birthdates_differenses = defaultdict(datetime)
	for user in users:
		if user.id != checking_user.id:
			birthdates_differenses[user] = abs(convert_datetime(user.birthdate) - convert_datetime(checking_user.birthdate))
	
	return min(birthdates_differenses, key=birthdates_differenses.get)

def closest_height(users, checking_user):
	height_differenses = defaultdict(int)
	for user in users:
		if user.id != checking_user.id:
			height_differenses[user] = abs(user.height - checking_user.height)
	
	return min(height_differenses, key=height_differenses.get)

def find(user_id, session):
	query = session.query(User).filter(User.id == user_id).first()
	if query is not None:
		users =  session.query(User).all()
		closest_user_birthdate = closest_date(users, query)
		closest_user_height = closest_height(users, query)
		print("Рост пользователя с id {check_id} - {check_height} см. Ближе всего к нему пользователь с id - {height_id} {height_name} с ростом {height} см.\n".format(check_id = query.id, check_height = query.height, height_id=closest_user_height.id, height_name=closest_user_height.first_name, height=closest_user_height.height))
		print("Дата рождения пользователя с id {check_id} - {check_birthdate} см. Ближе всего к нему пользователь с id - {birthdate_id} {birthdate_name}. Его дата рождения: {birthdate}.\n".format(check_id = query.id, check_birthdate = query.birthdate, birthdate_id=closest_user_birthdate.id, birthdate_name=closest_user_birthdate.first_name, birthdate=closest_user_birthdate.birthdate))
	else:
		print("Пользователя с таким id нет в базе")
