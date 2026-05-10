import sys
from PIL import Image

def hide_payload(image_path, payload_path, output_path="output.png"):
    # 1. Open de afbeelding en lees de payload
    img = Image.open(image_path).convert("RGB") # Zorg ervoor dat de afbeelding in RGB is zodat we de kleuren correct kunnen aanpassen
    with open(payload_path, 'r') as f:
        payload = f.read()

    # Voeg een stop-marker toe zodat we weten wanneer we moeten stoppen met lezen
    payload += "#####"
    
    # Zet de payload om in een lijst van bits (0en en 1en)
    bits = ""
    for char in payload:
        bits += format(ord(char), '08b')

    # 2. Pixel data ophalen
    pixels = list(img.getdata())
    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)
        # We passen R, G en B aan van elke pixel
        for i in range(3):
            if bit_index < len(bits):
                # Verander de LSB (Least Significant Bit)
                # bitwise AND met 254 (11111110) zet de laatste bit op 0
                # daarna voegen we de bit (0 of 1) toe
                new_pixel[i] = (new_pixel[i] & 254) | int(bits[bit_index])
                bit_index += 1
        new_pixels.append(tuple(new_pixel))

    # 3. Nieuwe afbeelding opslaan
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)
    print(f"Klaar! Payload verstopt in {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Gebruik: python hide.py <image_pad> <payload_pad>")
    else:
        hide_payload(sys.argv[1], sys.argv[2])
