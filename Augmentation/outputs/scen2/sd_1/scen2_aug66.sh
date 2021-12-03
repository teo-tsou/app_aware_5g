
sleep 25.53

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.02
pkill sipp

sleep 4.3

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.65
pkill chromium