
sleep 24.93

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.99
pkill sipp

sleep 5.38

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.06
pkill chromium