
sleep 24.16

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.08
pkill sipp

sleep 6.18

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.01
pkill chromium