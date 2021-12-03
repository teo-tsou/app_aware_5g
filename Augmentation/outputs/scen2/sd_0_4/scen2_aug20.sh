
sleep 25.13

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.1
pkill sipp

sleep 5.07

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.85
pkill chromium