
sleep 25.54

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.45
pkill sipp

sleep 4.29

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.12
pkill chromium