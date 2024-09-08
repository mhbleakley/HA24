#!/usr/bin/bash
# move services
echo 'copying services to systemd'
sudo cp /home/hrfo/HA24/RPi/HA24-API.service /etc/systemd/system/
sudo cp /home/hrfo/HA24/RPi/HA24-BROWSER.service /etc/systemd/system/
sudo cp /home/hrfo/HA24/RPi/HA24-NODE.service /etc/systemd/system/
# move chromium script
echo 'copying chromium script to ~'
sudo cp /home/hrfo/HA24/RPi/HA24-start-chromium.sh /home/hrfo/
sudo chmod +x /home/hrfo/HA24-start-chromium.sh
# enable services
echo 'enabling services'
sudo systemctl enable HA24-API.service
sudo systemctl enable HA24-NODE.service
sudo systemctl enable HA24-BROWSER.service
# reboot after this point
echo 'configuration complete, you should reboot now'