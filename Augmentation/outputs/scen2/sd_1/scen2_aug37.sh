
sleep 23.82

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.81
pkill sipp

sleep 6.17

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.65
pkill chromium