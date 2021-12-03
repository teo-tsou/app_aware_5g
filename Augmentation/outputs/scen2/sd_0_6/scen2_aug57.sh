
sleep 26.08

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.19
pkill sipp

sleep 4.75

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.42
pkill chromium