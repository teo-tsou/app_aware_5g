
sleep 25.18

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.21
pkill sipp

sleep 5.22

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.7
pkill chromium
