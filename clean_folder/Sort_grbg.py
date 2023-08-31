from pathlib import Path
from sys import argv
import os
import shutil

def normalize(text, suf = None):
    import re
    
    str1 = ""
    
    text = text[:-(len(suf))] if suf else ...
    
    text = re.sub("\W+", "_", text)
    
    for let in text:
        if let.islower():
            str1 += let.translate(letters)
        elif let.isupper():
            let = let.lower()
            up_let = let.translate(letters)
            str1 += up_let.upper()
        else:
            str1 += let
    
    str1 += suf if suf else ...
    
    return str1

def make_file_name(file_name, dir):
    file_path = str(path_grbg) + fr"\{dir}\\"
    if not Path(file_path).is_dir():
        os.mkdir(file_path)
    fin_file_path = file_path + file_name
    
    return fin_file_path
    
letters = {
        ord('а'): 'a',
        ord('б'): 'b',
        ord('в'): 'v',
        ord('г'): 'g',
        ord('д'): 'd',
        ord('е'): 'e',
        ord('ё'): 'e',
        ord('ж'): 'zh',
        ord('з'): 'z',
        ord('и'): 'i',
        ord('й'): 'y',
        ord('к'): 'k',
        ord('л'): 'l',
        ord('м'): 'm',
        ord('н'): 'n',
        ord('о'): 'o',
        ord('п'): 'p',
        ord('р'): 'r',
        ord('с'): 's',
        ord('т'): 't',
        ord('у'): 'u',
        ord('ф'): 'f',
        ord('х'): 'h',
        ord('ц'): 'ts',
        ord('ч'): 'ch',
        ord('ш'): 'sh',
        ord('щ'): 'sch',
        ord('ъ'): '',
        ord('ы'): 'y',
        ord('ь'): '',
        ord('э'): 'e',
        ord('ю'): 'yu',
        ord('я'): 'ya'
    }
folder_list = ["archives", "videos", "images", "documents", "audio", "other"]
suf_dict = {"img": [".jpeg", ".jpg", ".png", ".svg"],
            "vid": [".avi", ".mp4", ".mov", ".mkv"],
            "doc": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
            "mus": [".mp3", ".ogg", ".wav", ".amr"],
            "arch": [".zip", ".gz", ".tar"]}
files_dict = {"img": [], "vid": [], "doc": [], "mus": [], "arch": [], "other": []}
inc_suf = []
unknown_suf = [] 

try:
    param = argv[1]
except IndexError:
    print("Use path as a param")
    exit()
    
param1 = " ".join(argv[1:])
print(param1)
path_grbg = Path(fr"{param1}") 

if not path_grbg.is_dir():
    print("Use the possible path!")
    exit()
           
def sorting(path):
    num = 2 
    
    for file in path.iterdir():
        if file.is_dir() and not file.name in folder_list:
            sorting(file)
            file.rmdir()
            continue
        elif file.is_dir and file.name in folder_list:
            continue
        
        suf = file.suffix
        new_file_name = normalize(file.name, suf)
        
        if suf in suf_dict['img']:
            files_dict['img'].append(new_file_name)
            inc_suf.append(suf) if not suf in inc_suf else ...
            new_file_path = make_file_name(new_file_name, "images")
        elif suf in suf_dict['doc']:
            files_dict['doc'].append(new_file_name)
            inc_suf.append(suf) if not suf in inc_suf else ...
            new_file_path = make_file_name(new_file_name, "documents")
        elif suf in suf_dict['mus']:
            files_dict['mus'].append(new_file_name)
            inc_suf.append(suf) if not suf in inc_suf else ...
            new_file_path = make_file_name(new_file_name, "audio")
        elif suf in suf_dict['vid']:
            files_dict['vid'].append(new_file_name)
            inc_suf.append(suf) if not suf in inc_suf else ...
            new_file_path = make_file_name(new_file_name, "video")
        elif suf in suf_dict['arch']:
            files_dict['arch'].append(new_file_name)
            inc_suf.append(suf) if not suf in inc_suf else ...
            new_file_path = new_file_path = make_file_name((new_file_name[:-(len(suf))]), "archives")
            os.mkdir(new_file_path)
            shutil.unpack_archive(file, new_file_path)
            os.remove(file)
            continue
        else:
            files_dict['other'].append(new_file_name)
            unknown_suf.append(suf) if not suf in inc_suf else ...
            new_file_path = make_file_name(new_file_name, "other")
        
        while True:
            path_check = Path(new_file_path)
            if path_check.is_file():
                if new_file_path[-7:-4] == (f"({num-1})"):
                    new_file_path = f"{new_file_path[:-(len(suf))-3]}({num}){suf}"
                else:
                    new_file_path = f"{new_file_path[:-(len(suf))]}({num}){suf}"
                num += 1
            else:
                break
            
        os.rename(file, new_file_path)

        
def sort_folder():
        
    sorting(path_grbg)
    
    print(files_dict)
    print(inc_suf)
    print(unknown_suf)
    

if __name__ == "__main__":
                 
    sorting(path_grbg)
    
    print(files_dict)
    print(inc_suf)
    print(unknown_suf)
