
sleep 26.08

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.52
pkill sipp

sleep 4.2

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.49
pkill chromium