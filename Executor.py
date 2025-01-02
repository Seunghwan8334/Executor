import os 
import webbrowser 

programs = [    
    r"C:\~.exe",
    r"C:\~.exe",
]

websites = [
    "https://", 
    "https://", 
]

for program in programs:
    try:
        os.startfile(program)
        print("Successfully executed program")
    except Exception as e:
        print("Failed executing program.")

for website in websites:
    try:
        webbrowser.open(website)
        print("Successfully opend website") 
    except Exception as e:
        print("Failed opening website.")

