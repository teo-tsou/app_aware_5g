
sleep 25.53

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.04
pkill sipp

sleep 6.41

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.86
pkill chromium