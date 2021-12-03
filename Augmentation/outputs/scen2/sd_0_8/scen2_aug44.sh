
sleep 26.76

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.03
pkill sipp

sleep 5.0

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.27
pkill chromium