import string

def analyze_password(password: str) -> None:
    checks = [
        len(password) >= 8,
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
    ]
    score = sum(checks)

    if score <= 2:
        strength = "Weak"
        recommendation = "❌ Use a longer password with symbols and numbers."
    elif score <= 4:
        strength = "Medium"
        recommendation = "⚠️  Add special characters for better security."
    else:
        strength = "Strong"
        recommendation = "✅ Good password!"

    print(f"\n🔐 Password Strength : {strength}")
    print(f"   Score            : {score}/5")
    print(f"   {recommendation}")