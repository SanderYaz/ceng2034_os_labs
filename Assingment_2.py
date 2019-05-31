#!/bin/bash
hd -n 512 /dev/sda > MyMbr.txt
echo 'menuentry "ubuntu-18.10-desktop-amd64.iso" {
set isofile="/home/sanman/ubuntu-18.10-desktop-amd64.iso"
loopback loop (hd0,5)$isofile
linux (loop)/sanman/vmlinuz boot=casper iso-scan/filename=${isofile} quiet splash
initrd (loop)/sanman/initrd
}' >> /etc/grub.d/40_custom
update-grub
reboot
