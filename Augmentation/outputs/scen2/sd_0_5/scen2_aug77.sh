
sleep 25.23

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.46
pkill sipp

sleep 5.5

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.62
pkill chromium