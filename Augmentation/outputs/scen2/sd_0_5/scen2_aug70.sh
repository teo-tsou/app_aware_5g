
sleep 24.59

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.87
pkill sipp

sleep 5.11

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.97
pkill chromium
