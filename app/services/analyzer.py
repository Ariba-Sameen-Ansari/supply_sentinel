def analyze_package(pkg_name: str) -> dict:
    # Simulated "LLM-style" response
    if "crypto" in pkg_name.lower() or "obfus" in pkg_name.lower():
        return {
            "package": pkg_name,
            "risk": "High",
            "reason": "Contains keywords like 'crypto' or 'obfuscation' often used in malicious packages.",
            "mitre_technique": "T1027 – Obfuscated Files or Information"
        }
    else:
        return {
            "package": pkg_name,
            "risk": "Low",
            "reason": "No suspicious indicators found.",
            "mitre_technique": None
        }
