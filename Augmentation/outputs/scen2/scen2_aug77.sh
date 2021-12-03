
sleep 26.12

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.96
pkill sipp

sleep 5.56

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.58
pkill chromium