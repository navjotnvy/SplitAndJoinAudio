#Change the Enviroment Variable to where the pydub repository is
# Also download the dependencies given i.e. download ffmpeg https://github.com/jiaaro/pydub#dependencies

from pydub import AudioSegment
fileplace_input = raw_input("Enter the folder name(Should be: Desktop, Downloads, Document or Music) :")
fileplace = fileplace_input[0].upper() + fileplace_input[1:].lower()
#print(fileplace)
filename = raw_input("Enter your file name with type(mp3,ogg,flv,mp4,wma,aiff(aac),wav)")

print("File will be divided into 3 parts and joined")
print("Part 1")
sec_first = float(raw_input("Part 1: Input in seconds from where you want to start split"))
sec_last  = float(raw_input("Part 1: Input in seconds where you want to end split"))

print("Part 2")
sec_third  = float(raw_input("Part 2: Input in seconds from where you want to start split"))
sec_fourth = float(raw_input("Part 2: Input in seconds where you want to end split"))

print("Part 3")
sec_fifth = float(raw_input("Part 3: Input in seconds from where you want to start split"))
sec_sixth = float(raw_input("Part 3: Input in seconds where you want to end split"))

if((fileplace=="Desktop")or(fileplace=="Downloads")or(fileplace=="Document")or(fileplace=="Music")):
    filetype = filename.split('.',1)[1]
    if(filetype=="mp3"):
        sound = AudioSegment.from_file("C:\Users\Unix\\"+fileplace+"\\"+filename, "mp3")
        #third = len(sound) / 3
        #thirdpart = sound[third:]
        #print(third)

        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.mp3", format="mp3")
        #thirdpart.export("C:/Users/Unix/"+fileplace+"/file1.mp3", format="mp3")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    elif(filetype=="ogg"):
        sound = AudioSegment.from_ogg("C:\Users\Unix\\"+fileplace+"\\"+filename, "ogg")
        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.ogg", format="ogg")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    elif(filetype=="flv"):
        sound = AudioSegment.from_flv("C:\Users\Unix\\"+fileplace+"\\"+filename, "flv")
        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.flv", format="flv")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    elif(filetype=="mp4"):
        sound = AudioSegment.from_file("C:\Users\Unix\\"+fileplace+"\\"+filename, "mp4")
        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.mp4", format="mp4")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    elif(filetype=="wma"):
        sound = AudioSegment.from_file("C:\Users\Unix\\"+fileplace+"\\"+filename, "wma")
        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.wma", format="wma")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    elif(filetype=="aac"):
        sound = AudioSegment.from_file("C:\Users\Unix\\"+fileplace+"\\"+filename, "aac")
        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.aac", format="aac")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    elif(filetype=="wav"):
        sound = AudioSegment.from_wav("C:\Users\Unix\\"+fileplace+"\\"+filename, "wav")
        #concept
        splitpart1 = sound[(sec_first*1000):(sec_last*1000)]
        splitpart2 = sound[(sec_third*1000):(sec_fourth*1000)]
        splitpart3 = sound[(sec_fifth*1000):(sec_sixth*1000)]
        splitpart = splitpart1 + splitpart2 + splitpart3
        #export
        splitpart.export("C:/Users/Unix/"+fileplace+"/file.wav", format="wav")
        print("Your file is downloaded at C:/Users/Unix/"+fileplace+"/file.mp3")
    else:
        print("Please enter mp3,ogg,flv,mp4,wma,aiff(aac),wav files only")
else:
    print("Please make sure that your file is in these FOLDER Desktop, Download, Document or Music")



'''
ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")
mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")
wav_version = AudioSegment.from_wav("never_gonna_give_you_up.wav")
'''

#backwards = sound.reverse()
#third = len(sound) / 3
#thirdpart = sound[third:]

#thirdpart.export("C:/Users/Unix/Desktop/file.mp3", format="mp3")
#backwards.export("C:/Users/Unix/Desktop/file.mp3", format="mp3")
