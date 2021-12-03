
sleep 26.03

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.06
pkill sipp

sleep 4.4

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.51
pkill chromium