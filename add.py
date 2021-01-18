# Page d'ajout de donateurs

from datetime import datetime
from random import randrange, choice
import pymongo
from flask import Flask


class Connexion:

    @classmethod
    def connect(cls):
        cls.user = "Wimblow"
        cls.password = "Leboutdumonde47"
        cls.database = "Dons"
        return pymongo.MongoClient(f"mongodb+srv://{cls.user}:{cls.password}@clusterwim.bhpor.mongodb.net/{cls.database}?retryWrites=true&w=majority")


    @classmethod
    def open_db(cls):
        cls.client = cls.connect()
        cls.don = cls.client.Dons.don


    @classmethod
    def close_db(cls):
        cls.client.close()



fname_li = ['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Olivia', 'Emma',
        'Ava', 'Sophia', 'Isabella', 'Charlotte', 'Amelia', 'Mia', 'Harper', 'Evelyn', 'Abbey', 'Addison', 'Adal', 'Alex',
        'Ali', 'Thomas', 'Camille', 'Pereg', 'Baptiste', 'Jérémy', 'César', 'Paul', 'Pauline', 'Eva', 'Christelle', 'Patricia',
        'Julien', 'Céline', 'Gwendolyne', 'Coralie', 'Stéphanie', 'Brigitte', 'Laura', 'Clémentine', 'Clara', 'Capucine',
        'Morgane', 'Jason', 'Kevin', 'Bob', 'Théo', 'Léopold', 'Reagan', 'Maud', 'Julie', 'David', 'Hermione', 'Cheryl', 'Cassandra',
        'Christopher', 'Christophe', 'Peter', 'Billy', 'Joan', 'Joe', 'John', 'Lyn', 'Dirk', 'Don', 'Ben', 'Jim', 'Christian', 'Assa',
        'Fatou', 'Nelson', 'Talia', 'Bruce', 'Micheline', 'Ana', 'Sean', 'Victoria']
name_li = ['Bokalli', 'Bonneau', 'Chaigneau', 'Cloatre', 'Furiga', 'Guillen', 'Hergoualc\'h', 'Ibanni', 'Karfaoui', 'LeBerre',
        'LeGoff', 'LeJoncour', 'LeMoal', 'Maintier', 'Moulard', 'Petron', 'Rioual', 'Sabia', 'Verpoest', 'Anderson', 'Dupuis', 'Dupont',
        'Fields', 'Morris', 'Landers', 'Flanders', 'Simpson', 'Swift', 'Derulo', 'Derm', 'Xin', 'Salvia', 'Davis', 'Glenn', 'Neill', 'Ameche',
        'Mandella', 'Bogarde', 'Berry', 'MacLaine', 'Neil', 'Owen', 'Spector', 'Dalton', 'Fournirer', 'Louis', 'Dennis', 'Fitzalan', 'Jenner',
        'Elbe', 'Smith', 'Todd', 'Bisset', 'Cruise', 'Glaser', 'Charles', 'Fontaine', 'Barrymore', 'Laden', 'Traoré', 'Polina']


Connexion.open_db()
for i in range(20):
    name = choice(name_li)
    fname = choice(fname_li)
    adresse = "123 rue du parc"
    mail = f'{name.lower()}.{fname.lower()}@gmail.com'
    don = randrange(500)
    Connexion.don.insert_one({"name":name, "fname":fname, "adresse":adresse, "mail":mail, "don":int(don)} )
Connexion.close_db()
