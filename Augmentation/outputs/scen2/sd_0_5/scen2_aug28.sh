
sleep 24.81

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.5
pkill sipp

sleep 4.98

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.38
pkill chromium
