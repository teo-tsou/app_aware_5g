
sleep 25.48

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.68
pkill sipp

sleep 4.58

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.17
pkill chromium