import os


def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def Moves(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


if __name__ == "__main__":
    os.system('clear')
    os.system('sleep 4')
    os.system('figlet -ctf slant "Cleans"')
    print('Created by Rohit Ahirwal')
    os.system('sleep 3')
    print('Subscribe my youtube channel Code like Devil')
    
    os.system('sleep 4')
    files = os.listdir()
    files.remove('main.py')

    CreateIfNotExist('Images')
    CreateIfNotExist('Docs')
    CreateIfNotExist('Videos')
    CreateIfNotExist('Musics')
    CreateIfNotExist('Zips')
    CreateIfNotExist('Programings')
    CreateIfNotExist('Others')

    print('Fetching files')
    os.system('sleep 3')
    imgExts = ['.jpg', '.png', '.jpeg', '.ico', '.svg']
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    print('')
    print('Images succesfully fetched')

    os.system('sleep 3')
    docExts = ['.doc', '.docx', '.pdf', '.txt']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    print('')
    print('Documents successfully fetched')

    os.system('sleep 3')
    videoExts = ['.mp4']
    videos = [file for file in files if os.path.splitext(file)[1].lower() in videoExts]
    print('')
    print('Videos successfully fetched')

    os.system('sleep 3')
    musicExts = ['.mp3']
    musics = [file for file in files if os.path.splitext(file)[1].lower() in musicExts]
    print('')
    print('Musics successfully fetched')

    os.system('sleep 3')
    zipExts = ['.zip', '.7z', '.rar']
    zips = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]
    print('')
    print('Zips successfully fetched')
    
    os.system('sleep 3')
    programingExts = ['.html', '.css', '.js', '.java','.c', '.c++', '.cs', '.py', '.sh', '.php', '.xml']
    programings = [file for file in files if os.path.splitext(file)[1].lower() in programingExts]
    print('')
    print('Programings succssfully fetched')

    os.system('sleep 3')
    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in videoExts) and (ext not in musicExts) and (ext not in zipExts) and (ext not in programingExts):
            others.append(file)
    print('')
    print('Others succesfully fetched')
    os.system('sleep 3')
    
    print('')
    print('All files fetched')
    
    os.system('sleep 5')
    Moves('Images', images)
    Moves('Docs', docs)
    Moves('Videos', videos)
    Moves('Musics', musics)
    Moves('Zips', zips)
    Moves('Programings', programings)
    Moves('Others', others)
    
    os.system('sleep 5')
    print('')
    print(len(images), ' Images succesfully cleaned')
    print('')
    print(len(docs), 'Document succesfully cleaned')
    print('')
    print(len(videos), 'Videos succesfully cleaned')
    print('')
    print(len(musics), 'Musics succesfully cleaned')
    print('')
    print(len(zips), 'Zips succesfully cleaned')
    print('')
    print(len(programings), 'Programings succesfully cleaned')
    print('')
    print(len(others), 'Others succesfully cleaned')
