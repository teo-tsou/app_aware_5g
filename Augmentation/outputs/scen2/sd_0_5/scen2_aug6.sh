
sleep 24.88

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.4
pkill sipp

sleep 5.86

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.57
pkill chromium
