
sleep 25.28

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.96
pkill sipp

sleep 3.42

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.46
pkill chromium