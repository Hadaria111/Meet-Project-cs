from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from textblob import TextBlob
engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_video_by_name(video_name):
  video = session.query(Video).filter_by(name=video_name).first()
  print(video)
  return video

def get_video_by_artist(video_artist):
  video = session.query(Video).filter_by(artist=video_artist).first()
  return video

def add_video(name, artist, genre, link):
	if get_video_by_name(name) == None and get_video_by_artist(artist) == None:
	    Video_object = Video(
	        name = name,
	        artist=artist,
	        # year = year,
			genre = genre, 
	        link = link,
	        # is_in_cart = False
	        )
	    session.add(Video_object)
	    session.commit()


def get_video_by_genre(genre):
  Videos = session.query(Video).filter_by(genre=genre).all()
  return Videos
review_genre_int = 0
review_indie_int = 0
review_rock_int = 0
review_pop_int = 0
def review_genre(think_of_genre, genre):
	global review_genre
	global review_rock
	global review_pop
	global review_indie
	global review_genre_answer
	global review_genre_int
	global review_rock_int
	global review_pop_int
	global review_indie_int
	review_genre = TextBlob(think_of_genre)
	if genre == "rock":
		review_rock = TextBlob(think_of_genre)
		review_rock_int = review_rock_int + review_genre.sentiment.polarity
		if review_rock_int < 0:
			review_genre_answer = "Most of the reviews on this genre are negative :("
		elif review_rock_int > 0:
			review_genre_answer = "Most of the reviews on this genre are positive :)"
		else:
			review_genre_answer = "The reviews on this genre are natrual"
	elif genre == "pop":
		review_pop = TextBlob(think_of_genre)
		review_pop_int = review_pop_int + review_genre.sentiment.polarity
		if review_pop_int < 0:
			review_genre_answer = "Most of the reviews on this genre are negative :("
		elif review_pop_int > 0:
			review_genre_answer = "Most of the reviews on this genre are positive :)"
		else:
			review_genre_answer = "The reviews on this genre are natrual"
	elif genre == "indie":
		review_indie = TextBlob(think_of_genre)
		review_indie_int = review_indie_int + review_genre.sentiment.polarity
		if review_indie_int < 0:
			review_genre_answer = "Most of the reviews on this genre are negative :("
		elif review_indie_int > 0:
			review_genre_answer = "Most of the reviews on this genre are positive :)"
		else:
			review_genre_answer = "The reviews on this genre are natrual"
	else:
		review_genre_answer = "The reviews on this genre are natrual"
	return review_genre_answer


import requests


## function that gets the random quote
def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']

			## getting the quote from the data
			print(data[0]['quoteText'])
			return(data[0]['quoteText'])
		else:
			print("Error while getting quote")
	except:
		print("Something went wrong! Try Again!")


# TODO: Add your database functions below this line!