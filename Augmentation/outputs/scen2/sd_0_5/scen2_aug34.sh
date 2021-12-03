
sleep 25.37

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.42
pkill sipp

sleep 5.16

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.3
pkill chromium
