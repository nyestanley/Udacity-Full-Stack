import media
import fresh_tomatoes

#Create movie objects
mary_poppins = media.Movie("Mary Poppins",
                           "A woman visits a dysfunctional family in London and employs her unique brand of lifestyle to improve the family's dynamic",
                        "https://upload.wikimedia.org/wikipedia/en/7/78/Marypoppins.jpg",
                           "https://youtu.be/nOfH7uEojKk")

cube = media.Movie("Cube",
                   "A group of people cross industrialized cube-shaped rooms, with some rigged with various traps designed to kill",
                    "https://upload.wikimedia.org/wikipedia/en/0/0c/Cube_The_Movie_Poster_Art.jpg",
                   "https://youtu.be/YAWSkYqqkMA")

mr_limpet = media.Movie("The Incredible Mr. Limpet",
                        "It is about a man named Henry Limpet who turns into a talking fish resembling a tilefish and helps the U.S. Navy locate and destroy Nazi submarines",
                        "https://upload.wikimedia.org/wikipedia/en/2/27/TIML_poster.jpg",
                        "https://youtu.be/xDkt79gV6xQ")

set_it_off = media.Movie("Set It Off",
                         "It follows four close friends in Los Angeles, California, who decide to plan and execute a bank robbery. They decide to do so for different reasons, although all four want better for themselves and their families.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0d/Set_it_off_poster.jpg",
                         "https://youtu.be/Qb5jq3doQa8")

the_temptations = media.Movie("The Temptations", "History of one of Motown's longest-lived acts, The Temptations",
                              "http://www.gstatic.com/tv/thumb/tvbanners/9100172/p9100172_b_v8_ac.jpg",
                              "https://youtu.be/yve3xB219VQ")


cinderella = media.Movie("Cinderella","Re-make of Rodgers & Hammerstein's television movie musical, Cinderella",
                         "http://www.gstatic.com/tv/thumb/dvdboxart/19677/p19677_d_v8_aa.jpg",
                         "https://youtu.be/dd0fuaD-OwE")
    


#Create array to past to web page generator
movies = [set_it_off, the_temptations, cinderella, mary_poppins, cube, mr_limpet]

#Generate movie trailer web page
fresh_tomatoes.open_movies_page(movies)
