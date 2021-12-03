
sleep 24.2

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.43
pkill sipp

sleep 4.44

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.04
pkill chromium