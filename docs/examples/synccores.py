/*
Illustrates the synchronisation across all cores, all cores display the hello message,wait and then the after message once othe cores have
caught up. Comment out the sync line and rerun to see the messages more interleaved
To run: epython synccores.py
*/
import parallel

print "Hello from core "+coreid()
sync()
print "After sync from core "+coreid()
