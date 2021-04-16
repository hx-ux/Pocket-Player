from flask import Flask, render_template,request
import time
import sys
import os
import subprocess
import time
import sys
import os
import subprocess
import glob
from signal import pause

curVideo='none'

def index_folder():
  fileExt=[".mp4",".avi",".m4v"]
  _files=[]
  for b in fileExt:
   for file in os.listdir("data"):    
         if file.endswith(b):
           _files.append(file)     
  print(_files)
  return _files


def play_video(_url,_name):
     url=_url    
     print('video started')
     subprocess.Popen(['omxplayer', '-b', '--loop', url, '&'])     
     curVideo=_name
     return curVideo
    
 

def stop_video(): 
  subprocess.call(['killall', 'omxplayer.bin'])
  os.system('clear')  
  curVideo='none'
  return curVideo

def index_folder_chs(_list):
     _len=len(_list)
     _list_chs=[0 for i in range(_len)]
     for x in range(0, _len):
      _list_chs[x]=x     
     return _list_chs

app = Flask(__name__)

@app.route('/')
def ws_index():   
      return render_template('index.html',output_data = mylist,len=len(mylist),index=mylist_chs,currV=curVideo)

@app.route('/video')
def ws_v_play():
     _request = request.args.get('video')     
     _num=(int(_request))     
     stop_video()     
     src='data/'+mylist[_num]
     play_video(src,mylist[_num])          
     return render_template('video.html')
@app.route('/shuffle')
def ws_v_shuffle():         
    stop_video()
    return "Nothing"
@app.route('/stop')
def ws_v_stop():    
    stop_video()    
    return render_template('stop.html')
@app.route('/scan_lib')
def ws_scan_lib():
    index_folder()
    return "Nothing"

if __name__ == '__main__':    
        
    mylist=index_folder()
    mylist_chs=index_folder_chs(mylist)
    app.run(debug=False, host='0.0.0.0')
