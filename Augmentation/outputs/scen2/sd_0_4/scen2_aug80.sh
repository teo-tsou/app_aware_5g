
sleep 24.79

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.46
pkill sipp

sleep 4.85

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.76
pkill chromium