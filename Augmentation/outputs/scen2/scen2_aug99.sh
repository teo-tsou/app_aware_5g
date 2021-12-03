
sleep 24.22

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.43
pkill sipp

sleep 4.29

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.11
pkill chromium