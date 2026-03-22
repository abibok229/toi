import random
import string
import json

def main() -> None:
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "James", "Jessica", "Robert", "Linda"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    age = random.randint(18, 90)
    
    email_domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    email = f"{name.lower().replace(' ', '.')}@{random.choice(email_domains)}"
    
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_chars, k=12))
    
    user_data = {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }
    
    with open("user.json", "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)
    
    with open("user.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    
    print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
