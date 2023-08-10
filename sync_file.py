import os
import sys
import shutil
import time
import hashlib
import schedule

def calculate_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def synchronize_folders(source_path, replica_path, log_path):
    try:
        print("Synchronizing folders...")
        with open(log_path, 'a') as log_file:
            log_file.write(f"Synchronization started at: {time.ctime()}\n")

            if os.path.exists(replica_path):
                for root, _, files in os.walk(source_path):
                    for file in files:
                        source_file_path = os.path.join(root, file)
                        replica_file_path = os.path.join(replica_path, os.path.relpath(source_file_path, source_path))
                        
                        source_hash = calculate_md5(source_file_path)
                        
                        if not os.path.exists(replica_file_path):
                            shutil.copy2(source_file_path, replica_file_path)
                        else:
                            replica_hash = calculate_md5(replica_file_path)
                            if source_hash != replica_hash:
                                shutil.copy2(source_file_path, replica_file_path)

                log_file.write("Synchronization completed successfully.\n")
                print("Synchronization completed successfully.")
            else:
                shutil.copytree(source_path, replica_path)

                log_file.write("Initial synchronization completed successfully.\n")
                print("Initial synchronization completed successfully.")
    except Exception as e:
        with open(log_path, 'a') as log_file:
            log_file.write(f"Error occurred: {str(e)}\n")
        print(f"Error occurred: {str(e)}")


def main():
    if len(sys.argv) != 5:
        print("Usage: python sync_folders.py <source_path> <replica_path> <interval_in_minutes> <log_path>")
        return
    
    source_path = sys.argv[1]
    replica_path = sys.argv[2]
    interval_in_minutes = int(sys.argv[3])
    log_path = sys.argv[4]

    print(f"Source Path: {source_path}")
    print(f"Replica Path: {replica_path}")
    print(f"Synchronization Interval: {interval_in_minutes} minutes")
    print(f"Log Path: {log_path}")

    if not os.path.exists(source_path):
        print("Source folder does not exist.")
        return
    if not os.path.exists(replica_path):
        os.makedirs(replica_path)

    # Initial synchronization
    synchronize_folders(source_path, replica_path, log_path)
    
    # Schedule periodic synchronizations
    schedule.every(interval_in_minutes).minutes.do(synchronize_folders, source_path, replica_path, log_path)

    print("Synchronization program started...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
