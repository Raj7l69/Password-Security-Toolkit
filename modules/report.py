from pathlib import Path
from datetime import datetime

def generate_report(username: str, password: str, strength: str, time_taken: float) -> None:
    risk = "HIGH" if strength == "Weak" else "MEDIUM" if strength == "Medium" else "LOW"

    report = f"""
================= PASSWORD SECURITY AUDIT REPORT =================

User Information
----------------
Username        : {username}
Password Tested : {password}

Analysis Result
---------------
Password Strength : {strength}
Risk Level        : {risk}
Time to Crack     : {time_taken} seconds

Security Insights
-----------------
- Weak passwords are highly vulnerable to dictionary and brute-force attacks.
- Attack simulation performed in a controlled environment.
- Results indicate the importance of strong password policies.

Recommendations
---------------
- Use at least 12–16 characters
- Include uppercase, lowercase, numbers, and symbols
- Avoid dictionary words and personal information
- Use unique passwords for different accounts

Report Metadata
---------------
Generated On : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Tool         : Password Security Toolkit

===============================================================
"""

    output_path = Path("output/report.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path = Path(f"output/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    output_path.write_text(report)

    print("\n✅ Report generated successfully!")
    print(f"   Saved in : {output_path}")
