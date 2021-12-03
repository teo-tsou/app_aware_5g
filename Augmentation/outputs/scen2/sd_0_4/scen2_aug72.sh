
sleep 25.92

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.76
pkill sipp

sleep 4.94

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.97
pkill chromium