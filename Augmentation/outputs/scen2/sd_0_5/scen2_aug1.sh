
sleep 24.69

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.26
pkill sipp

sleep 5.22

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.9
pkill chromium
