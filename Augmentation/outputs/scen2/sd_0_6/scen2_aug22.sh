
sleep 23.99

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.89
pkill sipp

sleep 5.47

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.52
pkill chromium