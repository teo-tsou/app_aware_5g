
sleep 24.9

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.67
pkill sipp

sleep 4.64

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 53.25
pkill chromium
