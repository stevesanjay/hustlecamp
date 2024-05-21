import csv
import random
from faker import Faker
import pycountry

# Initialize Faker
faker = Faker()

# Dictionary mapping countries to their regions
def get_region(country_name):
    try:
        country = pycountry.countries.get(name=country_name)
        return country.subdivision.name
    except AttributeError:
        return "Unknown"

# Function to generate random data
def generate_data():
    job_titles = ["Software Engineer", "Data Scientist", "Web Developer", "Systems Analyst", "Network Administrator"]
    locations = ["Texas", "Ontario"]
    technical_skills = ["Node.js", "Python", "Java", "RESTful API", "SQL", "HTML","CSS", "JavaScript","React", "Vue.js","Docker", "Kubernetes","CI/CD"," Linux"," AWS"

]
    languages = ["English", "Spanish", "French", "German", "Mandarin"]

    name = faker.name()
    job_title = random.choice(job_titles)
    country = random.choice(["USA", "Canada"])
    location = random.choice(locations) if country == "USA" else get_region(country)
    years_of_experience = random.randint(1, 20)
    num_technical_skills = random.randint(1, 5)
    num_languages = random.randint(1, 4)

    technical_skill = ", ".join(random.sample(technical_skills, num_technical_skills))
    language = ", ".join(random.sample(languages, num_languages))

    return {
        "Name": name,
        "Job Title": job_title,
        "Location": location,
        "Years of Experience": years_of_experience,
        "Technical Skill": technical_skill,
        "Language known": language
    }

# Number of rows to generate
num_rows = 1000000

# File name to save
file_name = "freelancers-na-10m-20240513.csv"

# Column names
fieldnames = ["Name", "Job Title", "Location", "Years of Experience", "Technical Skill", "Language known"]

# Writing data to CSV file
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(num_rows):
        writer.writerow(generate_data())

print(f"CSV file '{file_name}' created successfully with {num_rows} rows!")
