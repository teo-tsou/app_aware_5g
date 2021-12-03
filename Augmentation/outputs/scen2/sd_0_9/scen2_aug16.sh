
sleep 24.25

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.76
pkill sipp

sleep 5.24

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.01
pkill chromium