
sleep 24.96

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.27
pkill sipp

sleep 4.48

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.32
pkill chromium
