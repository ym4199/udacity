from lesson6 import media
from lesson6 import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=d9IxdwEFk1c&list=RDEM79RRQ105L7V61p68gX8ahw")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://image-proxy.namuwikiusercontent.com/r/https%3A%2F%2Fncache.ilbe.com%2Ffiles%2Fattach%2Fnew%2F20140713%2F1349949%2F1835525709%2F3880417504%2Facbafc9bfca6b24842a6da40bbc9ba03.jpg",
                     "https://www.youtube.com/watch?v=d9IxdwEFk1c&list=RDEM79RRQ105L7V61p68gX8ahw")

the_circle = media.Movie(
    "The Circle",
    "가장 투명하고 완벽한 세상",
    "http://img.cgv.co.kr/Movie/Thumbnail/Poster/000079/79675/79675_1000.jpg",
    "https://www.youtube.com/watch?v=iwPglAKl4yQ",
)



movies = [toy_story, avatar, the_circle]
# fresh_tomatoes.open_movies_page(movies)


print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)