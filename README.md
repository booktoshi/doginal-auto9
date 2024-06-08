
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/booktoshi/inscriber">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Auto9 Inscriber</h3>

  <p align="center">
    This is a Doginal Inscription Auto-Inscriber that is modified from @martinseeger2's v5 Auto-Inscriber. This dynamically reads the files in your images folder as well as prints to screen pertinent information.
    <br />
    <a href="https://github.com/booktoshi/doginal-auto9"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

This project is designed to automate the inscription of images with detailed terminal output, including file names being processed, progress tracking, and error handling. It ensures each image is inscribed only once and handles specific errors with appropriate pauses.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Ensure you have the following installed:

* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/booktoshi/doginal-auto9.git
   ```
2. Navigate to the project directory
   ```sh
   cd doginal-auto9
   ```
3. Install required packages
   ```sh
   npm install
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To use the script, run the following command:

```sh
python auto9.py
```

The script will prompt you to enter the Dogecoin address to inscribe to and will display detailed information about the progress and status of each file being inscribed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<!-- ROADMAP -->
## Roadmap

- [ ] Add more error handling
- [ ] Enhance progress tracking
- [ ] Improve user prompts

See the [open issues](https://github.com/booktoshi/inscriber/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Booktoshi - [@twitter_handle](https://twitter.com/twitter_handle) - booktoshi@example.com

Project Link: [https://github.com/booktoshi/inscriber](https://github.com/booktoshi/inscriber)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [othneildrew's Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Contributors](https://github.com/booktoshi/inscriber/graphs/contributors)
* [Issues](https://github.com/booktoshi/inscriber/issues)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/booktoshi/doginals.svg?style=for-the-badge
[contributors-url]: https://github.com/booktoshi/doginals/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/booktoshi/doginals.svg?style=for-the-badge
[forks-url]: https://github.com/booktoshi/doginals/forks
[stars-shield]: https://img.shields.io/github/stars/booktoshi/doginals.svg?style=for-the-badge
[stars-url]: https://github.com/booktoshi/doginals/stargazers
[issues-shield]: https://img.shields.io/github/issues/booktoshi/doginals.svg?style=for-the-badge
[issues-url]: https://github.com/booktoshi/doginals/issues
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
