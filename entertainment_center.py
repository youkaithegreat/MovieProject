import fresh_tomatoes
import media

#list of movies 
toy_story = media.Movie("Toy Story",
                        "A story of a boy and some toys",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_UY268_CR9,0,182,268_AL_.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4","PG-13","83/100","Animation")

avatar = media.Movie("Avatar", "A movie about a marine on an alien planet",
                     "http://imgs.abduzeedo.com/files/articles/Avatar/4154691473_fa5a635992_o.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY","PG-13","79/100", "Sci-Fi")

kung_fu_panda = media.Movie("Kung Fu Panda", "A movie about a kung fu panda",
                     "http://ia.media-imdb.com/images/M/MV5BMTUyNzgxNjg2M15BMl5BanBnXkFtZTgwMTY1NDI1NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=PXi3Mv6KMzY","PG-13","78/100", "Animation")

my_little_bride = media.Movie("My Little Bride", "A movie about a young girl who gets married",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Mylittlebrideposter.jpg/220px-Mylittlebrideposter.jpg",
                     "https://www.youtube.com/watch?v=cxhRA630Xdc","PG-13","72/100", "Romantic Comedy")

deadpool = media.Movie("Deadpool", "A movie about Deadpool",
                     "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=gtTfd6tISfw","R","86/100", "Action")

pokemon = media.Movie("Pokemon: The First Movie", "Pikachu Cries",
                     "http://s7.computerhistory.org/is/image/CHM/500004148-03-01?$re-medium$",
                     "https://www.youtube.com/watch?v=dUaELbAqKLY","PG-13","110/100", "Animation")

udacity = media.Movie("Udacity Front End Nanodegree", "Learn to make websites they said",
                     "https://lh3.googleusercontent.com/-TO82bf9JGDs/AAAAAAAAAAI/AAAAAAAAAAY/ioCmx9KTLWY/s265-c-k-no/photo.jpg",
                     "https://www.youtube.com/watch?v=dQw4w9WgXcQ","R","9/100", "Fantasy")

oceans_eleven = media.Movie("Ocean's Eleven", "They plan a great heist",
                     "http://ia.media-imdb.com/images/M/MV5BMTY0Mzg4MzgwN15BMl5BanBnXkFtZTgwNDk0MzkxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=u7VTkceSsEw","PG-13","94/100", "Sci-Fi")

dark_knight = media.Movie("The Dark Knight", "Na Na Na Na Batman",
                     "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY","PG-13","90/100", "Sci-Fi")

#populate an array to be iterated through in fresh_tomatoes.create_movie_titles_content
movies = [toy_story, avatar, kung_fu_panda, my_little_bride, deadpool, pokemon, udacity, oceans_eleven, dark_knight]
fresh_tomatoes.open_movies_page(movies)
