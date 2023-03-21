



class Movie: #notice class has its own docstring!
    """Movie class holds title of the movie, the cast, the rating, and year of release. 

    It prints in a nicely formatted string, and has a method to check if an actor is in the cast.

    Attributes:
        name (str): the title of the movie
        cast (list): a list of actors in the movie, it will perform a shallow copy of the original list.
        rating (int): the rating of the movie
        year (int): the year the movie was released
    """
    def __init__(self, name: str, cast: list, rating: int, year: int):
        """Constructor of the movie object. It will perform a shallow copy of the cast list.

        Args:
            name (str): the title of the movie
            cast (list): a list of actors in the movie
            rating (int): the rating of the movie
            year (int): the year the movie was released
        """
        self.__name = name
        self.__cast = cast.copy() 
        self.__rating = rating
        self.__year = year

    @property
    def name(self) -> str:
        """Returns the name of the movie"""
        return self.__name

    @property
    def cast(self) -> list:
        """Returns the cast of the movie"""
        return self.__cast

    @property
    def rating(self) -> int:
        """Returns the rating of the movie"""
        return self.__rating
    
    @rating.setter
    def rating(self, rating: int) -> None:
        """Sets the rating of the movie,

        Args:
            rating (int): the rating of the movie
        
        Raises:
            ValueError: if the rating is negative
        """
        if rating < 0:
            raise ValueError("Rating cannot be negative")
        self.__rating = rating

    @property
    def year(self) -> int:
        """Returns the year of the movie"""
        return self.__year
    

    def has_actor(self, actor: str) -> str:
        """
        Checks if the actor is in the cast of the movie.
        Assumes lowercase, and will match on partial names
        so keanu will return Keanu Reeves, kea will return Keanu Reeves.
        Only returns the first instance. 
        If no match is found, returns an empty string.

        
        Args:
            actor (str): the name of the actor to check
        """
        for actors in self.__cast:
            if actor.lower() in actors.lower():
               return actors  # why did we do it this way, instead of just return actor in self.__cast
        return ''

    def __convert_rating(self, val: int, min_s : int = 0, max_s: int = 5) -> str:
        """Private function to convert the rating to stars.

        Args:
            val (int): the rating value
            min_s (int, optional): minimum stars. Defaults to 0.
            max_s (int, optional): maximum stars. Defaults to 5.

        Returns:
            str: stars between min_s and max_s
        """
        val = int(val) 
        if val < min_s:
            val = min_s
        if val > max_s:
            val = max_s
        return "*" * val

    def __str__(self) -> str:
        """Returns a nicely formatted string of the movie. of the format Stars MovieName"""
        return f"{self.__convert_rating(self.rating):<{7}}{self.name}"
    
    def __eq__(self, o: object) -> bool:
        """Overrides the default implementation, checking to make sure the movie is the same title and year, then the are equal."""
        if isinstance(o, Movie): ## check if the object is a movie
            return self.name == o.name and self.year == o.year
        return False
    
    def __hash__(self) -> int:
        """Overrides the default implementation, hashing the movie name and year. 
        This would allow us to store the movie in a set, as it provides properties to make sure it is unique"""
        return hash((self.name, self.year))


def sample_run():
    """Sample run of the program"""
    movie = Movie("The Matrix", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"], 5, 1999)
    print(movie)
    print(movie.has_actor("keanu"))
    matrix2 = Movie("The Matrix Reloaded", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"], 3, 2003)
    print(matrix2)
    matrix3 = Movie("The Matrix Revolutions", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"], 4, 2003)
    print(matrix3)
    princess_bride = Movie("The Princess Bride", ["Cary Elwes", "Mandy Patinkin", "Robin Wright"], 100, 1987)
    print(princess_bride)

    ### if the above function is ran in an interactive python terminal, the following will be the output:
#     *****  The Matrix
#     Keanu Reeves
#     ***    The Matrix Reloaded
#     ****   The Matrix Revolutions
#     *****  The Princess Bride