import random
from django.core.management.base import BaseCommand
from destination.models import Destination
from review.models import Review

class Command(BaseCommand):
    help = 'Populates the database with initial data for destinations and reviews.'

    def handle(self, *args, **options):
        self.stdout.write("Deleting existing data...")
        Destination.objects.all().delete()
        Review.objects.all().delete()

        self.stdout.write("Creating new data...")

        destinations = [
            {'name': 'Paris', 'country': 'France', 'description': 'The city of love, famous for the Eiffel Tower.'},
            {'name': 'Rome', 'country': 'Italy', 'description': 'A historic city, home to the Colosseum and Roman Forum.'},
            {'name': 'Tokyo', 'country': 'Japan', 'description': 'A bustling metropolis blending tradition and modernity.'},
            {'name': 'Sydney', 'country': 'Australia', 'description': 'Known for its iconic Opera House and Harbour Bridge.'},
            {'name': 'Cairo', 'country': 'Egypt', 'description': 'Home to the Pyramids of Giza and ancient treasures.'},
            {'name': 'New York City', 'country': 'USA', 'description': 'The city that never sleeps, with famous landmarks like Times Square.'},
            {'name': 'Rio de Janeiro', 'country': 'Brazil', 'description': 'Famous for its Carnival, Christ the Redeemer, and beautiful beaches.'},
            {'name': 'London', 'country': 'UK', 'description': 'A vibrant city with a rich history, home to the Tower of London.'},
            {'name': 'Dubai', 'country': 'UAE', 'description': 'A futuristic city known for its skyscrapers and luxury shopping.'},
            {'name': 'Machu Picchu', 'country': 'Peru', 'description': 'An ancient Incan city set high in the Andes Mountains.'},
            {'name': 'Santorini', 'country': 'Greece', 'description': 'A beautiful island with stunning sunsets and white-washed villages.'},
        ]

        created_destinations = []
        for dest_data in destinations:
            destination, created = Destination.objects.get_or_create(
                name=dest_data['name'],
                defaults={
                    'country': dest_data['country'],
                    'description': dest_data['description'],
                }
            )
            if created:
                created_destinations.append(destination)
                self.stdout.write(self.style.SUCCESS(f"Successfully created destination: {destination.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Destination already exists: {destination.name}"))
                created_destinations.append(destination) # Add existing destinations as well to create reviews for them

        authors = ['John Doe', 'Jane Smith', 'Peter Jones', 'Mary Williams', 'David Brown', 'Susan Miller', 'Chris Wilson', 'Patricia Taylor', 'Robert Anderson', 'Jennifer Thomas']
        review_bodies = [
            "An absolutely amazing experience! Highly recommended.",
            "A beautiful place, but a bit too crowded for my taste.",
            "The food was incredible, and the locals were very friendly.",
            "I had a great time, but I wish I had more time to explore.",
            "A must-visit destination. I will definitely be back.",
            "It was a good trip, but it didn't quite live up to my expectations.",
            "The scenery was breathtaking. I've never seen anything like it.",
            "A fantastic place for a family vacation.",
            "I loved every minute of it. A truly unforgettable experience.",
            "The culture and history are fascinating. I learned so much.",
        ]

        for i in range(15):
            destination = random.choice(created_destinations)
            author = random.choice(authors)
            body = random.choice(review_bodies)
            rating = round(random.uniform(3.0, 5.0), 2)

            review, created = Review.objects.get_or_create(
                destination=destination,
                author=author,
                defaults={
                    'body': body,
                    'rating': rating,
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created review for {destination.name} by {author}"))
            else:
                self.stdout.write(self.style.WARNING(f"Review for {destination.name} by {author} already exists."))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
