
sleep 23.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.79
pkill sipp

sleep 4.74

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.42
pkill chromium
