
sleep 25.0

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.79
pkill sipp

sleep 3.91

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.24
pkill chromium