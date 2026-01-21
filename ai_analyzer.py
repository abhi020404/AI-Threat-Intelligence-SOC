import json

print("🤖 Running AI Threat Analysis")

# Load raw threat data
with open("raw_attacks.json", "r") as f:
    raw_attacks = json.load(f)

analyzed_attacks = []

for attack in raw_attacks:
    score = attack.get("risk_score", 50)  # default 50 if missing

    # Simple AI-style classification
    if score >= 85:
        severity = "HIGH"
    elif score >= 70:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    analyzed_attacks.append({
        "ip": attack.get("ip"),
        "attack_type": attack.get("attack_type"),
        "risk_score": score,
        "severity": severity,
        "country": attack.get("country", "Unknown")
    })

# Save the analyzed data
with open("analyzed_attacks.json", "w") as f:
    json.dump(analyzed_attacks, f, indent=4)

print("✅ analyzed_attacks.json created successfully")
