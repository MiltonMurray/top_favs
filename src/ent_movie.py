import media
import fresh_tomatoes

furious_eight = media.Movie("Fate of the Furious",
                           "The Betrayal of Dominic Tereto",
                           "https://cdn.traileraddict.com/content/universal-pictures/fast8-4.jpg",
                           "https://www.youtube.com/watch?v=JwMKRevYa_M")
#print (furious_eight.storyline)
#furious_eight.show_trailer()
pursuit_of_happiness = media.Movie("The Pursuit of Happiness",
                           "Once homeless, Christopher Gardner (Smith) turns his life around and becomes the head of his own brokerage firm",
                           "http://www.sonypictures.com/movies/thepursuitofhappyness/assets/images/onesheet.jpg",
                           "https://www.youtube.com/watch?v=SYg7RRYKWGw")
seven_pounds = media.Movie("Seven Pounds",
                           "A strange IRS agent uses his database to locate a series of needy people and goes to elaborate lengths to improve their lives."+
                           "During the process, he falls in love with a woman in need of a new heart. It's only after he's killed "+
                           "himself and everyone's benefitted from his generosity that we learn who he really was and "+
                           "why he did what he did.",
                           "https://cdn.traileraddict.com/content/columbia-pictures/seven_pounds.jpg",
                           "https://www.youtube.com/watch?v=MwrtEI-fcmM")
her = media.Movie("Her",
                           "Theodore Twombly, a complex, soulful man who makes his living writing touching, personal letters for other people.",
                           "http://www.impawards.com/2013/posters/her.jpg",
                           "https://www.youtube.com/watch?v=ne6p6MfLBxc")
arrival = media.Movie("The Arrival",
                           "When mysterious spacecrafts touch down across the globe, an elite team - lead by expert linguist Louise Banks (Amy Adams) - is brought together to investigate.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_UY1200_CR69,0,630,1200_AL_.jpg",
                           "https://www.youtube.com/watch?v=tFMo3UJ4B4g")
limitless = media.Movie("Limitless",
                           "Bradley Cooper and Robert De Niro star in Limitless, a paranoia-fueled action thriller about an unsuccessful writer whose life is transformed.",
                           "http://www.impawards.com/2011/posters/limitless.jpg",
                           "https://www.youtube.com/watch?v=jOLqNOfzus4")
beyond_the_pines = media.Movie("The Place Beyond the Pines",
                           "A motorcycle stunt rider considers committing a crime in order to provide for his wife and child, an act that puts him on a collision course with a cop-turned-politician.",
                           "https://upload.wikimedia.org/wikipedia/en/0/04/The_Place_Beyond_the_Pines_Poster.jpg",
                           "https://www.youtube.com/watch?v=G07pSbHLXgg")
charlie_countryman = media.Movie("The Necessary Death of Charlie Countryman",
                           "A footloose young man must undergo a dark and brutal trial by fire to save the love of his life in this flashy, violent adventure saga .",
                           "http://www.impawards.com/2013/posters/charlie_countryman_ver3.jpg",
                           "https://www.youtube.com/watch?v=YCPC0DGr44s")
movies = [furious_eight, pursuit_of_happiness, seven_pounds, her, arrival, limitless, beyond_the_pines, charlie_countryman]
fresh_tomatoes.open_movies_page(movies)
