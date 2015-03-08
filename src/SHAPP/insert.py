import pymongo
from pymongo import MongoClient
import sys
'''
    name = StringField()
    email = EmailField()
    phone = StringField()
    pic = StringField()
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField()
    Founded_Time = models.DateField()
    kwd = models.CharField(max_length=50)
    Company_URL = StringField()
 '''


def insert(dbName, cName):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client[dbName]
    collection = db[cName]
    data = []
    data.append({
            "nameID": 1,
            "name": "Harlem Biospace",
            "email": "hello@harlembiospace.com",
            "phone": "267-702-3051",
            "pic": "http://www.nycedc.com/sites/default/files/filemanager/hb_horizontal_logo.jpg",
            "lat": "40.813580",
            "lon": "-73.954203",
            "description": "Harlem Biospace (Hb) is a new biotech incubator, the first of its kind in New York City, to offer affordable shared wet-lab space for competitively-selected entrants. <br/> Situated at the heart of three academic campuses (Columbia University, City College of New York, and future Columbia Manhattanville campus), with easy access to other major universities and the vibrancy of New York City via the A, B, C, D and 1 trains, eight bus lines, and only three blocks from the Hudson River bike trail and West Side Highway.<br/> Located in the old Factory District of Harlem, an exciting new development attracting technology companies and start-ups, Hb will be housed in the Sweets Building, a former laboratory for confectionery research located at 423 West 127th Street. <br/> Walking distance to the world-famous Red Rooster, the legendary Apollo Theater, Michelin-recommended Jin Ramen, Maison Harlem, multiple Starbucks, and many high-quality independent restaurants and coffee shops.",
            "Founded_Time": "A new biotech incubator concept, right in Manhattan",
            "kwd": "biotech",
            "Company_URL": "http://harlembiospace.com/"
            })
    data.append({
            "nameID": 2,
            "name": "Soterixmedica",
            "email": "contact@soterixmedical.com",
            "phone": "888-990-8327",
            "pic": "http://soterixmedical.com/static/images/soterixlogo.png",
            "lat": "40.819887",
            "lon": "-73.950483",
            "description": "Researchers and clinicians choose Soterix Medical devices and accessories where the highest standards in performance are required. Soterix Medical products stand-out for their usability, unique features, and precision. Leveraging the most advanced scientific understanding, Soterix Medical technology is the forefront of neuromodulation clinical trials for the treatment of neuropsychiatric disorders and rehabilitation.",
            "Founded_Time": "Soterix Medical is the world leader in non-invasive neuromodulation and brain stimulation technology.",
            "kwd": "neuromodulation",
            "Company_URL": "http://soterixmedical.com/"
            })
    data.append({
            "nameID": 3,
            "name": "Zahn Innovation Center",
            "email": "Contact@zahncenternyc.com",
            "phone": "212-650-7434",
            "pic": "http://www.zahncenternyc.com/wp-content/uploads/2014/07/logggo.png",
            "lat": "40.819887",
            "lon": "-73.950483",
            "description": "The Zahn Innovation Center will spark your inner entrepreneur, the part of you that dares to think big, take risks, engage your creativity and solve problems. And we offer the training, mentorship, prototyping facilities and other resources to enable you to transform your technology or your idea for social change into a sustainable venture. <br/> We are at the heart of innovation and entrepreneurship at The City College of New York. The Zahn Innovation Center will spark your inner entrepreneur, the part of you that dares to think big, take risks, engage your creativity and solve problems. And we offer the training, mentorship, prototyping facilities and other resources to enable you to transform your technology or your idea for social change into a sustainable venture.",
            "Founded_Time": "DREAM  DESIGN  DEVELOP",
            "kwd": "null",
            "Company_URL": "http://www.zahncenternyc.com/"
            })
    data.append({
            "nameID": 4,
            "name": "Harlem Properties",
            "email": "broker@harlemproperties.com",
            "phone": "212-369-1518",
            "pic": "http://harlemproperties.com/wp-content/uploads/2015/02/HarlemProperties_Logo-tiny.png",
            "lat": "40.806429",
            "lon": "-73.955399",
            "description": "Harlem Properties is a real estate brokerage based in Harlem NYC.  We primarily focus on Harlem real estate, and only Harlem real estate.  We are your Harlem real estate experts.  Harlem Properties lists residential and commercial properties for sale, for rent, and for commercial lease all in the Harlem neighborhood of New York City.  We are a boutique real estate firm but we offer the same services as the big corporate firms in town.  Our agency comprises of only the finest Harlem real estate agents and you can expect nothing less than five-star service.",
            "Founded_Time": "Harlem Properties is a real estate brokerage based in Harlem NYC.",
            "kwd": "real estate brokerage",
            "Company_URL": "http://harlemproperties.com/"
            })
    data.append({
            "nameID": 5,
            "name": "Props Photo Booth Company",
            "email": "null",
            "phone": "347-658-6499",
            "pic": "http://static1.squarespace.com/static/52e07edde4b03a175e25140e/t/531664f9e4b025dd261d5df4/1425129006252/?format=750w",
            "lat": "40.810761",
            "lon": "-73.941709",
            "description": "null",
            "Founded_Time": "null",
            "kwd": "photo",
            "Company_URL": "http://www.propsphotoboothco.com/"
            })
    data.append({
            "nameID": 6,
            "name": "TechnoCrafts Inc",
            "email": "info@tcsin.com",
            "phone": "212-594-1881",
            "pic": "http://assets.dice.com/external/images/empLogos/6d2347b6ffc575ab48d7ec6b5547e536.jpg",
            "lat": "40.811825",
            "lon": "-73.950271",
            "description": "Utilize the broad range of Technocrafts Inc services for your IT needs. We are a one-stop partner delivering cost-effective services to help your business overcome technical challenges.",
            "Founded_Time": "Excels at providing business and technology solutions to help our clients improve their business performance.",
            "kwd": "overcome technical challenges",
            "Company_URL": "http://www.tcsin.com/"
            })
    for d in data:
        collection.insert(d)

if __name__=='__main__':
    insert(sys.argv[1], sys.argv[2])










