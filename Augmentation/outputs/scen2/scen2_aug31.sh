
sleep 25.58

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.0
pkill sipp

sleep 6.49

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.88
pkill chromium