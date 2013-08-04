import stagger
import os
import shutil
import random
from stagger.id3 import *
def copySongs(source,target):
    windows = True
    win = "\\"
    lin = "/"
    os.chdir(source)
    a = [ name for name in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), name)) ]
    for x in a:
        os.chdir(source)
        os.chdir(x)
        b = [ name for name in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), name)) ]
        for y in b:
            os.chdir(source)
            os.chdir(x)
            oldfilename = os.getcwd()+"\\"+y
            try:
                tag = stagger.read_tag(y)
                title = removeSymbols(tag.title.strip())
                artist = removeSymbols(tag.artist.strip())
                trackNr = tag.track
                album = removeSymbols(tag.album.strip())
                filename = str(trackNr)+" - "+title+".mp3"
            except:
                title = y
                artist = "NO ID3 TAG"
                trackNr = random.randint(0, 20)
                album = "NoAlbum"
                filename = str(trackNr)+" - "+title
            if len(album) > 0:
                if windows:
                    fullpath = target+win+artist+win+album+win
                    while fullpath.count('/') > 0:
                        fullpath = fullpath.replace('/', '')
                    while fullpath.count('|') > 0:
                        fullpath = fullpath.replace('|', '')
                    while fullpath.count('*') > 0:
                        fullpath = fullpath.replace('*', '')
                else:
                    fullpath = target+lin+artist+lin+album+lin
            else:
                if windows:
                    fullpath = target+win+artist+win+"NoAlbum"+win
                    while fullpath.count('/') > 0:
                        fullpath = fullpath.replace('/', '')
                    while fullpath.count('|') > 0:
                        fullpath = fullpath.replace('|', '')
                    while fullpath.count('*') > 0:
                        fullpath = fullpath.replace('*', '')
                else:
                    fullpath = target+lin+artist+lin+"NoAlbum"+lin
            fullfilepath = fullpath+filename
            if os.path.exists(r''+fullfilepath+''):
                pass
            else:
                if windows:
                    if os.path.exists(r''+target+win+artist):
                        os.chdir(r''+target+win+artist)
                    else:
                        os.mkdir(r''+target+win+artist)
                        os.chdir(r''+target+win+artist)
                else:
                    if os.path.exists(r''+target+lin+artist):
                        os.chdir(r''+target+lin+artist)
                    else:
                        os.mkdir(r''+target+lin+artist)
                        os.chdir(r''+target+lin+artist)
            if os.path.exists(r''+fullpath):
                os.chdir(r''+fullpath)
            else:
                os.mkdir(r''+fullpath)
                os.chdir(r''+fullpath)
                print(fullfilepath)
                shutil.copyfile(r''+oldfilename+'', r''+fullfilepath+'')

def removeSymbols(st):
    while st.count('/') > 0:
        st = st.replace('/', '')
    while st.count('|') > 0:
        st = st.replace('|', '')
    while st.count('\\') > 0:
        st = st.replace('\\', '')
    while st.count('?') > 0:
        st = st.replace('?', '')
    while st.count(':') > 0:
        st = st.replace(':', '')
    while st.count('<') > 0:
        st = st.replace('<', '')
    while st.count('>') > 0:
        st = st.replace('>', '')
    while st.count('*') > 0:
        st = st.replace('*', '')
    while st.count('"') > 0:
        st = st.replace('"', '')
    while st.count('\'') > 0:
        st = st.replace('\'', '')
    return st
    
