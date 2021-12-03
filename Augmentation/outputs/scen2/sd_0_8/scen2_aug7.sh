
sleep 24.4

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.14
pkill sipp

sleep 5.13

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.91
pkill chromium