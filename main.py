import json
import random

print("🚀 Initializing Threat Intelligence System (Offline Mode)")

attack_types = [
    "Ransomware C2 Server",
    "Malware Distribution IP",
    "Brute Force Source",
    "Phishing Server",
    "Botnet Controller"
]

countries = ["CN", "RU", "IR", "KP", "BR", "IN"]

attacks = []

for i in range(50):
    ip = f"10.0.{random.randint(1,255)}.{random.randint(1,255)}"
    attacks.append({
        "ip": ip,
        "attack_type": random.choice(attack_types),
        "risk_score": random.randint(60, 99),
        "country": random.choice(countries),
        "first_seen": "2025-01-15"
    })

with open("raw_attacks.json", "w") as f:
    json.dump(attacks, f, indent=4)

print("✅ raw_attacks.json created successfully (NO INTERNET REQUIRED)")
