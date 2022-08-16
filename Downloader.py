import os

a = open("YTB_favorites.txt", "r")
for i in a:
    print(i)
    a = f'youtube-dl.exe -f bestaudio {i}'
    cmd = a
    try :
        os.system(cmd)
    except:
        print("ERROR ")
