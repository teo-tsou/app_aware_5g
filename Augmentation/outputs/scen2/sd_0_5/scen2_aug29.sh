
sleep 24.97

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.07
pkill sipp

sleep 4.53

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.59
pkill chromium
