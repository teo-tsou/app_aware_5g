
sleep 25.84

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.39
pkill sipp

sleep 5.97

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.73
pkill chromium