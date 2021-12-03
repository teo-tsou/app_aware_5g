
sleep 25.33

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.41
pkill sipp

sleep 5.63

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 50.91
pkill chromium
