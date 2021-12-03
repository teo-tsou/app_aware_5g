
sleep 26.48

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.65
pkill sipp

sleep 4.99

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.73
pkill chromium