
sleep 24.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.94
pkill sipp

sleep 4.72

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.99
pkill chromium
