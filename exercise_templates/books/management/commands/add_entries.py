import random
from datetime import date

from django.core.management.base import BaseCommand

from books.models import Book
from reviews.models import Review


def get_random_name():
    first_names = ["John", "Jane", "Peter", "Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Harry",
                   "Isabella", "Jack", "Kate", "Liam", "Mary", "Nora", "Oliver", "Penelope", "Quinn", "Rachel", "Sam",
                   "Tina", "Ursula", "Victor", "Wendy", "Xander", "Yvonne", "Zane"]
    last_names = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
                  "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
                  "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
                  "Wright"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


class Command(BaseCommand):
    help = 'Adds new books and reviews to the database'

    def handle(self, *args, **options):
        # Update existing reviews with realistic names
        reviews_to_update = Review.objects.filter(author__startswith="Reviewer")
        for review in reviews_to_update:
            review.author = get_random_name()
            review.save()
            self.stdout.write(self.style.SUCCESS(f"Updated review author to '{review.author}'."))

        # Add new reviews to original books
        original_book_titles = [
            "Children of Time",
            "The Quantum Thief",
            "Dune",
            "A Game of Thrones",
            "Sapiens: A Brief History of Humankind",
            "The Hound of the Baskervilles"
        ]

        for book_title in original_book_titles:
            try:
                book = Book.objects.get(title=book_title)
                num_reviews = random.randint(8, 12)
                for i in range(num_reviews):
                    author_name = get_random_name()
                    if not Review.objects.filter(book=book, author=author_name).exists():
                        Review.objects.create(
                            author=author_name,
                            body=f"This is a fantastic new review for {book.title}. I really enjoyed it.",
                            rating=round(random.uniform(3.0, 5.0), 2),
                            book=book,
                            is_spoiler=random.choice([True, False])
                        )
                        self.stdout.write(
                            self.style.SUCCESS(f"Review by '{author_name}' for '{book.title}' created."))
                    else:
                        self.stdout.write(
                            self.style.WARNING(f"Review by '{author_name}' for '{book.title}' already exists."))
            except Book.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Book with title '{book_title}' not found."))

        self.stdout.write(self.style.SUCCESS("Review update and adding process finished."))