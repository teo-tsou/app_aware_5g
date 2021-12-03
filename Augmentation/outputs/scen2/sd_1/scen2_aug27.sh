
sleep 24.07

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.19
pkill sipp

sleep 6.95

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.99
pkill chromium