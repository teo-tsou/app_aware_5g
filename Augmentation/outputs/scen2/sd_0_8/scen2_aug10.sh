
sleep 25.7

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.88
pkill sipp

sleep 6.11

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.84
pkill chromium