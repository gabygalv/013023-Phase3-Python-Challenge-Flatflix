
class Movie:
    
    def __init__(self, title):
        self.reviews = []
        self.title = title

    def get_name(self):
        return self.title
    
    def set_name(self, title):
        if type(title) == str and len(title) > 0:
            title = self.title
        else:
            raise Exception 

    name = property(get_name, set_name)

    def average_rating(self):
        total = sum(review.rating for review in self.reviews)
        return total / len(self.reviews)

    @classmethod
    def highest_rated(cls):
        avg_ratings = list(cls.average_rating())
        avg_ratings.sort()
        return avg_ratings[0]

    def reviews(self):
        return self.reviews  
    
    def add_review(self, review):
        self.reviews.append(review)

    def reviewers(self):
        return list({review.viewer for review in self.reviews})
   