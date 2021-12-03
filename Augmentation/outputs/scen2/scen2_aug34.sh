
sleep 25.12

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.08
pkill sipp

sleep 6.08

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.45
pkill chromium