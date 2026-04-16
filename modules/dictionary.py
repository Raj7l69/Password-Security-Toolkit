from pathlib import Path

def generate_dictionary(name: str, dob: str, username: str = "") -> None:
    words = [
        name,
        name + dob,
        name + "123",
        name.capitalize() + dob,
        name + "@123",
        name.replace('a', '@'),
        name.replace('s', '$'),
    ]

    if username:
        words += [
            username,
            username + dob,
            username + "123",
            username.capitalize() + dob,
            username + "@123",
            username.replace('a', '@'),
            username.replace('s', '$'),
        ]

    output_path = Path("data/wordlist.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(words) + "\n")

    print(f"\n✅ Wordlist generated successfully!")
    print(f"   Total words : {len(words)}")
    print(f"   Saved in    : {output_path}")