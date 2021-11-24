from flask import Flask, render_template, request
from database import *
import requests
import json
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'
review_rock_int = 0
review_rock_answer = "The review on this genre is natural"
global genre_thing
genre_thing = "0"
# TODO: Add all of the routes you want below this line!

@app.route("/",methods=['GET', 'POST'])
def index():
	if request.method =='GET': 
		print("hello")
	else:
		# name_of_song = "request.form['name_of_song']"
		# name_of_artist = "request.form['name_of_artist']"
		# genre_of_song = "request.form['genre_of_song']"
		# link_of_song = "request.form['link_of_song']"
		add_video(request.form['name_of_song'], request.form['name_of_artist'],request.form['genre_of_song'], request.form['link_of_song'])
# ()
	return render_template("index.html", random_quote = get_random_quote())

@app.route("/rock",methods=['GET', 'POST'] )
def rock():
	if request.method =='GET': 
		# global review_rock 
		# global review_rock_int
		global genre_thing
		genre_thing = "The reviews on this genre are  natural"
		if get_video_by_name("American Idiot") == None:
			add_video("American Idiot","Green Day","rock","https://www.youtube.com/embed/Ee_uujKuJMI")
		if get_video_by_name("Hang on to yourself") == None:
			add_video("Hang on to yourself", "Palaye royale", "rock", "https://www.youtube.com/embed/cjSobSYXo_8")
		if get_video_by_name("Don't stop me now") == None:
			add_video("Don't stop me now", "Queen", "rock", "https://www.youtube.com/embed/HgzGwKwLmgM")
	else:
	# 	genre_thing = "The reviews on this genre are natural"
	# 	review_rock = TextBlob(request.form['think_of_genre'])
	# 	review_rock_int = review_rock_int + review_rock.sentiment.polarity
	# 	print(review_rock.sentiment.polarity)
	# 	print(review_rock_int)
	# 	if review_rock_int < 0:
	# 		review_rock_answer = "Most of the reviews on this genre are negative :("
	# 	elif review_rock_int > 0:
	# 		review_rock_answer = "Most of the reviews on this genre are positive :)"
	# 	else:
	# 		review_rock_answer = "The reviews on this genre are natrual"
	# 	genre_thing = review_rock_answer
	# review_rock_int = review_rock_int
		genre_thing = review_genre(request.form['think_of_genre'], "rock")
	video_rock = get_video_by_genre("rock")
	return render_template("rock.html", Videos = video_rock, reviews = genre_thing )



@app.route("/pop", methods=['GET', 'POST'])
def pop():
	if request.method =='GET': 
		global genre_thing
		genre_thing = "The reviews on this genre are  natural"
		add_video("All too well","Taylor Swift","pop","https://www.youtube.com/embed/sRxrwjOtIag")
		add_video("Watermelon suger", "Harry Styles", "pop", "https://www.youtube.com/embed/E07s5ZYygMg?start=9")
		add_video("Good 4 u", "Olivia Rodrigo", "pop", "https://www.youtube.com/embed/gNi_6U5Pm_o?start=15")
	else:
		# review_genre(request.form['think_of_genre'])
		genre_thing = review_genre(request.form['think_of_genre'], "pop")
	video_pop = get_video_by_genre("pop")
	return render_template("pop.html", Videos = video_pop, reviews = genre_thing )


@app.route("/indie",methods=['GET', 'POST'])
def indie():
	if request.method =='GET': 
		global genre_thing
		genre_thing = "The reviews on this genre are  natural"
		add_video("Pretty Girl","Clario","indie","https://www.youtube.com/embed/mngtcfcaVrI?start=15")
		add_video("These Days", "Wallows", "indie", "https://www.youtube.com/embed/pgWZQr7r0l0?start=4")
		add_video("We fell in love in october", "Girl in red", "indie", "https://www.youtube.com/embed/iggmiF7DNoM?start=4")
	else:
		genre_thing = review_genre(request.form['think_of_genre'],"indie")
	video_indie = get_video_by_genre("indie")
	return render_template("indie.html", Videos = video_indie, reviews = genre_thing )


# @app.route('/vinly' ,methods=['GET', 'POST'] )
# def vinly():
# 	if request.method =='GET': 
# 		if get_product_by_album_name("The beatles collection:") == None:
# 			add_product("The beatles collection", "The beatles", 15 , 2005,"vinly", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-OgaptlOoNlO9Luf07KjE4ZaPGylrF6LcWQ&usqp=CAU")
		
# 		if get_product_by_album_name("How do you love?") == None:
# 			add_product("How do you love?", "The regrettes", 15 , 2005,"vinly", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnn9GdcMhPn2VCp9Uou9OFp3q5VbaTX24n7g&usqp=CAU")

# 		if get_product_by_album_name("Trust fall/ Just like a movie") == None:
# 			add_product("Trust fall/ Just like a movie", "wallows", 15 , 2005,"vinly",  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8RRQKVE8x9kBk0OJXIas_ghTyw_uYmVPSIQ&usqp=CAU")


	# else:
	# 	product_id = request.form["product_id"]
	# 	print(product_id)
	# 	update_product( product_id, True)
		# return render_template('vinly.html', products = query_all())

# @app.route('/rock', methods=['GET', 'POST'])
# def entry():
# 	if request.method =='GET': 
# 		print("hi")
# 		return render_template('cart.html')

# 	else:
#         username = request.form['username']
#         password = request.form['pass']
#     	return render_template('vinly.html',
#             name = username)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
