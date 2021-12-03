
sleep 25.87

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.16
pkill sipp

sleep 5.19

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.09
pkill chromium
