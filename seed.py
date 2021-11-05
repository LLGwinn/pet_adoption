""" Seed data for pet_adoption db """

from models import Pet, db 
from app import app

# Create table
db.drop_all()
db.create_all()

# Clear table
Pet.query.delete()

# Create users
pet1 = Pet(name = 'Snuggles',
            species = 'cat',
            photo_url = 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y2F0fGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 1,
            notes = 'sweet little kitten ready for a forever family',
            available = True)
pet2 = Pet(name = 'Spaz',
            species = 'cat',
            photo_url = 'https://images.unsplash.com/photo-1494256997604-768d1f608cac?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNhdHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 2,
            notes = 'loves to play',
            available = True)
pet3 = Pet(name = 'Ridley',
            species = 'dog',
            photo_url = 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8ZG9nfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 6,
            notes = 'mature beach lover',
            available = True)
pet4 = Pet(name = 'Gomer',
            species = 'dog',
            photo_url = 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8ZG9nfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 3,
            notes = 'playful pup',
            available = True)
pet5 = Pet(name = 'Spike',
            species = 'porcupine',
            photo_url = 'https://images.unsplash.com/photo-1618527324482-d84be63d8077?ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8cG9yY3VwaW5lfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
            age = 12,
            notes = 'coffee companion',
            available = True)
pet6 = Pet(name = 'Shadow',
            species = 'dog',
            photo_url = '',
            age = 12,
            notes = 'coffee companion',
            available = False)


# Add users to db
db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])
db.session.commit()