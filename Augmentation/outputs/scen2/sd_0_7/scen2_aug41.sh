
sleep 25.54

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.73
pkill sipp

sleep 3.99

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.84
pkill chromium