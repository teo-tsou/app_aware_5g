
sleep 25.36

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.97
pkill sipp

sleep 4.13

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.98
pkill chromium