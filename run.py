import os
import sys
import subprocess

mode=['5g'] #Network type '5G', '4G' # List
host=[1] # Number of host
algo=['bba','elastic','conventional']#ABS List -- 'elastic','bba','logistic'
net5=['4g_Case_1','4g_Case_2','4g_Case_3','4g_Case_4','4g_Case_5'] # List
prot=['quic'] # List ['tcp','quic']
sertype=['WSGI'] # List
count = [1] # List of Experiments  # [1,2,3,4,5]

for curr in count:
    for md in mode:
        if md == '5g':
           for i in net5:
               #for j in doc5:
                   for k in sertype:
                       for l in host:
                           for m in algo:
                                for p in prot:
                                    clear = 'sudo mn -c'
                                    test3 = 'sudo python3 topo.py '+ str(md)+ ' ' + str(i) + ' ' + str(l)+ ' ' + str(m)+ ' ' + str(p)+ ' ' + str(k)+ ' ' + str(curr)
                                    subprocess.run(clear.split(' '))
                                    print(test3)
                                    subprocess.run(test3.split(' '))
        elif md =='4g':
            for i in net4:
               #for j in doc4:
                   for k in sertype:
                       for l in host:
                           for m in algo:
                               for p in prot:
                                    clear = 'sudo mn -c'
                                    test3 = 'sudo python topo.py '+ str(md)+ ' ' + str(i) + ' ' + str(l)+ ' ' + str(m)+ ' ' + str(p)+ ' ' + str(k)+ ' ' + str(curr)
                                    subprocess.run(clear.split(' '))
                                    print(test3)
                                    subprocess.run(test3.split(' '))
        else:
            for i in net3:
               #for j in doc3:
                   for k in sertype:
                       for l in host:
                           for m in algo:
                               for p in prot:
                                    clear = 'sudo mn -c'
                                    test3 = 'sudo python topo.py '+ str(md)+ ' ' + str(i) + ' '  + str(l)+ ' ' + str(m)+ ' ' + str(p)+ ' ' + str(k)+ ' ' + str(curr)
                                    subprocess.run(clear.split(' '))
                                    print(test3)
                                    subprocess.run(test3.split(' '))
