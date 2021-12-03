
sleep 25.6

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.79
pkill sipp

sleep 5.33

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.57
pkill chromium