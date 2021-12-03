
sleep 23.84

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.41
pkill sipp

sleep 5.4

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.13
pkill chromium