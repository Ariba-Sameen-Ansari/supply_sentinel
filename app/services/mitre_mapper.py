def get_mitre_description(technique_id: str) -> str:
    mitre_map = {
        "T1027": "Obfuscated Files or Information – Common in software supply chain attacks."
    }
    return mitre_map.get(technique_id.split(" ")[0], "No mapping available")
