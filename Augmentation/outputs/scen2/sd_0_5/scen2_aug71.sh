
sleep 25.07

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.64
pkill sipp

sleep 5.32

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.72
pkill chromium
