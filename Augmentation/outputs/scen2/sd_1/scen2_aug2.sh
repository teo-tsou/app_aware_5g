
sleep 24.42

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.1
pkill sipp

sleep 2.97

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 54.08
pkill chromium