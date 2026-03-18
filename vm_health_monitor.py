import psutil  
import argparse  


def check_vm_health():  
    # Get CPU, Memory, and Disk Usage  
    cpu_usage = psutil.cpu_percent(interval=1)  
    memory_usage = psutil.virtual_memory().percent  
    disk_usage = psutil.disk_usage('/').percent  
    
    # Check health status  
    healthy = True  
    reasons = []  
    if cpu_usage > 60:  
        healthy = False  
        reasons.append(f'CPU usage is at {cpu_usage}%.')  
    if memory_usage > 60:  
        healthy = False  
        reasons.append(f'Memory usage is at {memory_usage}%.')  
    if disk_usage > 60:  
        healthy = False  
        reasons.append(f'Disk usage is at {disk_usage}%.')  
    
    return healthy, reasons, cpu_usage, memory_usage, disk_usage  


if __name__ == '__main__':  
    parser = argparse.ArgumentParser(description='Check VM Health')  
    parser.add_argument('--explain', action='store_true', help='Display detailed explanation of health status.')  
    args = parser.parse_args()  
    healthy, reasons, cpu_usage, memory_usage, disk_usage = check_vm_health()  
    
    if healthy:  
        print('The virtual machine is healthy.')  
    else:  
        print('The virtual machine is not healthy.')  
    
    if args.explain:  
        print(f'CPU usage: {cpu_usage}%')  
        print(f'Memory usage: {memory_usage}%')  
        print(f'Disk usage: {disk_usage}%')  
        if not healthy:  
            for reason in reasons:  
                print(reason)  
