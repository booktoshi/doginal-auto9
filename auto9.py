import subprocess
import time
import json
import re
import os
from datetime import datetime
from tqdm import tqdm  # For the loading bar

def run_node_commands():
    # Prompt user for Dogecoin address
    doge_address = input("Please enter the Dogecoin address to inscribe to: ")

    # Create the inscriptionIDs folder if it doesn't exist
    inscription_folder = './inscriptionIDs'
    if not os.path.exists(inscription_folder):
        os.makedirs(inscription_folder)

    # Prepare the JSON file name
    json_file_name = os.path.join(inscription_folder, "inscriptionIDs.json")

    # Rename old JSON file if it exists
    if os.path.isfile(json_file_name):
        base_name, extension = os.path.splitext(json_file_name)
        counter = 1
        while os.path.isfile(f"{base_name}_{counter}{extension}"):
            counter += 1
        os.rename(json_file_name, f"{base_name}_{counter}{extension}")

    # Load existing data if any
    data = []
    inscribed_files = set()
    if os.path.isfile(json_file_name):
        with open(json_file_name, 'r') as file:
            data = json.load(file)
            for item in data:
                inscribed_files.add(item['name'])

    # Create or load airdropcomp.txt
    airdrop_comp_file = "airdropcomp.txt"
    airdrop_data = []
    if os.path.isfile(airdrop_comp_file):
        with open(airdrop_comp_file, 'r') as file:
            airdrop_data = [line.strip() for line in file.readlines()]

    # Create or load completion report
    completion_report_file = "completion_report.txt"
    if not os.path.isfile(completion_report_file):
        with open(completion_report_file, 'w') as file:
            file.write("Timestamp,File,TxID,Duration,Fees,Vout\n")

    total_minted = 0
    total_fees = 0.0

    # Define the directory to search for image files
    image_directory = './images'

    # Check if the directory exists
    if not os.path.exists(image_directory):
        print(f"Directory {image_directory} does not exist.")
        return

    # Get the list of all image files in the image directory and subdirectories
    all_files = []
    for root, dirs, files in os.walk(image_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg')):
                all_files.append(file_path)

    # Create a progress bar
    with tqdm(total=len(all_files), desc="Inscribing images", unit="file") as pbar:
        for file_path in all_files:
            if file_path in inscribed_files:
                print(f"File {file_path} already inscribed, skipping.")
                pbar.update(1)
                continue

            # Print the file being inscribed
            print(f"Inscribing file: {file_path}")

            start_time = time.time()

            # Construct and run the mint command
            mint_command = f"node . mint {doge_address} {file_path}"
            result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
            print("Output from mint command:")
            print(result_mint.stdout)

            # Check if there is an error in the mint command
            if result_mint.stderr:
                print("Error in mint command:")
                print(result_mint.stderr)

            # Check for success message in the mint command's output
            txid_search = re.search("inscription txid: (\w+)", result_mint.stdout)
            fees_search = re.search("Fees: ([0-9.]+) DOGE", result_mint.stdout)
            vout_search = re.search("vout: (\d+)", result_mint.stdout)
            if txid_search and fees_search and vout_search:
                txid = txid_search.group(1) + 'i0'
                fees = float(fees_search.group(1))
                vout = vout_search.group(1)
                total_fees += fees
                print(f"Successful mint, updating JSON file....")
                update_json_file(json_file_name, file_path, txid)
                airdrop_data.append(f"{doge_address},{txid}")
                total_minted += 1

                end_time = time.time()
                duration = end_time - start_time
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Append to the completion report
                with open(completion_report_file, 'a') as file:
                    file.write(f"{timestamp},{file_path},{txid},{duration:.2f},{fees},{vout}\n")

                if total_minted % 12 == 0:
                    print("Processed 12 files, taking a 120-second break...")
                    time.sleep(120)

            # Check for specific error message in the mint command's output
            if "'64: too-long-mempool-chain'" in result_mint.stdout:
                print("Detected specific error message, proceeding to wallet sync in 120 seconds...")
                time.sleep(120)

                # Loop for the second command
                while True:
                    wallet_sync_command = "node . wallet sync"
                    result_sync = subprocess.run(wallet_sync_command, shell=True, capture_output=True, text=True)
                    print("Output from wallet sync command:")
                    print(result_sync.stdout)

                    if result_sync.stderr:
                        print("Error in wallet sync command:")
                        print(result_sync.stderr)

                    # Check for success message
                    if "inscription txid" in result_sync.stdout:
                        print("Successful inscription, extracting txid and updating JSON file.")
                        txid_search = re.search("inscription txid: (\w+)", result_sync.stdout)
                        fees_search = re.search("Fees: ([0-9.]+) DOGE", result_sync.stdout)
                        vout_search = re.search("vout: (\d+)", result_sync.stdout)
                        if txid_search and fees_search and vout_search:
                            txid = txid_search.group(1) + 'i0'
                            fees = float(fees_search.group(1))
                            vout = vout_search.group(1)
                            total_fees += fees
                            update_json_file(json_file_name, file_path, txid)
                            airdrop_data.append(f"{doge_address},{txid}")
                            total_minted += 1

                            end_time = time.time()
                            duration = end_time - start_time
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                            # Append to the completion report
                            with open(completion_report_file, 'a') as file:
                                file.write(f"{timestamp},{file_path},{txid},{duration:.2f},{fees},{vout}\n")

                            if total_minted % 12 == 0:
                                print("Processed 12 files, taking a 120-second break...")
                                time.sleep(120)
                            break
                        else:
                            print("TXID not found in wallet sync output")

                    # Check for the specific error and retry
                    elif "'64: too-long-mempool-chain'" in result_sync.stdout:
                        print("Detected specific error message, retrying in 120 seconds...")
                        time.sleep(120)
                    else:
                        print("Unknown response, stopping the retry loop.")
                        break

            pbar.update(1)

    # Write airdropcomp.txt
    with open(airdrop_comp_file, 'w') as file:
        for line in airdrop_data:
            file.write(line + "\n")

    # Print the total number of files minted and total fees
    print(f"Total number of files minted: {total_minted}")
    print(f"Total fees used: {total_fees} DOGE")

def update_json_file(json_file_name, file_path, txid):
    new_data = {
        "inscriptionId": txid,
        "name": os.path.basename(file_path),
        "file_name": os.path.basename(file_path),
        "attributes": {
            "trait1": "trait1",
            "trait2": "trait2",
            "trait3": "trait3",
            "trait4": "trait4",
            "trait5": "trait5",
            "trait6": "trait6",
            "trait7": "trait7"
        }
    }

    data = []
    if os.path.isfile(json_file_name):
        with open(json_file_name, 'r') as file:
            data = json.load(file)
    
    data.append(new_data)

    with open(json_file_name, 'w') as file:
        json.dump(data, file, indent=4)

run_node_commands()
