
sleep 25.06

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.9
pkill sipp

sleep 3.48

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.27
pkill chromium