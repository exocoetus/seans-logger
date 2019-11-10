from time import localtime, strftime
import os

def main():
    #start_time = time()
    init_time = localtime()
    #Check output folder
    cur_directory = os.getcwd()
    target_directory = os.path.join(cur_directory, r'logs')
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    #Initialize log file
    log_name = strftime("%Y-%m-%d_%Hh%Mm%Ss", init_time)
    file_name = log_name + ".txt"
    file = open(os.path.join(target_directory, file_name), "w+")
    logging = True
    print("Type ESC to escape.\n")
    file.write(log_name + "\n")
    current_time = localtime()
    log_time = strftime("%H:%M:%S", current_time)
    file.write(log_time + " - LOGGING START" + "\n")

    #Loop
    while logging:
        entry = str(input())
        #Escape condition
        if entry == "ESC":
            logging = False
            log_time = strftime("%H:%M:%S", current_time)
            file.write(log_time + " - LOGGING END" + "\n")
            file.close()
            print("Logging Ended.")
            break
        current_time = localtime()
        #TODO Time difference
        log_time = strftime("%H:%M:%S", current_time)
        file.write(log_time + " - " + entry + "\n")

if __name__ == "__main__":
    main()