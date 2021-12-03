
sleep 24.83

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.63
pkill sipp

sleep 5.55

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.27
pkill chromium
