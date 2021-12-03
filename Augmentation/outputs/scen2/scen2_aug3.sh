
sleep 26.14

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.91
pkill sipp

sleep 4.49

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.87
pkill chromium