from googleapiclient.discovery import build
import sys
import json, time, os

green     = '\033[92m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
black='\033[30m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'

api_key =  "AIzaSyD9JDXhHNhwBLKCIVmUdjf2Bew8NfJ-UwE"
youtube = build('youtube', 'v3', developerKey=api_key)
# req = youtube.search().list(q='code with harry', part='snippet', type='video')
# res = req.execute()
# num = sys.argv[1]
playlist_id = input("Enter The Play list Id : ")
# ----------------
nextPage = None
list = []
try:
    while True:
        res = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults='50',
        pageToken=nextPage,
        ).execute()
        list += res['items']
        try:
            nextPage = res['nextPageToken']
        except :
            break
except :
    print(f'{red}\ninvalid playlist id , doesnt match !{end}\n')
    print(f'{lightgrey}Enter a valid playlist id{end}\n')
    exit()
    

channel_name = res['items'][0]['snippet']['channelTitle']
print(f"{green}{bold}\nChannel name : {channel_name}{end}")
# list_title = [list['items'][i]['snippet']['title'] for i in range(len(list['items']))]

list_title = [i['snippet']['title'] for i in list]
# for i in range(len(list_title)):
#     print(i+1, list_title[i])
# --------------

title_list = list_title
# title_list = [res['items'][i]['snippet']['title'] for i in range(len(data['items']))]
names_list = [i for i in os.listdir() if '.mp4' in i]

title = [i.replace('[','_').replace(']','_').replace('?','_').replace(':','_').replace('|','_').replace('+','_').replace('*','_').replace('🔥', '_fire_') for i in title_list]
names = [i.replace(" ( 720 X 1280 ).mp4", "") for i in names_list]



def rename_files(list1,list2):
    title_count = 0
    for i in list1:
        title_count += 1
        name_count = 0
        for j in list2:
            name_count += 1
            if i in j:
                #print(f"{title_count} > '{i}'' found on index {name_count}***")
                #print(f"{title_list[title_count-1]}")
                #print(f"{title_count} {names_list[name_count-1]}")
                try:
                	os.rename(names_list[name_count-1], f"{title_count} {names_list[name_count-1]}")
                	print(f"{title_count} {names_list[name_count-1]}")
                except:
                	continue
                #print(i)
               
                
# print(title)

# print(names)
#rename_files(title, names)
def view_list():
	for i in range(len(title)):
		print(f'{lightred}{i+1}{end} {Yellow}{title[i]}{end}')
                                   
while True:
	command = input(f"\n{Cyan}--> (view/rename/exit)? :{end}")
	if command == 'view' or command == 'v':
		view_list()
	elif command == 'rename' or command == 'r':
		rename_files(title, names)
	elif command == 'exit'or command == 'e' or command == 'q':
		print()
		print("Exiting!")
		exit()
	elif command == 'help' or command == 'h' or command == '':
		print(f'''{Magenta}
-->h/help for help message
-->v/view for viewing the playlist
-->r/rename for renaming in current directory
-->e/exit/q for quit{end}
        \n''')
	else:
		print("\nINVALID input !!\n")
