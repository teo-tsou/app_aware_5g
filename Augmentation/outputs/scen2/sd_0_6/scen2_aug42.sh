
sleep 25.9

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.38
pkill sipp

sleep 4.65

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.37
pkill chromium