
sleep 25.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.68
pkill sipp

sleep 5.04

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.97
pkill chromium
