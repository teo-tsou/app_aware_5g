
sleep 25.62

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.94
pkill sipp

sleep 4.76

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.09
pkill chromium
