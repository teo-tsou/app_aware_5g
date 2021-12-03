
sleep 25.41

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.61
pkill sipp

sleep 6.56

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.76
pkill chromium