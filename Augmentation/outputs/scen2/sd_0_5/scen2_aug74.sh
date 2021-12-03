
sleep 25.26

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.41
pkill sipp

sleep 5.55

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.3
pkill chromium