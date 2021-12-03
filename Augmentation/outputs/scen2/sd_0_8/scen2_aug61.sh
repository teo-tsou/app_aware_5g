
sleep 25.98

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.94
pkill sipp

sleep 4.49

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.94
pkill chromium