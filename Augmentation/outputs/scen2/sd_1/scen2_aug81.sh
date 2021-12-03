
sleep 25.32

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.05
pkill sipp

sleep 6.92

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.04
pkill chromium