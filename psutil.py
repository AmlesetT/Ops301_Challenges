#!/usr/bin/env python3

# Script Name:                  Ops 301 - Challenge 11
# Author:                       Amleset Tesfamariam, CF Ops lecture 301, Google, ChatGPT
# Date of latest revision:      09/11/2023
# Purpose:                      To create a script in Python that fetches certain information using Psutil.
# Reason:                       It is important to quickly and efficiently use code to pull necessary information.


# Declaration of variables

import psutil


# Requesting system times using Psutil

# Time spent by normal processes executing in user mode
user_time = psutil.cpu_times().user

# Time spent by processes executing in kernel mode
kernel_time = psutil.cpu_times().system

# Time when system was idle
idle_time = psutil.cpu_times().idle

# Time spent by priority processes executing in user mode
priority_user_time = psutil.cpu_times().nice

# Time spent waiting for I/O to complete
io_wait_time = psutil.cpu_times().iowait

# Time spent for servicing hardware interruptions 
irq_time = psutil.cpu_times().irq

# Time spent for servicing software interruptions
soft_irq_time = psutil.cpu_times().softirq

# Time spent by other operating systems running in a virtualized environment
steal_time = psutil.cpu_times().steal

# Time spent running a virtual CPU for guest operating systems under control of the Linux kernel
guest_time = psutil.cpu_times().guest

# Print fetched system information
print(f"Time spent by normal processes executing in user mode: {user_time} seconds")

print(f"Time spent by processes executing in kernel mode: {kernel_time} seconds")

print(f"Time when system was idle: {idle_time} seconds")

print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")

print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")

print(f"Time spent for servicing hardware interruptions: {irq_time} seconds")

print(f"Time spent for servicing software interruptions: {soft_irq_time} seconds")

print(f"Time spent by other operating systems running in a virtualized environment: {steal_time} seconds")

print(f"Time spent running a virtual CPU for guest operating systems under control of the Linux kernel: {guest_time} seconds")


# End