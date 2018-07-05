import os

os.system("netsh interface show interface")


def enable():
    os.system('netsh interface set interface "Wi-Fi" admin=enable')


def disable():
    os.system('netsh interface set interface "Wi-Fi" admin=disable')


enable()
