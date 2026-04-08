with open("people.csv", "r") as file:
    lines = file.readlines()
    data_lines = lines[1:]

oldest_name = ""
oldest_age = -1  



for line in data_lines:
    clean_line= line.strip()
    parts= clean_line.split(",")
    name= parts[0]
    age = int(parts[1])
    print(f"Name:{name},Age:{age}")

    if age > oldest_age:
        oldest_age = age
        oldest_name = name
print(f"oldest person is {oldest_name} with age {oldest_age}")