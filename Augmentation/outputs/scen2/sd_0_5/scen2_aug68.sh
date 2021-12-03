
sleep 24.75

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.1
pkill sipp

sleep 5.83

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.69
pkill chromium
