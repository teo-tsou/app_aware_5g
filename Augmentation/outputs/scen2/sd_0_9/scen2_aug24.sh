
sleep 25.84

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.44
pkill sipp

sleep 5.76

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.93
pkill chromium