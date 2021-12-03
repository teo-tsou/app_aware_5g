
sleep 25.15

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.84
pkill sipp

sleep 5.48

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.33
pkill chromium