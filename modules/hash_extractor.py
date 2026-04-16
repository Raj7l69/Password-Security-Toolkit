import hashlib
from pathlib import Path

ALGORITHMS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha512"
}

def generate_hash(password: str) -> None:
    print("\nSelect Hash Algorithm:")
    for key, algo in ALGORITHMS.items():
        print(f"  {key}. {algo.upper()}")

    choice = input("\nEnter choice (1-4): ").strip()

    if choice not in ALGORITHMS:
        print("❌ Invalid choice. Please select 1-4.")
        return

    algo = ALGORITHMS[choice]
    hash_value = hashlib.new(algo, password.encode()).hexdigest()

    output_dir = Path("data")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "hashes.txt"
    with output_file.open("a") as f:
        f.write(f"Algorithm : {algo.upper()}\n")
        f.write(f"Hash      : {hash_value}\n")
        f.write("-" * 50 + "\n")

    print(f"\n✅ Hash generated successfully!")
    print(f"   Algorithm : {algo.upper()}")
    print(f"   Hash      : {hash_value}")
    print(f"   Saved to  : {output_file}")


if __name__ == "__main__":
    pwd = input("Enter password to hash: ").strip()
    if pwd:
        generate_hash(pwd)
    else:
        print("❌ Password cannot be empty.")