
sleep 23.94

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.58
pkill sipp

sleep 3.94

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.24
pkill chromium