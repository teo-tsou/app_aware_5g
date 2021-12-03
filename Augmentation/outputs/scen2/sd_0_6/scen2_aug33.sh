
sleep 25.74

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.76
pkill sipp

sleep 4.79

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.63
pkill chromium