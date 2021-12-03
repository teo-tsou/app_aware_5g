
sleep 25.08

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.81
pkill sipp

sleep 5.05

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.26
pkill chromium