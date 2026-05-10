import subprocess 

def open_calculator():
    try:
        # Opens the Windows Calculator app
        subprocess.Popen('calc.exe')
    except Exception as e:
        print(f"Failed to open calculator: {e}")

if __name__ == "__main__":
    open_calculator()
