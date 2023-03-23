class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        viewer.add_review(self)
        movie.add_review(self)

    # rating property goes here!
    def get_rating(self):
        return self.rating
    def set_rating(self, rating):
        if 1 <= rating <= 5:
            rating = self.rating
    rating = property(get_rating, set_rating)


    # viewer property goes here!
    @property
    def viewer(self):
        return self.viewer

    # movie property goes here!
    @property
    def movie(self):
        return self.movie
