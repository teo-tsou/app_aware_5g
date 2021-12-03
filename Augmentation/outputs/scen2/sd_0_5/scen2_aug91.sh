
sleep 25.47

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.19
pkill sipp

sleep 5.12

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 50.96
pkill chromium
