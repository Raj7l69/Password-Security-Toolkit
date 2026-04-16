# 🔐 Password Security Toolkit

A Python-based cybersecurity toolkit designed to simulate password cracking techniques and analyze password strength in a controlled environment.

---

## 🚀 Features

- Custom Dictionary Generator (Name, DOB, Username based)
- Password Hash Generator (MD5, SHA1, SHA256, SHA512)
- Dictionary Attack Simulation
- Support for Custom Wordlist & RockYou Wordlist
- Password Strength Analyzer
- Security Audit Report Generator

---

## 📂 Project Structure

project/
 ├── main.py
 ├── modules/
 │    ├── dictionary.py
 │    ├── hash_extractor.py
 │    ├── brute_force.py
 │    ├── analyzer.py
 │    └── report.py
 ├── data/
 │    ├── wordlist.txt
 │    ├── hashes.txt
 ├── output/
 │    └── report.txt
 └── docs/
      └── diagrams

---

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Raj7l69/Password-Security-Toolkit.git
cd Password-Security-Toolkit
```
---

## 📥 RockYou Wordlist Setup

### Kali Linux

RockYou is pre-installed in Kali Linux.

```bash
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz  
cp /usr/share/wordlists/rockyou.txt data/  
```
---

### Other Operating Systems

Download RockYou from:

```
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt  
```

After downloading, move it to:

data/rockyou.txt  

---

## ▶️ How to Run

```
python3 main.py  
```

---

## 🧪 Usage Flow

1. Generate Dictionary (custom wordlist)  
2. Generate Hash of password  
3. Run Attack (choose Custom or RockYou)  
4. Analyze Password Strength  
5. Generate Security Report  

---

## ⚠️ Important Notes

- RockYou wordlist (~130MB) is not included in this repository  
- Add it manually as shown above  
- The tool is designed for simulation only  

---

## 🛡️ Ethical Use

This project is strictly for educational and cybersecurity learning purposes.  
No real systems or unauthorized access are involved.  

---

## 📊 Output

- Wordlist file (data/wordlist.txt)  
- Hash file (data/hashes.txt)  
- Attack simulation results  
- Password strength analysis  
- Final report (output/report.txt)  

---

## 📌 Future Improvements

- GPU-based cracking simulation  
- Advanced attack techniques  
- Real-time monitoring system  
- GUI interface  

---

## 📚 References

- Kali Linux Documentation  
- Python Official Documentation  
- Cybersecurity Best Practices  

---

## 👤 Author

Rajendra Singh