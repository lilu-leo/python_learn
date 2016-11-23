import time
import webbrowser

total_breaks = 3
break_count = 0
print("This program started on " + time.ctime())

while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://v.youku.com/v_show/id_XMTgzMDM2OTMyMA==.html?spm=a2hww.20023042.m_223465.5~5~5~5!3~5!2~5~A&from=y1.3-idx-beta-1519-23042.223465.8-1")
    break_count = break_count + 1
    print("This program run on " + time.ctime())
print ("This program end on " + time.ctime())
