import stagger
import os
import shutil
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
            oldfilename = os.getcwd()+"\\"+y
            tag = stagger.read_tag(y) 
            title = tag.title
            artist = tag.artist
            trackNr = tag.track
            album = tag.album
            print(album)
            filename = str(trackNr)+" - "+title+".mp3"
            if len(album) > 0:
                if windows:
                    fullpath = target+win+artist+win+album+win
                else:
                    fullpath = target+lin+artist+lin+album+lin
            else:
                if windows:
                    fullpath = target+win+artist+win+"NoAlbum"+win
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
                shutil.copyfile(r''+oldfilename, r''+fullfilepath)
                os.chdir(source)
                os.chdir(x)
