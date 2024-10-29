class StudentRating:
    def __init__(self, ratings=None):
        self.ratings = ratings if ratings is not None else []


    def get_ratings(self):
        return self.ratings


    def set_ratings(self, new_ratings):
        self.ratings = new_ratings


    def add_rating(self, rating):
        if 0 <= rating <= 100:
            self.ratings.append(rating)
        else:
            print("Рейтинг має бути в межах 0-100")

    # 1


    def max_rating(self):
        return max(self.ratings) if self.ratings else None


    def min_rating(self):
        return min(self.ratings) if self.ratings else None


    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else None

    # 2


    def above_average_count(self):
        avg = self.average_rating()
        return len([r for r in self.ratings if r > avg])


    def below_average_count(self):
        avg = self.average_rating()
        return len([r for r in self.ratings if r < avg])


    def excellent_count(self):
        return len([r for r in self.ratings if 91 <= r <= 100])

        # 3


    def very_good_count(self):
            return len([r for r in self.ratings if 71 <= r <= 90])


    def good_count(self):
        return len([r for r in self.ratings if 60 <= r <= 70])


    def satisfactory_count(self):
        return len([r for r in self.ratings if 0 <= r <= 59])


    def __str__(self):
        return f"Рейтинги студентів: {', '.join(map(str, self.ratings))}"


ratings = [85, 92, 74, 56, 88, 100, 64, 47, 80, 61]
student_rating = StudentRating(ratings)


print("Максимальний рейтинг:", student_rating.max_rating())
print("Мінімальний рейтинг:", student_rating.min_rating())
print("Середній рейтинг:", student_rating.average_rating())
print("Кількість студентів з рейтингом вище середнього:", student_rating.above_average_count())
print("Кількість студентів з рейтингом нижче середнього:", student_rating.below_average_count())
print("Кількість студентів з рейтингом 'excellent':", student_rating.excellent_count())
print("Кількість студентів з рейтингом 'very good':", student_rating.very_good_count())
print("Кількість студентів з рейтингом 'good':", student_rating.good_count())
print("Кількість студентів з рейтингом 'satisfactory':", student_rating.satisfactory_count())
print(student_rating)
