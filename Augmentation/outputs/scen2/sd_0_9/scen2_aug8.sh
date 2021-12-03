
sleep 25.68

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.79
pkill sipp

sleep 6.77

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.21
pkill chromium