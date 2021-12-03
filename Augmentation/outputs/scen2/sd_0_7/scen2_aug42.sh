
sleep 25.02

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.4
pkill sipp

sleep 5.51

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.17
pkill chromium