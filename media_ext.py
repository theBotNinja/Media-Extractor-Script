import os
import shutil
from tkinter import filedialog
from time import sleep
from random import choice

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

folder_stack = []
chipMode = {"imageExt" : ['.jpeg', '.jfif', '.tiff', '.jpg', '.exif', '.gif', '.bmp', '.png', '.ppm', '.pgm', '.pbm', '.pnm', '.webp', '.mpeg', '.heif'],
        "docExt":['.abw', '.acl', '.afp', '.ami', '.ans', '.asc', '.aww', '.ccf', '.csv', '.cwk', '.dbk', '.dita', '.doc', '.docm', '.docx',".xlsx",
                    ".accdb" ,'.dot', '.dotx', '.dwd', '.egt', '.epub', '.ezw', '.fdx', '.ftm', '.ftx', '.gdoc', '.html', '.hwp', '.hwpml', '.log', '.lwp',
                    '.mbp', '.md', '.me', '.mcw', '.mobi', '.nb', '.nb', '.nbp', '.neis', '.odm', '.odoc', '.odt', '.osheet', '.ott', '.omm', '.pages',"pub",
                     '.pap', '.pdax', '.pdf',"pptx", '.quox', '.rtf', '.rpt', '.sdw', '.se', '.stw', '.sxw', '.tex', '.info', '.troff', '.txt', '.uof', '.uoml',
                    '.via', '.wpd', '.wps', '.wpt', '.wrd', '.wrf', '.wri', '.xhtml', '.xml', '.xps'],
        "videoExt":['.mxf', '.3g2', '.3gp', '.svi', '.m4v', '.mpg', '.mpeg', '.m2v', '.mpg','.mp2', '.mpeg', '.mpe', '.mpv', '.webm', '.vob', '.drc',
             '.flv','.mkv', '.ogv', '.ogg', '.avi', '.mng', '.gifv', 'mts', '.m2ts', '.ts', '.mov', '.qt', '.rmvb', '.wmv', '.yuv', '.asf', 
             '.amv', '.mp4', '.m4p', '.m4v', '.rm', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b'],
        "audioExt":[".aa",".aax",".aac",".act",".aiff",".alac",".amr",".au",".awd",".dss",".dvf",".flac",".gsm",".ivs",".m4a",".m4b",".m4p",".mmf",".movpkg",".mp3",".msv",".mpc",".nmf",".ogg",".raw",".voc",".vox",".wav",".wma",".wv",".webm",".8svx",".cda"]
        } 

def getExt(path):
    for i in range(len(path)-1,-1,-1):
        if (path[i]=='.'):
            return path[i:]

for i in range(5):
    print(f"{bcolors.HEADER}{bcolors.BOLD}\r\t(^_^)",end="\r")
    sleep(.06)
    print(f"\r\t(o_o)",end="\r")
    sleep(.06)
    print(f"\r\t(^.^)",end="\r")
    sleep(.06)
    print(f"""\r\t(".")""",end="\r")
    sleep(.06)
    print(f"\r\t($.$){bcolors.ENDC}",end="\r")
    sleep(.06)

print(f"""{bcolors.OKGREEN}\t({choice(['^','o','"',"$"])}{choice(["_","."])}{choice(["^","o",'"',"$"])})\t{bcolors.ENDC}""")
print(f"press ENTER set Extaction path set to {bcolors.OKBLUE}{os.getcwd()}{bcolors.ENDC}")
ext_path = os.getcwd()
if (input(f"{bcolors.WARNING}change Extaction path ? -> {bcolors.ENDC}") == "y"):
    ext_path = filedialog.askdirectory()
    if (not ext_path):
        print(f"{bcolors.FAIL}path not provided{bcolors.ENDC}")
        exit()
print(f"\n{bcolors.OKGREEN}Extaction path set to {bcolors.OKBLUE}{ext_path}{bcolors.ENDC}\n")
print(f"press ENTER set Output path set to {bcolors.OKBLUE}{os.getcwd()}{bcolors.ENDC}")
output_path = os.getcwd()
if (input(f"{bcolors.WARNING}change Output path ? -> {bcolors.ENDC}") == "y"):
    output_path = filedialog.askdirectory()
    if (not output_path):
        print(f"{bcolors.FAIL}path not provided{bcolors.ENDC}")
        exit()
print(f"\n{bcolors.OKGREEN}Output path set to {bcolors.OKBLUE}{output_path}{bcolors.ENDC}\n")

moveORcopy = input(f"{bcolors.WARNING}Enter '0' to move and '1' to copy -> {bcolors.ENDC}" ).strip()
if (moveORcopy != '0' and moveORcopy != '1'):
    print(f"{bcolors.FAIL}proper input not found!!{bcolors.ENDC}")
    exit()

folder_stack.append(ext_path)
for key in chipMode.keys():
    try:
        os.mkdir(os.path.join(output_path,key))
    except FileExistsError:
        print(f"{bcolors.WARNING}output files already exists{bcolors.ENDC}")
while(len(folder_stack)):
    files=[]
    top_folder = folder_stack.pop()
    filesAndFolder = os.listdir(top_folder)
    for item in filesAndFolder:
        if (os.path.isdir(os.path.join(top_folder,item))):
            folder_stack.append(os.path.join(top_folder,item))
        else:
            files.append(os.path.join(top_folder,item))
    
    for item in files:
        #get ext of file 
        itemExt = getExt(item)
        #check where to place 
        for key in chipMode.keys():
            if itemExt in chipMode[key]:
                # opetation
                if not moveORcopy:
                    try:
                        shutil.move(item,os.path.join(output_path,key))
                        print(f"{item} {bcolors.OKCYAN}moved{bcolors.ENDC} {output_path}")
                        break
                    except Exception:
                        print(f"{bcolors.FAIL}Error:{Exception}{bcolors.ENDC}")
                else:
                    try:
                        shutil.copy(item,os.path.join(output_path,key))
                        print(f"{item} {bcolors.OKCYAN}copied{bcolors.ENDC} {output_path}")
                        break
                    except Exception:
                        print(f"{bcolors.FAIL}Error:{Exception}{bcolors.ENDC}")