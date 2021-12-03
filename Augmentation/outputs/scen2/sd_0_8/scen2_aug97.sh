
sleep 25.03

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.6
pkill sipp

sleep 5.56

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.43
pkill chromium