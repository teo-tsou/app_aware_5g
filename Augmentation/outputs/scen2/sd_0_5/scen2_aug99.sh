
sleep 24.57

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.86
pkill sipp

sleep 4.92

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.18
pkill chromium
