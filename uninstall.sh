#!/bin/bash

sudo rm $(which ipfs)
sudo rm /etc/systemd/system/ipfs.service
sudo rm -rf /var/log/ipfs/