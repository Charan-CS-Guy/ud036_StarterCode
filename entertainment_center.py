''' This module creates data for different movies using media module's Movie class'''
import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "Toy Story is about the 'secret life of toys' when people are not around.", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg")

iron_man = media.Movie("Iron Man", "Iron Man is a 2008 American superhero film based on the Marvel Comics character of the same", "https://www.youtube.com/watch?v=8hYlB38asDY", "https://www.flickeringmyth.com/wp-content/uploads/2017/03/Iron-Man-2008-Movie-Poster.jpg")

the_imitation_game = media.Movie("The Imitation Game", "Film is loosely based on the biography of Alan Turing", "https://www.youtube.com/watch?v=S5CjKEFb-sM", "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg")

pursuit_of_happyness = media.Movie("The Pursuit of Happyness", "The film is a drama of entrepreneur Chris Gardner's nearly one-year struggle being homeless", "https://www.youtube.com/watch?v=bTJ-0zVAsEA", "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg")

dark_knight = media.Movie("The Dark Knight", " Bruce Wayne/Batman (Bale), James Gordon (Oldman) and Harvey Dent (Eckhart) form an alliance to dismantle organized crime in Gotham City", "https://www.youtube.com/watch?v=EXeTwQWrcwY", "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")

artificial_intelligence = media.Movie("Artificial Intelligence", " The film is based on a screen story by Ian Watson and the 1969 short story 'Super-Toys Last All Summer Long' by Brian Aldiss.", "https://www.youtube.com/watch?v=_19pRsZRiz4", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/AI_Poster.jpg/220px-AI_Poster.jpg")

#create a list of all the movies/objects to provide as an input to open_movies function
movies = [toy_story, iron_man, the_imitation_game, pursuit_of_happyness, dark_knight, artificial_intelligence]

fresh_tomatoes.open_movies_page(movies)
