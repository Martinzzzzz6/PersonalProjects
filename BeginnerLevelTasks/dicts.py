programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          123: "A number",
                          "True": "A boolean value that represents the truth.",
                          "False": "A boolean value that represents the false.",
                          2523452 : "A big number",}

# print(programming_dictionary["True"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."

# for key in programming_dictionary:
#     print(f"{key} : {programming_dictionary[key]}")


student_scores = { "Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


#Nested dictionaries in a list
capitals = {"France": "Paris",
            "Germany": "Berlin",
            "Singpoare": "Singapore"}

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log_dict = {
    "France" : {"cities_visited" : ["Paris, Lille, Dijon"], "total_visits" : 12},
    "Germany" : {"cities_visited" : ["Berlin, Hamburg, Stuttgart"], "total_visits" : 5},    
}

travel_log_dict = [
   {
       "country" : "France", 
       "cities_visited" : ["Paris, Lille, Dijon"], 
       "total_visits" : 12
       },
   {
       "country" : "Germany", 
       "cities_visited" : ["Berlin, Hamburg, Stuttgart"], 
       "total_visits" : 5
       },    
]

for key in travel_log_dict:
    print(f"{key['country']} : {key['cities_visited']} : {key['total_visits']}")

for key in travel_log_dict:
    print(f"{key}")

def add_new_country(country, cities_visited, total_visits):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = total_visits
    travel_log_dict.append(new_country)
    