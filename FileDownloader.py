import requests
'''

'''
def DownloadFile(URL, SaveFileTo):
    r = requests.get(URL, stream=True)
    with open(SaveFileTo, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

#Debug sekcja
URL=input("URL:")
SaveFileTo=input("File:")

DownloadFile(URL, SaveFileTo)
