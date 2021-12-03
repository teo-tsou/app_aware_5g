
sleep 26.68

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.5
pkill sipp

sleep 4.79

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 53.2
pkill chromium
