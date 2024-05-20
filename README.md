
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

<h3 align="center">Inscriber AutoV6</h3>

  <p align="center">
    This is a Doginal Inscription Auto-Inscriber that is modified from @martinseeger2's v5 Auto-Inscriber. This dynamically reads the files in your images folder as well as prints to screen pertinent information.
    <br />
    <a href="https://github.com/booktoshi/doginal-auto-inscriberv6"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/booktoshi/inscriber">View Demo</a>
    ·
    <a href="https://github.com/booktoshi/inscriber/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/booktoshi/inscriber/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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

[![Product Name Screen Shot][product-screenshot]]

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
   git clone https://github.com/booktoshi/doginal-auto-inscriberv6.git
   ```
2. Navigate to the project directory
   ```sh
   cd inscriber
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
python inscriber.py
```

The script will prompt you to confirm the detected file extension and input the duration for pauses between functions when specific errors are detected. It will display detailed information about the progress and status of each file being inscribed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add more error handling
- [ ] Enhance progress tracking
- [ ] Improve user prompts

See the [open issues](https://github.com/booktoshi/inscriber/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

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
[product-screenshot]: images/logo2.png
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
