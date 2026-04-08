with open("text.csv", "r") as file:
    lines = file.readlines()
    
print(f"This file has {len(lines)} rows including header")