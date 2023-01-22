import os

def update_password(website, kullanici_adi, sifre):
    lines = []
    with open("password.txt", "r") as f:
        for line in f:
            if website in line:
                line = website + " : " + kullanici_adi + " : " + sifre + "\n"
            lines.append(line)
    with open("password.txt", "w") as f:
        f.writelines(lines)

def delete_password(website):
    lines = []
    with open("password.txt", "r") as f:
        for line in f:
            if website not in line:
                lines.append(line)
    with open("password.txt", "w") as f:
        f.writelines(lines)

def save_password(website,kullanici_adi,sifre):
    with open("password.txt", "a") as f:
        f.write(website + " : " + kullanici_adi + " : " + sifre + "\n")

def get_passwords():
    with open("password.txt", "r") as f:
        return f.read()

def main():
    while True:
        secim = input("1. Enter URL, username and password.\n2. Show saved information.\n3. Update saved information.\n4. Delete saved information.\n5. Exit\nMake your choice-->  ")
        if secim == "1":
            website = input("URL: ")
            kullanici_adi = input("Username: ")
            sifre = input("Password: ")
            save_password(website,kullanici_adi,sifre)
            print("The information has been saved.")
        elif secim == "2":
            print("Saved Information: ")
            print(get_passwords())
        elif secim == "3":
            website = input("Enter a URL: ")
            kullanici_adi = input("Enter a new username: ")
            sifre = input("Enter a new password: ")
            update_password(website, kullanici_adi, sifre)
            print("Information has been updated. ")
        elif secim == "4":
            website = input("Enter a URL: ")
            delete_password(website)
            print("Information has been deleted..")
        elif secim == "5":
            print("Exiting..")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
