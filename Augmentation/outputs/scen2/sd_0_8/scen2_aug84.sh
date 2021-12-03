
sleep 25.14

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.22
pkill sipp

sleep 4.17

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.5
pkill chromium