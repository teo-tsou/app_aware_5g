
sleep 24.16

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.14
pkill sipp

sleep 5.43

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.3
pkill chromium
