
sleep 24.81

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.2
pkill sipp

sleep 6.09

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.39
pkill chromium
