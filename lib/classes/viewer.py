from .review import Review
class Viewer:
    
    def __init__(self, username):
        self.reviews = []
        self._username = username

    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if 6 <= len(username) <= 16:
            username = self._username
        else:
            raise Exception 

    username = property(get_username, set_username)

    def reviewed_movies(self):
        return list({review.movie for review in self.reviews})

    def reviews(self):
        return self.reviews  
    
    def add_review(self, review):
        self.reviews.append(review)

    def reviewed_movie(self, movie):
        if (self.username and movie) in {review.movie for review in self.reviews}:
            return True
        else:
            return False
        # return movie in self.reviewed_movies()
        
    def rate_movie(self, rating, movie):
        if self.username and movie not in self.reviews:
            return Review(self, rating, movie)
        