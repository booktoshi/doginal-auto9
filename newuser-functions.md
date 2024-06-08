```markdown
## Functions

### `run_node_commands()`

This is the main function that handles the entire process of inscribing images, managing errors, and logging progress.

#### Terminal Prompt
- "Please enter the Dogecoin address to inscribe to:"

```python
def run_node_commands():
    """
    Prompts the user for a Dogecoin address and processes all images in the './images' directory,
    inscribing each image onto the Dogecoin blockchain while handling errors and logging progress.
    """
```

### `update_json_file(json_file_name, file_path, txid)`

Updates the `inscriptionIDs.json` file with new inscription data.

```python
def update_json_file(json_file_name, file_path, txid):
    """
    Updates the JSON file with the new inscription data.

    Parameters:
        json_file_name (str): The path to the JSON file to update.
        file_path (str): The path to the file being inscribed.
        txid (str): The transaction ID of the inscription.
    """
```

### `main()`

The main entry point for the script, which calls `run_node_commands()`.

```python
def main():
    """
    Main entry point for the script. Calls the run_node_commands function.
    """
    run_node_commands()
```

### `load_existing_data(json_file_name)`

Loads existing inscription data from the JSON file if it exists.

```python
def load_existing_data(json_file_name):
    """
    Loads existing inscription data from the JSON file.

    Parameters:
        json_file_name (str): The path to the JSON file to load.

    Returns:
        data (list): A list of existing inscription data.
        inscribed_files (set): A set of filenames that have already been inscribed.
    """
```

### `write_completion_report(completion_report_file, timestamp, file_path, txid, duration, fees, vout)`

Writes a line to the completion report file with details about the inscription.

```python
def write_completion_report(completion_report_file, timestamp, file_path, txid, duration, fees, vout):
    """
    Writes a line to the completion report file with details about the inscription.

    Parameters:
        completion_report_file (str): The path to the completion report file.
        timestamp (str): The timestamp of the inscription.
        file_path (str): The path to the file being inscribed.
        txid (str): The transaction ID of the inscription.
        duration (float): The duration of the inscription process.
        fees (float): The fees used for the inscription.
        vout (str): The vout value of the transaction.
    """
```

### `log_airdrop_data(airdrop_comp_file, airdrop_data)`

Writes the airdrop data to the `airdropcomp.txt` file.

```python
def log_airdrop_data(airdrop_comp_file, airdrop_data):
    """
    Writes the airdrop data to the airdropcomp.txt file.

    Parameters:
        airdrop_comp_file (str): The path to the airdrop completion file.
        airdrop_data (list): A list of airdrop data to be written.
    """
```

### `prompt_doge_address()`

Prompts the user to enter the Dogecoin address for inscription.

#### Terminal Prompt
- "Please enter the Dogecoin address to inscribe to:"

```python
def prompt_doge_address():
    """
    Prompts the user to enter the Dogecoin address for inscription.

    Returns:
        doge_address (str): The Dogecoin address entered by the user.
    """
```

### `print_progress(file_path, total_minted, total_files)`

Prints the progress of the inscription process.

```python
def print_progress(file_path, total_minted, total_files):
    """
    Prints the progress of the inscription process.

    Parameters:
        file_path (str): The path to the file being inscribed.
        total_minted (int): The total number of files successfully inscribed.
        total_files (int): The total number of files to be inscribed.
    """
```
```
