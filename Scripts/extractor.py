import sys
from PIL import Image

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gebruik: python extractor.py <stego_image_pad>")
    else:
        resultaat = extract_payload(sys.argv[1])
        # Schrijf de gevonden payload naar een nieuw bestand
        with open("extracted_payload.py", "w") as f:
            f.write(resultaat)
        
        print("Klaar! De verstopte payload is opgeslagen in 'extracted_payload.py'")
        print("\nInhoud van de payload:")
        print("-" * 20)
        print(resultaat)
        print("-" * 20)
