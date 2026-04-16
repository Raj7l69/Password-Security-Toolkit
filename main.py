from modules.dictionary import generate_dictionary
from modules.hash_extractor import generate_hash
from modules.brute_force import crack_password
from modules.analyzer import analyze_password
from modules.report import generate_report

def menu():
    print("\n--- Password Security Toolkit ---")
    print("1. Generate Dictionary")
    print("2. Generate Hash")
    print("3. Run Attack")
    print("4. Analyze Password")
    print("5. Generate Report")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            dob = input("Enter DOB: ").strip()
            username = input("Enter username (Enter to skip): ").strip()
            generate_dictionary(name, dob, username)

        elif choice == "2":
            password = input("Enter password: ").strip()
            generate_hash(password)

        elif choice == "3":
            target_hash = input("Enter hash: ").strip()
            algorithm = input("Enter algorithm (md5/sha1/sha256/sha512): ").strip().lower()

            print("\nSelect Wordlist:")
            print("1. Custom Wordlist")
            print("2. RockYou")

            wl_choice = input("Enter choice: ").strip()

            path = "data/rockyou.txt" if wl_choice == "2" else "data/wordlist.txt"

            crack_password(target_hash, algorithm, path)

        elif choice == "4":
            password = input("Enter password to analyze: ").strip()
            analyze_password(password)

        elif choice == "5":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            strength = input("Enter strength (Weak/Medium/Strong): ").strip()
            time_taken = input("Enter crack time (seconds): ").strip()
            generate_report(username, password, strength, time_taken)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()