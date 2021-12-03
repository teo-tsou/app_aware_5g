
sleep 25.11

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.16
pkill sipp

sleep 3.78

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.05
pkill chromium