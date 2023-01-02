# EFFECTOR: DASH QoE and QoS Evaluation Framework For EnCrypTed videO tRaffic

Tools required to stream DASH video content

  - Mininet-wifi https://mininet-wifi.github.io/
  - goDASHBED https://github.com/uccmisl/goDASHbed
  - Caddy Web-server https://caddyserver.com/

# Steps to make a your own setup

![Blog diagram](https://github.com/razaulmustafa852/EFFECTOR/blob/main/phase_2.png)

 1. Install Mininet. https://mininet-wifi.github.io/get-started/
 2. In the next step, Install goDASHBED. How to install goDASHBED please follow: https://github.com/uccmisl/goDASHbed
 3. Next you need video. You can download videos from http://cs1dev.ucc.ie/misl/4K_non_copyright_dataset/. You will find 2,4,6,8,10 second segment size
 4. Once you downlaod the file, move all files to /var/www/html in a Ubuntu directory
 5. Run run.py to start doing experiments. In this file there many parameters you need to set, e.g., Technology -- 4G, 5G, Protocol -- TCP, QUIC etc. We explain different types of parameters in the paper.
 6. In topo.py, there are many functions where path is given to store pcaps & goDASHBED logs. Please change all path according to your system.
 7. Each experiment generate 1-pcap and 1-goDASHBED logs. 
 8. To extract QoS features from pcap downlaod scripts from our Google Drive https://drive.google.com/drive/folders/11nQwCPox1dkhZt8_sxrIK9EDXXcmX06E?usp=sharing.

# Single VM With All Scripts & Dependencies
 - https://drive.google.com/file/d/14fyG88dO9LthucnSw19_5QYyijtoFh17/view?usp=sharing
