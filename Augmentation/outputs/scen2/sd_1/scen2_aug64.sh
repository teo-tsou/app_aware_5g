
sleep 27.41

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.83
pkill sipp

sleep 4.17

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.29
pkill chromium