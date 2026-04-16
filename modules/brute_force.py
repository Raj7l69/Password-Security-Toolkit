import hashlib
import time
from pathlib import Path

def crack_password(target_hash: str, algorithm: str, path: str = "data/wordlist.txt") -> None:
    wordlist_path = Path(path)

    try:
        words = wordlist_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except FileNotFoundError:
        print("❌ Wordlist not found.")
        return

    print(f"\nStarting Dictionary Attack using: {wordlist_path}\n")

    start_time = time.time()

    for word in words:
        hash_val = hashlib.new(algorithm, word.encode()).hexdigest()

        if hash_val == target_hash:
            elapsed = round(time.time() - start_time, 2)
            print(f"✅ Password Found  : {word}")
            print(f"⏱️  Time Taken      : {elapsed} seconds")
            return

    elapsed = round(time.time() - start_time, 2)
    print(f"❌ Password not found in wordlist.")
    print(f"⏱️  Time Taken      : {elapsed} seconds")