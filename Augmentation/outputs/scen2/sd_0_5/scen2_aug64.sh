
sleep 25.05

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.38
pkill sipp

sleep 5.05

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.83
pkill chromium
