from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
import random
from accounts.models import User,Profile

from blog.models import Post,Category


category_list = [
    'Python',
    'Django',
    'JavaScript',
    'Vuejs',
    'React',
    'Angular'
]

class Command(BaseCommand):

    help = "Inserting Dummy Data to Data-Base"
    

    def __init__(self):

        self.faker = Faker()


    def handle(self, *args, **options):
        

        user = User.objects.create_user(email=self.faker.email(),password="123qwe!@#")

        profile = Profile.objects.get(user=user)
        profile.first_name = self.faker.first_name()
        profile.last_name = self.faker.last_name()
        profile.description = self.faker.paragraph(nb_sentences = 10)
        profile.save()
        
        for name in category_list:
            Category.objects.get_or_create(name=name)
            
        for _ in range(20000):
            Post.objects.create(
                title=self.faker.paragraph(nb_sentences = 2),
                content=self.faker.text(max_nb_chars=500),
                author=profile,
                status=random.choice([True,False]),
                category=Category.objects.get(name=random.choice(category_list)),
                created_date=datetime.now(),
                published_date=datetime.now()            
            )