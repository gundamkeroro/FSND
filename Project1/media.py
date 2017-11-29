class Movie():
	"""This class has a function:
	   __init__(self, movie_title, movie_story, movie_poster, movie_url)
	   creates a new movie object.
	"""

	def __init__(self, movie_title, movie_story, movie_poster, movie_url):
		self.title = movie_title
		self.story = movie_story
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_url
		
