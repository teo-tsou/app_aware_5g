
sleep 24.72

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.24
pkill sipp

sleep 4.31

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.82
pkill chromium