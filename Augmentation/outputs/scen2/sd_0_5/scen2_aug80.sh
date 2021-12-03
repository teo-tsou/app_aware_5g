
sleep 25.17

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.41
pkill sipp

sleep 4.51

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.97
pkill chromium
