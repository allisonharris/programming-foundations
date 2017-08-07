import fresh_tomatoes
import media

slums = media.Movie("Slums of Beverly Hills",
                        "The niece of a divorced man helps raise his adolescent daughter and two sons on the outskirts of Beverly Hills.",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Slums_of_Beverly_Hills_film.jpg",
                        "https://www.youtube.com/watch?v=dADNBoN7idQ")

#print slums.storyline
#slums.show_trailer()

the_circle = media.Movie("The Circle",
                        "Mae Holland seizes the opportunity of a lifetime when she lands a job with the world's most powerful technology and social media company",
                        "http://www.impawards.com/2017/posters/circle_xlg.jpg",
                        "https://www.youtube.com/watch?v=ZkzpcfY9JAo")

me_you = media.Movie("Me You and Everyone We Know",
                        "Single dad Richard meets Christine, a starving artist who moonlights as a cabbie. They awkwardly attempt to start a romance.",
                        "http://www.gstatic.com/tv/thumb/dvdboxart/88898/p88898_d_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=r-HIuog7ACc&t")

royal = media.Movie("The Royal Tenenbaums",
                        "Royal Tenenbaum and his wife Etheline had three children and then they separated. All three children are extraordinary --- all geniuses.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcRquKeojQNexv_1qza8leUdU-G-IHwq6Vb0M6j2A3_oiHkRfrqa",
                        "https://www.youtube.com/watch?v=W5AU78dqBgE")

amelie = media.Movie("Amelie",
                        "Amelie is a fanciful comedy about a young woman who discretely orchestrates the lives of the people around her, creating a world exclusively of her own making.",
                        "http://www.gstatic.com/tv/thumb/dvdboxart/28319/p28319_d_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=HUECWi5pX7o")

whose_streets = media.Movie("Whose Streets",
                        "An account of the Ferguson uprising as told by the people who lived it.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcT_xY8-CWqgtYiJquEzNbIxkrRcb6SFdAp-_VsVBBVy-U8s4QdL",
                        "https://www.youtube.com/watch?v=-AS1-QmQ93Y")

movies = [slums, the_circle, me_you, royal, amelie, whose_streets]
fresh_tomatoes.open_movies_page(movies)

