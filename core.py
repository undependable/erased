import requests
import webbrowser

print("")
print("Will notify and open erased project when the drop is live...")
print("")

while True:
    resp = (requests.get("https://erasedproject.com/", allow_redirects=False))
    
    if resp.status_code == 302:
        pass

    if resp.status_code == 200:
        print(f"[+] Collection officially dropped!")
        print("[!] Opening website for you...")
        webbrowser.open("https://erasedproject.com/")
        exit()
        
