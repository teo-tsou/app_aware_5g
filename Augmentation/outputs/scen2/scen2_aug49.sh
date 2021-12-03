
sleep 23.96

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.1
pkill sipp

sleep 3.11

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.74
pkill chromium