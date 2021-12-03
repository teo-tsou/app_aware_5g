
sleep 24.93

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.2
pkill sipp

sleep 6.14

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.37
pkill chromium