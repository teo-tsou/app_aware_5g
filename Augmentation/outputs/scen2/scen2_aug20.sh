
sleep 23.85

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.29
pkill sipp

sleep 6.24

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 49.32
pkill chromium