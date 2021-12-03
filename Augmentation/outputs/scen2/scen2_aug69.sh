
sleep 26.11

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.13
pkill sipp

sleep 4.87

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.85
pkill chromium