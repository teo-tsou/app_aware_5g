
sleep 50

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 140
pkill sipp

sleep 10

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 102
pkill chromium