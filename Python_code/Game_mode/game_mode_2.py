#!/bin/usr/env python3
import subprocess
import os

# programs to open
try:
    subprocess.Popen('F:\\ExitLag\\ExitLag.exe')
    subprocess.Popen(
        'C:\\Users\\onio_\\AppData\\Local\\Programs\\wooting-double-movement\\wooting-double-movement.exe')
    subprocess.Popen(
        '"C:\\Program Files (x86)\\MSI Afterburner\\MSIAfterburner.exe"')
    subprocess.Popen(
        '"C:\\Program Files\\SteelSeries\\GG\\SteelSeriesGG.exe" -dataPath="C:\\ProgramData\\SteelSeries\\GG" -dbEnv=production')
except Exception as e:
    print("Error opening programs:", e)

# firewalls to shut off
try:
    subprocess.check_call('netsh.exe advfirewall set domainprofile state off')
    subprocess.check_call('netsh.exe advfirewall set privateprofile state off')
    subprocess.check_call('netsh.exe advfirewall set publicprofile state off')
except Exception as e:
    print("Error shutting off firewall:", e)

# turn off extra monitor
try:
    os.system("Displayswitch.exe/internal")
except Exception as e:
    print("Error turning off extra monitor:", e)
