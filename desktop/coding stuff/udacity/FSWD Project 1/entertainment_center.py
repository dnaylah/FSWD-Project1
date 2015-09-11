import media
import fresh_tomatoes

jump_street = media.Movie("21 Jump Street",
                          "2 former enemies become friends in this comedy",
                          "http://popculturegalaxy.com/wp-content/uploads/2013/04/21-jump-street-2.jpg",  # noqa
                          "https://www.youtube.com/watch?v=RLoKtb4c4W0",
                          "(2012)")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://fanaru.com/avatar/image/6676-avatar-avatar-movie-poster.jpg",  # noqa
                     "https://www.youtube.com/watch?t=1&v=cRdxXPV9GNQ",
                     "(2009)")

sideways = media.Movie("Sideways",
                       "2 friends who find themselves \
                            during a bachelor party trip",
                       "http://static.rogerebert.com/uploads/movie/movie_poster/sideways-2004/large_tojQbn3H4UcM8lkuns1E7CnLv8D.jpg",  # noqa
                       "https://www.youtube.com/watch?v=YS9ocP6FNvM",
                       "(2004)")


super_troopers = media.Movie("Super Troopers",
                             "Cops gone wild",
                             "http://www.caddycat.com/Ebay/Super_Troopers-1.jpg",  # noqa
                             "https://www.youtube.com/watch?v=2-9D2qUHN-E",
                             "(2002)")

tomorrow_never_dies = media.Movie("Tomorrow Never Dies",
                                  "James Bond film",
                                  "http://1.bp.blogspot.com/-118OGkSTyHE/UNC6C-FPZ5I/AAAAAAAAGMk/CJbMcc1d6mo/s1600/Tomorrow-Never-Dies.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=gYtz5sw98Bc",  # noqa
                                  "(1997)")

pineapple_express = media.Movie("Pineapple Express",
                                "2 stoners get in trouble with drug dealers",
                                "http://theblemish.com/images/2008/08/pineapple_express-500x743.jpg",  # noqa
                                "https://www.youtube.com/watch?v=wWbEoEJsxYw",
                                "(2008)")

# Append each movie to the movies list
movies = [jump_street, avatar, sideways, super_troopers,
          tomorrow_never_dies, pineapple_express]


# Need to run this to update the html page
fresh_tomatoes.open_movies_page(movies)
