
sleep 23.29

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.29
pkill sipp

sleep 3.72

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.25
pkill chromium