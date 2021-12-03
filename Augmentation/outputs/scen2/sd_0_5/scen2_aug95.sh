
sleep 25.63

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.97
pkill sipp

sleep 5.28

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.72
pkill chromium
