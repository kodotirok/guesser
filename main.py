import requests

def get_gender(payload):
    gender_URL = "https://api.genderize.io/"
    gender_r = requests.get(gender_URL, params=payload)
    gender = gender_r.json()["gender"]
    p_gender = gender_r.json()["probability"]

    return gender, p_gender

def get_age(payload):
    age_URL = "https://api.agify.io/"
    age_r = requests.get(age_URL, params=payload)
    age = age_r.json()["age"]

    return age

def get_nat(payload):
    nat_URL = "https://api.nationalize.io/"
    nat_r = requests.get(nat_URL, params=payload)

    nat_ctry = nat_r.json()["country"]

    nat_list = []
    for i in nat_ctry:
        nat_list.append({"country" : i["country_id"], "probability" : i["probability"]})

    return nat_list

print("I will guess the gender, age and nationality of a person based on their name.")

first_name = input("First name: ")

payload = {"name" : first_name}

genderstats = get_gender(payload)
agestat = get_age(payload)
natstats = get_nat(payload)

print(f"Gender: {genderstats[0]} with the probability of: {genderstats[1]}")
print(f"Age (probably): {agestat}")
print(f"Nationality: ")
for i in natstats:
    print(f"\tFrom {i["country"]} with the probability of: {i["probability"]:.3f}")