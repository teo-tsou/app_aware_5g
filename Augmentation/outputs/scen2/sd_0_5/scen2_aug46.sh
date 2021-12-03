
sleep 24.62

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.14
pkill sipp

sleep 4.36

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.98
pkill chromium
