import media
import fresh_tomatoes
import webbrowser

# create three movie objects placed on web page.
Shawshank = media.Movie(
    "The Shawshank Redemption",
    "A story about true friendship in prison....",
    "https://upload.wikimedia.org/wikipedia/zh/th" +
    "umb/a/af/Shawshank_Redemption_ver2.jpg/220px-" +
    "Shawshank_Redemption_ver2.jpg",
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")

Les_Choristes = media.Movie(
    "Les Choristes",
    "A story between a music teacher and a talented young" +
    "singer",
    "https://upload.wikimedia.org/wikipedia/zh/3/33/Le" +
    "s_Choristes_movie.jpg",
    "https://www.youtube.com/watch?v=qhYtVMoWFNQ")

let_the_bullets_fly = media.Movie(
    "let the bullets fly",
    "A story between A hoodlum (Chow Yun-Fat) and his" +
    "town's new governor(Wen Jiang)",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b3/" +
    "Let_the_Bullets_Fly.jpg/220px-Let_the_Bullets_Fly.jpg",
    "https://www.youtube.com/watch?v=PFoLfRA5ghw")

movies = [Shawshank, Les_Choristes, let_the_bullets_fly]

# open browser 
fresh_tomatoes.open_movies_page(movies)


