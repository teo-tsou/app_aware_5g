
sleep 26.19

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.22
pkill sipp

sleep 4.69

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.21
pkill chromium