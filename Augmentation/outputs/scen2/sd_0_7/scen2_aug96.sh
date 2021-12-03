
sleep 24.97

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.04
pkill sipp

sleep 5.48

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.84
pkill chromium