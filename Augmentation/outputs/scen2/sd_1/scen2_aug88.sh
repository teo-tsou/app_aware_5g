
sleep 27.07

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.88
pkill sipp

sleep 5.68

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.23
pkill chromium