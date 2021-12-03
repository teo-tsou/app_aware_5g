
sleep 25.38

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.52
pkill sipp

sleep 5.24

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.14
pkill chromium