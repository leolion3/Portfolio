<link rel="stylesheet" type="text/css" href="html/style.css"/>
<div class="table-responsive" style="overflow:auto;">
  <table class="table table-bordered">
    <thead>
      <tr>
        <th scope="col"><a href="#welcome" style="color:#b5e853; text-decoration: none;">Welcome</a></th>
        <th scope="col"><a href="#my-resume" style="color:#b5e853; text-decoration: none;">Resume</a></th>
        <th scope="col"><a href="#my-tools" style="color:#b5e853; text-decoration: none;">Tools</a></th>
        <th scope="col"><a href="#publications" style="color:#b5e853; text-decoration: none;">Publications</a></th>
        <th scope="col"><a href="#me-etc" style="color:#b5e853; text-decoration: none;">More from me</a></th>
        <th scope="col"><a href="#google-play" style="color:#b5e853; text-decoration: none;">Google Play</a></th>
        <th scope="col"><a href="#contact-section" style="color:#b5e853; text-decoration: none;">Contact</a></th>
      </tr>
    </thead>
  </table>
</div>

<p></p>

<h2 id="welcome">Welcome, friend</h2>

On this website you can find a bunch of useful tools, both for your personal workstation, as well as for your professional life.
This website also serves as my Portfolio, so if you're looking to hire me, or are interested in filing a development request, don't hesitate to use the <a href="#contact-section">contact section below</a>.

*For resources to help you with University subjects, check out my other <a href="https://uni.leolion.tk/" target="_blank">website <i class="fa fa-external-link"></i></a>*

**All tools provided on this website are free to use and change, misuse however, is prohibited. Any damage caused by these tools, in addition to violations of local restrictions, are your own problem, not mine.** 

---

<h1 id="my-resume">Who am I?</h1>

{% capture p1 %}{% include_relative Etc/leolion3/README.md %}{% endcapture %}
{{ p1 | markdownify }}

<p>Wanna know if you should hire me or need a software developed? Check out my interactive digital resume below (or <a href='https://leolion3.github.io/Portfolio/CV/' target='_blank' id='digital-resume'>here <i class="fa fa-external-link"></i></a>).</p>

<details>
  <summary>
  	<b style="color: purple;"><i class="fa-solid fa-user"></i> Show Resume</b>
  </summary>
  <div>
  	{% capture p21 %}{% include_relative CV/README.md %}{% endcapture %}
	  {{ p21 | markdownify }}
  </div>
</details>

---

<h1 id="my-tools">Ok, so what's on the menu?</h1>

Well you can stick around and take a look at the list below, or you can go browse the repository!

<!-- AI Wrappers -->
<details>
  <summary>
    <b style="color: #10a37f;"><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/html/gpt.svg" style="height: 24px; vertical-align: middle"> (Azure-) OpenAI API Wrappers</b>
    <hr/>
  </summary>

<!---
  Python Azure OpenAI Assistants Wrapper
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/AzureAssistantsWrapper' target='_blank' id='python-assistants-wrapper'><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/html/gpt.svg" style="height: 24px; vertical-align: middle"> Python Azure OpenAI Assistants Wrapper <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p1 %}{% include_relative Python/AzureAssistantsWrapper/README.md %}{% endcapture %}
    {{ p1 | markdownify }}
  </div>
  <a href="#python-assistants-wrapper">Back to Top</a>
</details>

<hr/>

<!---
  Python Azure OpenAI Dall-E Wrapper
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/DallEWrapper' target='_blank' id='python-dalle-wrapper'><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/html/gpt.svg" style="height: 24px; vertical-align: middle"> Python Azure OpenAI Dall-E Wrapper <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p1 %}{% include_relative Python/DallEWrapper/README.md %}{% endcapture %}
    {{ p1 | markdownify }}
  </div>
  <a href="#python-dalle-wrapper">Back to Top</a>
</details>

<hr/>

</details>

<!-- DEV Tools -->
<details>
  <summary>
    <b style="color: #ffffff;"><i class="fa-brands fa-dev"></i> Developer Tools</b>
    <hr/>
  </summary>
<!---
  Python Logger
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/Logger' target='_blank' id='python-logger'><i class="fa-solid fa-rectangle-list"></i> Python Logging Module <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p1 %}{% include_relative Python/Logger/README.md %}{% endcapture %}
    {{ p1 | markdownify }}
  </div>
  <a href="#python-logger">Back to Top</a>
</details>

<hr/>

<!---
  Python CSV Module
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/CSVImportExport' target='_blank' id='python-csv'><i class="fa-solid fa-file-csv"></i> Python CSV Module <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p1 %}{% include_relative Python/CSVImportExport/README.md %}{% endcapture %}
    {{ p1 | markdownify }}
  </div>
  <a href="#python-csv">Back to Top</a>
</details>

<hr/>

<!---
  Git config gen
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/GitConfigGenerator' target='_blank' id='git-conf-gen'><i class="fab fa-git-alt"></i> Git SSH Config Generator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p1 %}{% include_relative Python/GitConfigGenerator/README.md %}{% endcapture %}
    {{ p1 | markdownify }}
  </div>
  <a href="#git-conf-gen">Back to Top</a>
</details>

<hr/>
</details>

<!-- JAVA -->
<details>
  <summary>
  	<b style="color: #f89820;"><i class="fa-brands fa-java"></i> Java</b>
  	<hr/>
  </summary>
<!---
	File Transfer Tool
-->
<h3>
	<a href='https://github.com/leolion3/Simple-File-Transfer-PC' target='_blank' id='java-easy-file-transfer'><i class="fa-solid fa-file-arrow-up"></i> Easy File Transfer Tool (Cross-Platform) <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p13 %}{% include_relative Etc/Simple-File-Transfer-PC/README.md %}{% endcapture %}
	  {{ p13 | markdownify }}
  </div>
  <a href="#java-easy-file-transfer">Back to Top</a>
</details>

<hr/>
</details>

<details>
  <summary>
  	<b style="color: limegreen;"><i class="fab fa-python"></i> Python</b>
  	<hr/>
  </summary>
<!---
  File Transfer Tool
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/FileSender' target='_blank' id='file-transfer-ref'><img src="html/media/ptransfer/logo.webp" style="width: 24px; vertical-align: top;"> File Transfer Tool <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p3 %}{% include_relative Python/FileSender/README.md %}{% endcapture %}
    {{ p3 | markdownify }}
  </div>
  <a href="#file-transfer-ref">Back to Top</a>
</details>

<hr/>
<!---
  Finanzblick API Base
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/finanzblick' target='_blank' id='finanzblick-ref'><img src="https://play-lh.googleusercontent.com/ryukWLh6qbHhSK_e0zq59BXczSAYE2dVb1UCSWnLxEjTji5l_dXcw2qIpb7kZITqAOUD=w240-h480-rw" style="width: 24px; vertical-align: top;"> Finanzblick API Template <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p3 %}{% include_relative Python/finanzblick/README.md %}{% endcapture %}
    {{ p3 | markdownify }}
  </div>
  <a href="#finanzblick-ref">Back to Top</a>
</details>

<hr/>

<!---
  Gmail Permutator
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/GmailPermutationGenerator' target='_blank' id='gmail-permutator'><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="52 42 88 66" style="vertical-align: middle;"><path fill="#4285f4" d="M58 108h14V74L52 59v43c0 3.32 2.69 6 6 6"/><path fill="#34a853" d="M120 108h14c3.32 0 6-2.69 6-6V59l-20 15"/><path fill="#fbbc04" d="M120 48v26l20-15v-8c0-7.42-8.47-11.65-14.4-7.2"/><path fill="#ea4335" d="M72 74V48l24 18 24-18v26L96 92"/><path fill="#c5221f" d="M52 51v8l20 15V48l-5.6-4.2c-5.94-4.45-14.4-.22-14.4 7.2"/></svg> Gmail Permutation Generator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/GmailPermutationGenerator/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#gmail-permutator">Back to Top</a>
</details>
<hr/>
<!---
  ONOC Tools
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/ONOC' target='_blank' id='onoc-tools'><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/ONOC/media/pizza_bot.jpg" style="height: 24px; vertical-align: top"> ONOC Tools <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/ONOC/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#onoc-tools">Back to Top</a>
</details>
<hr/>
<!---
  Red Alert Telegram Notifier
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/RedAlert' target='_blank' id='red-alert'><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/html/red-alert.png" style="height: 24px; vertical-align: middle"> Israel Red-Alert Telegram Notifier <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/RedAlert/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#red-alert">Back to Top</a>
</details>
<hr/>
<!---
  Mensa Food Telegram Notifier
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/UniMensa' target='_blank' id='uni-mensa'><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/html/mensa.webp" style="height: 24px; vertical-align: middle"> Uni Bremen Mensa-Food Telegram Notifier <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p1 %}{% include_relative Python/UniMensa/README.md %}{% endcapture %}
    {{ p1 | markdownify }}
  </div>
  <a href="#uni-mensa">Back to Top</a>
</details>
<hr/>
<!---
  DL Envelope Generator
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/Envelope' target='_blank' id='dl-generator'><i class="fa-solid fa-envelope"></i> DL Envelope Printable Generator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/Envelope/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#dl-generator">Back to Top</a>
</details>
<hr/>
<!---
  Earthquake Notifier
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/EarthquakeMonitor' target='_blank' id='earthquake-notifier'><i class="fa-solid fa-house-chimney-crack"></i> Earthquake Monitor w/ Telegram Notifications <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/EarthquakeMonitor/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#earthquake-notifier">Back to Top</a>
</details>

<hr/>
<!---
  Trash Calendar
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/TrashCalendar' target='_blank' id='trash-calendar'><i class="fa-solid fa-trash"></i> Telegram Trash Calendar Renderer <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/TrashCalendar/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#trash-calendar">Back to Top</a>
</details>

<hr/>
<!---
  Trash Schedule Notifier
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/TrashScheduleNotifier' target='_blank' id='trash-notifier'><i class="fa-solid fa-trash"></i> Telegram Trash Schedule Notifier <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/TrashScheduleNotifier/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#trash-notifier">Back to Top</a>
</details>

<hr/>
<!---
  iCal Generator
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/iCalGenerator' target='_blank' id='ical-generator'><i class="fa-solid fa-calendar-days"></i> iCal File Generator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/iCalGenerator/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#ical-generator">Back to Top</a>
</details>

<hr/>
<!---
  Canary Tracker
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/CanaryTrackingPixel' target='_blank' id='canary-tracking-pixel'><i class="fa-solid fa-magnifying-glass"></i> Canary Tracking Pixel <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/CanaryTrackingPixel/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#canary-tracking-pixel">Back to Top</a>
</details>

<hr/>
<!---
	StudIP REST API
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/StudIP_REST_API' target='_blank' id='studip-rest-api'><img src="https://raw.githubusercontent.com/leolion3/Portfolio/master/html/studip.png" style="height: 24px; vertical-align: middle"> StudIP REST API <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p21 %}{% include_relative Python/StudIP_REST_API/README.md %}{% endcapture %}
	  {{ p21 | markdownify }}
  </div>
  <a href="#studip-rest-api">Back to Top</a>
</details>

<hr/>
<!---
  StreamTogether
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/StreamTogether' target='_blank' id='stream-together'><i class="fa-solid fa-film"></i> StreamTogether (Synchronous Streaming) <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/StreamTogether/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#stream-together">Back to Top</a>
</details>

<hr/>
<!---
	Python MiniHTTP Server
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/MiniHTTPServer' target='_blank' id='mini-http-server'><i class="fa-solid fa-server"></i> MiniHTTPServer (Minimal HTTP Server) <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p21 %}{% include_relative Python/MiniHTTPServer/README.md %}{% endcapture %}
	  {{ p21 | markdownify }}
  </div>
  <a href="#mini-http-server">Back to Top</a>
</details>

<hr/>
<!---
  Duplicate file deleter
-->
<h3>
  <a href='https://github.com/leolion3/Portfolio/tree/master/Python/DuplicateFileDetector' target='_blank' id='duplicate-file-detector'><i class="fa-solid fa-file"></i> Duplicate File Deleter <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
    <b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
    {% capture p21 %}{% include_relative Python/DuplicateFileDetector/README.md %}{% endcapture %}
    {{ p21 | markdownify }}
  </div>
  <a href="#duplicate-file-detector">Back to Top</a>
</details>

<hr/>
<!---
	KeepBusy
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/KeepBusy' target='_blank' id='keep-busy'><i class="fa-solid fa-computer-mouse"></i> KeepBusy Mouse Mover <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p21 %}{% include_relative Python/KeepBusy/README.md %}{% endcapture %}
	  {{ p21 | markdownify }}
  </div>
  <a href="#keep-busy">Back to Top</a>
</details>

<hr/>
<!---
	Yearly Investment Yield Calculator
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/YearlyYieldCalculator' target='_blank' id='investment-yield-ref'><i class="fa-solid fa-money-bill-trend-up"></i> Investment Yield Calculator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p13 %}{% include_relative Python/YearlyYieldCalculator/README.md %}{% endcapture %}
	  {{ p13 | markdownify }}
  </div>
  <a href="#investment-yield-ref">Back to Top</a>
</details>

<hr/>
<!---
	Bank Balance Calculator
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/NetworthCalculator' target='_blank' id='bank-balance-ref'><i class="fa-solid fa-money-check-dollar"></i> Bank-Balance Calculator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p1 %}{% include_relative Python/NetworthCalculator/README.md %}{% endcapture %}
	  {{ p1 | markdownify }}
  </div>
  <a href="#bank-balance-ref">Back to Top</a>
</details>

<hr/>
<!---
	Password Vault
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/PasswordVault" target="_blank" rel="noopener noreferrer" id='password-vault-ref'><i class="fa-solid fa-lock"></i> Password Vault <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p2 %}{% include_relative Python/PasswordVault/README.md %}{% endcapture %}
	  {{ p2 | markdownify }}
  </div>
  <a href="#password-vault-ref">Back to Top</a>
</details>

<hr/>

<!---
	Password Transfer Tool
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/PasswordUtils' target='_blank' id='password-transfer-ref'><i class="fa-solid fa-key"></i> Password Transfer Tool <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p20 %}{% include_relative Python/PasswordUtils/README.md %}{% endcapture %}
	  {{ p20 | markdownify }}
  </div>
  <a href="#password-transfer-ref">Back to Top</a>
</details>

<hr/>

<!---
	Mass Git Diff
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/GitDiff' target='_blank' id='massgdiff-ref'><i class="fa-brands fa-git-alt"></i> Mass Git Diff <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p20 %}{% include_relative Python/GitDiff/README.md %}{% endcapture %}
	  {{ p20 | markdownify }}
  </div>
  <a href="#massgdiff-ref">Back to Top</a>
</details>

<hr/>

<!---
	Spotify Module
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/SpotifyAPI' target='_blank' id='spotify-api-ref'><i class="fa-brands fa-spotify"></i> Spotify API Modules <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p20 %}{% include_relative Python/SpotifyAPI/README.md %}{% endcapture %}
	  {{ p20 | markdownify }}
  </div>
  <a href="#spotify-api-ref">Back to Top</a>
</details>

<hr/>

<!---
	Python Ethermine Ticker
-->
<h3>
	<a href='https://github.com/leolion3/Portfolio/tree/master/Python/Ethermine' target='_blank' id='ethermine-ticker-ref'><i class="fa-brands fa-bitcoin"></i> Ethermine Ticker <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p4 %}{% include_relative Python/Ethermine/README.md %}{% endcapture %}
	  {{ p4 | markdownify }}
  </div>
  <a href="#ethermine-ticker-ref">Back to Top</a>
</details>

<hr/>
<!---
	Monoalphabetic Decypherer
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/MonoalphabeticDecypherer" target="_blank" rel="noopener noreferrer" id='monoalphabetic-decypherer-ref'><i class="fa-solid fa-language"></i> Monoalphabetic Decypherer <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p5 %}{% include_relative Python/MonoalphabeticDecypherer/README.md %}{% endcapture %}
	  {{ p5 | markdownify }}
  </div>
  <a href="#monoalphabetic-decypherer-ref">Back to Top</a>
</details>

<hr/>
<!---
	Reverse Shell
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/PythonReverseShell" target="_blank" rel="noopener noreferrer" id='py-revshell-ref'><i class="fa-solid fa-terminal"></i> Reverse Shell <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p6 %}{% include_relative Python/PythonReverseShell/README.md %}{% endcapture %}
	  {{ p6 | markdownify }}
  </div>
  <a href="#py-revshell-ref">Back to Top</a>
</details>

<hr/>
<!---
	Markdown Text Editor
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/Markdown" target="_blank" rel="noopener noreferrer" id='py-texteditor-ref'><i class="fa-solid fa-newspaper"></i> Markdown/Text Editor <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p7 %}{% include_relative Python/Markdown/README.md %}{% endcapture %}
	  {{ p7 | markdownify }}
  </div>
  <a href="#py-texteditor-ref">Back to Top</a>
</details>

<hr/>
<!---
	Youtube to MP3
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/YouTube" target="_blank" rel="noopener noreferrer" id='yt-downloader-ref'><i class="fa-brands fa-youtube"></i> YouTube MP3 Downloader <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p8 %}{% include_relative Python/YouTube/README.md %}{% endcapture %}
	  {{ p8 | markdownify }}
  </div>
  <a href="#yt-downloader-ref">Back to Top</a>
</details>

<hr/>
<!---
	Revshell Payload Generator
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/ShellGenerator" target="_blank" rel="noopener noreferrer" id='powershell-revshell-ref'><i class="fa-brands fa-windows"></i> Powershell TCP Reverse Shell Generator <i class="fa fa-external-link"></i></a>
</h3>
	
<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p9 %}{% include_relative Python/ShellGenerator/README.md %}{% endcapture %}
	  {{ p9 | markdownify }}
  </div>
  <a href="#powershell-revshell-ref">Back to Top</a>
</details>
<hr/>

<!---
	Chat spammer
-->
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/ChatSpammer" target="_blank" rel="noopener noreferrer" id='py-chatspammer-ref'><i class="fa-regular fa-comments"></i> Chat Spammer <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p16 %}{% include_relative Python/ChatSpammer/README.md %}{% endcapture %}
	  {{ p16 | markdownify }}
  </div>
  <a href="#py-chatspammer-ref">Back to Top</a>
</details>

<hr/>

<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Python/Introduction" target="_blank" rel="noopener noreferrer" id='python-introduction-ref'><i class="fa-brands fa-python"></i> Python Introduction <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p10 %}{% include_relative Python/Introduction/README.md %}{% endcapture %}
	  {{ p10 | markdownify }}
  </div>
  <a href="#python-introduction-ref">Back to Top</a>
</details>
<hr/>
</details>

<details>
  <summary>
  	<b style="color: cyan;"><i class="fa-brands fa-windows"></i> Windows Terminal/Batchfile</b>
  	<hr/>
  </summary>
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/Powershell/Customization" target="_blank" rel="noopener noreferrer" id='wt-customization'><i class="fa-solid fa-terminal"></i> Windows Terminal Customization <i class="fa fa-external-link"></i></a>
</h3>
	<details>
		<summary>
			<b style="color: purple;">Click to view Details</b>
		</summary>
		<div>
			{% capture p11 %}{% include_relative Powershell/Customization/README.md %}{% endcapture %}
			{{ p11 | markdownify }}
		</div>
		<a href="#wt-customization">Back to Top</a>
	</details>
<hr/>
<h3>
	<a href="https://github.com/leolion3/Portfolio/tree/master/CustomCommands" target="_blank" rel="noopener noreferrer" id='custom-windows-commands'><i class="fa-brands fa-git-alt"></i> Custom Windows Commands and Git Shortcuts <i class="fa fa-external-link"></i></a>
</h3>
<details>
		<summary>
			<b style="color: purple;">Click to view Details</b>
		</summary>
		<div>
			{% capture p12 %}{% include_relative CustomCommands/README.md %}{% endcapture %}
			{{ p12 | markdownify }}
		</div>
		<a href="#custom-windows-commands">Back to Top</a>
	</details>
<hr/>

</details>

<details>
  <summary>
  	<b style="color: white;"><i class="fa-brands fa-linux"></i> Linux/Bash</b>
  	<hr/>
  </summary>
  <h3>
		<a href="https://github.com/leolion3/Portfolio/tree/master/Linux/Customization/Oh-My-Zsh" target="_blank" rel="noopener noreferrer" id='terminal-customization'><i class="fa-solid fa-terminal"></i> Customize Terminal with Oh-My-Zsh <i class="fa fa-external-link"></i></a>
	</h3>
	<details>
	<summary>
		<b style="color: purple;">Click to view Details</b>
	</summary>
		<div>
			{% capture p10 %}{% include_relative Linux/Customization/Oh-My-Zsh/README.md %}{% endcapture %}
			{{ p10 | markdownify }}
		</div>
		<a href="#terminal-customization">Back to Top</a>
	</details>
	<hr/>
	<h3>
		<a href="https://github.com/leolion3/Portfolio/tree/master/Linux/CustomCommands" target="_blank" rel="noopener noreferrer" id='linux-commands'><i class="fa-brands fa-git-alt"></i> Custom Linux/MacOS Commands <i class="fa fa-external-link"></i></a>
	</h3>
	<details>
	<summary>
		<b style="color: purple;">Click to view Details</b>
	</summary>
		<div>
			{% capture p10 %}{% include_relative Linux/CustomCommands/README.md %}{% endcapture %}
			{{ p10 | markdownify }}
		</div>
		<a href="#linux-commands">Back to Top</a>
	</details>
	<hr/>

</details>

<details>
  <summary>
  	<b style="color: yellow;"><i class="fa-solid fa-ellipsis"></i> Etc</b>
  	<hr/>
  </summary>
<h3>
	<a href="https://gist.github.com/leolion3/ccf654ab60c8e110c65ef948da6af461" target="_blank" rel="noopener noreferrer" id="dlu"><img src="https://cdn2.steamgriddb.com/logo/1c8dcf919f8a604f3a488b0e4b0f1420.png" style="height: 18px"> DLU Lego Universe Server Setup <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
			{% capture p15 %}
				{% include_relative Etc/DLU/1.DLUSetup.md %}{% endcapture %}
			{{ p15 | markdownify }}
	</div>
  <a href="#dlu">Back to Top</a>
</details>
<hr/>
</details>

<details>
  <summary>
    <b style="color: coral;"><i class="fa-solid fa-calendar-day"></i> Events</b>
    <hr/>
  </summary>
  <h3 id="advent-of-code">
    <i class="fa-solid fa-tree"></i> Advent of Code
  </h3>
  <details>
    <summary>
      <b style="color: purple;">Click to view Details</b>
    </summary>
    <div>
        <img src="https://github.com/leolion3/advent-of-code-2023/assets/45939246/1121e7ce-c1cd-4b94-9f5d-f7ff8a5c65d9" alt="Banner from https://blog.pythondiscord.com/advent-of-code-2020/" />
    </div>
    <h4>
      <a href="https://github.com/leolion3/advent-of-code-2024" target="_blank" rel="noopener noreferrer" id="aoc2024"><i class="fa-solid fa-tree"></i> Advent of Code 2024 (Python) <i class="fa fa-external-link"></i></a>
    </h4>
    <h4>
      <a href="https://github.com/leolion3/advent-of-code-2023" target="_blank" rel="noopener noreferrer" id="aoc2023"><i class="fa-solid fa-tree"></i> Advent of Code 2023 (Python) <i class="fa fa-external-link"></i></a>
    </h4>
    <a href="#advent-of-code">Back to Top</a>
  </details>
  <hr/>
</details>

<h1 id="publications">Publications</h1>

<h2 id="trash-separation">Trash Separation Using AI (Prototype paper)</h2>

<img src="html/robot-arm.png" alt="robot arm https://www.pngitem.com/middle/ihmmoJx_robot-machine-technology-robot-arm-3d-camera-hd/"/>

A paper proposing a robot-arm trash separation approach, applicable on a large-scale using IoT Devices and public networks.

*The paper can be found <a href="https://leolion3.github.io/University_Stuff/Publications/trash-separation.pdf">here <i class="fa fa-external-link"></i></a>*

<h2 id="bachelor-robots">B-More-Human: Dynamic Cheering Reactions for humanoid Football-Robots (Bachelor Thesis)</h2>

<img src="html/b-human.jpg"/>

The B-Human football robots were incapable of showing emotions during RoboCup games. This has been changed. The process of doing so required various tweaks dozens of code-fragments throughout the B-Human framework and the introduction of various new mechanisms. 

**The thesis can be found <a href="https://leolion3.github.io/University_Stuff/Publications/BA_B-More-Human_leonard_haddad_SoSe22.pdf">here <i class="fa fa-external-link"></i></a>**

**The thesis was graded with a 1.3 (an A if an A+ is the highest possible grade).**

**\* The professors' assessments can be provided upon request. Long live open source and free access to information!**

<p id="dancing-robots">Check out the dancing robots below!</p>

<details>
  <summary>
  	<b style="color: purple;">See some dancing robots!</b>
  </summary>
  <div>
			{% include youtube.html id="zWgDolhWsEk" %}
			{% include youtube.html id="-_vlZ9nGPxQ" %}
			{% include youtube.html id="d9McmzbOyaA" %}
			{% include youtube.html id="adCF4C8HlTs" %}
			{% include youtube.html id="NRGpaM_M4x8" %}
			{% include youtube.html id="QJQhpZUD9jg" %}
			{% include youtube.html id="C-O1FXAt7Ek" %}
			{% include youtube.html id="yvMbB3C7fME" %}
	</div>
  <a href="#dancing-robots">Back to Top</a>
</details>

<br>

<h2 id="iug">Cyberbullying - Causes, Appearances and Prevention</h2>

<img src="https://github.com/leolion3/University_Stuff/raw/master/Publications/data/cyberbullying.png"/>

Cyberbullying is one of the 21st century's new demons, where due to technology it is easier than ever to bully someone without being within their physical vicinity.

In this homework for the "Informatik und Gesellschaft" (literally translated "IT and Society") we dive into the topic of cyberbullying, display some of its root causes and manifestations and then describe ways of preventing it.

This publication can be found <a href="https://leolion3.github.io/University_Stuff/Publications/IuG.pdf" target="_blank">here <i class="fa fa-external-link"></i></a>

It was graded with a 1.3 and the assessment can be provided upon request.

*If you are suffering from cyberbullying, reach out to either an adult who is close to you, or to your national cyberbullying helpline! If you know someone suffering from cyberbullying, reach out and offer help and/or contact the local authorities!*

---

<h1 id="me-etc">More from Me</h1>

### Teespring Merch

<a href='https://leolions-merch.creator-spring.com/' target='_blank'>
	<img src='html/teespring.png' width='100%'/>
</a>

Check out the various cool merch on my <a href='https://leolions-merch.creator-spring.com/' target='_blank'>Teespring store <i class="fa fa-external-link"></i></a>

---

<!-- Google Play -->
<h1 id="google-play">
  <img src="https://www.gstatic.com/android/market_images/web/play_prism_hlock_2x.png" width="168" height="35"/>
</h1>

Check out my Google Play Apps!

**(\*) Note: Google has taken my old developer account offline for being "inactive". The apps "Sharky" and "Semesterplaner" are temporarily unavailable. The "Easy File Transfer" can be downloaded from its Github link below, while the "Password Generator" needs to be built from source. The apps will be available again soon (on a different app store and maybe on Google Play again...). Self-hosted alternatives are in the works.**

<ul>
<!-- File transfer tool -->
  <li>
    <h2>
      <img src="html/media/ptransfer/logo.webp" style="vertical-align: middle;" width="24" height="24"> Open Source Easy File Transfer <a href="https://play.google.com/store/apps/details?id=software.isratech.filetransferos" target="_blank">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
    <img src="html/media/ptransfer/demo-1.webp" width="17%">
    <img src="html/media/ptransfer/demo-2.webp" width="17%">
    <img src="html/media/ptransfer/demo-3.webp" width="17%">
    <img src="html/media/ptransfer/demo-4.webp" width="17%">
    <p>Tired of sending files back and forth through Whatsapp, just to transfer them from your PC to your Phone and vice versa? Would you like an AirDrop equivalent for Android and Windows? Well, this is it! Simply pick the file you want to send, and let the receiving device connect to your device and viola!</p>
    <p>This is a companion app for the <a href='https://github.com/leolion3/Portfolio/tree/master/Python/FileSender' target='_blank'>Python File Transfer Tool <i class="fa fa-external-link"></i></a> found <a href="#file-transfer-ref">above</a>.<br>A Java graphical variant (cross-platform) can be found <a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Simple-File-Transfer-PC">here <i class="fa fa-external-link"></i></a></p>
    <p>The source code can be found on <a href="https://github.com/leolion3/Simple-File-Transferer-Android" target="_blank">Github <i class="fa fa-external-link"></i></a></p>
    	<p>
      <details id="simple-file-transfer-android">
      <summary>
	<b style="color:#b5e853">Simple File Transfer Android</b>
      </summary>
	  <div>
		{% capture p21 %}{% include_relative Etc/Simple-File-Transferer-Android/README.md %}{% endcapture %}
		  {{ p21 | markdownify }}
	  </div>
	  <a href="#simple-file-transfer-android">Back to Top</a>
      </details>
      <details id="simple-file-transfer-pc-2">
      <summary>
	<b style="color:#b5e853">Simple File Transfer PC</b>
      </summary>
	<div>
		{% capture p21 %}{% include_relative Etc/Simple-File-Transfer-PC/README.md %}{% endcapture %}
		  {{ p21 | markdownify }}
	</div>
	<a href="#simple-file-transfer-pc-2">Back to Top</a>
      </details>
    </p>

  <p><strong>List of available Distros:</strong></p>
  <ul style="margin-bottom: 10px;">
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Simple-File-Transfer-PC/releases"><i class="fa-solid fa-desktop"></i> PC Release <i class="fa fa-external-link"></i></a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://play.google.com/store/apps/details?id=software.isratech.filetransferos"><i class="fa-solid fa-mobile"></i> Android App <i class="fa fa-external-link"></i></a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Portfolio/tree/master/Python/FileSender"><i class="fa-solid fa-terminal"></i> Python CLI Tool <i class="fa fa-external-link"></i></a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Simple-File-Transfer-PC"><i class="fa-solid fa-code"></i> PC Source <i class="fa fa-external-link"></i></a></li>
    <li><a href="https://github.com/leolion3/Simple-File-Transferer-Android" target="_blank"><i class="fa-solid fa-code"></i> Android Source <i class="fa fa-external-link"></i></a></li>
  </ul>
  </li>
<!-- Sharky -->
  <li>
    <h2>
      <img src="html/media/sharky/logo.webp" style="vertical-align: middle;" width="24" height="24"> Sharky the hungry Sharkfish Game <a target="_blank" rel="noopener noreferrer" href="https://play.google.com/store/apps/details?id=com.SpaceAhoy.Sharky">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
    <img src="html/media/sharky/demo.webp" width="85%">
    <p>Sharky is very Hungry! Help by feeding him as many fish as you can, but watch out for those nasty harpoons!<br>Sharky is a family-friendly game designed for all ages. Furthermore it is completely FREE<br> and AD-FREE. Collect coins to unlock powerups and new skins, and get that highscore!<br>Sharky is a great time killer for your free time as well!<br /> Be it while waiting at the airport, or in the subway, sharky can played anywhere at any given time!<br /> What are you still waiting for? Get Sharky today!
    </p>
  </li>
<!-- Semesterplaner -->
  <li>
    <h2>
      <img src="html/media/planer/logo.webp" style="vertical-align: middle;" width="24" height="24"> SemesterPlaner - Plan your Schedule! <a target="_blank" rel="noopener noreferrer" href="https://play.google.com/store/apps/details?id=com.spaceahoy.semesterplaner">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
      <img src="html/media/planer/demo-1.webp" width="17%">
      <img src="html/media/planer/demo-2.webp" width="17%">
      <img src="html/media/planer/demo-3.webp" width="17%">
      <img src="html/media/planer/demo-4.webp" width="17%">
      <p>Tired of using the same old photoshop template for your semester schedule?<br>Why not automate your schedule creation today using Semester Planer!<br>Just select your work days, how long you work per day and hit that button!<br>Semester Planer will automatically create you a schedule table that can be filled,<br />edited and exported to PNG at any given time!<br> Stop wasting your time and use Semester Planer today!</p>
  </li>
<!-- Password Generator -->
  <li>
    <h2>
      <img src="html/media/genpass/logo.webp" style="vertical-align: middle;" width="24" height="24"> Open-Source Password Generator App <a target="_blank" rel="noopener noreferrer" href="https://play.google.com/store/apps/details?id=processing.test.password_generator">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
    <img src="html/media/genpass/demo-1.webp" width="17%">
    <img src="html/media/genpass/demo-2.webp" width="17%">
    <img src="html/media/genpass/demo-3.webp" width="17%">
    <img src="html/media/genpass/demo-4.webp" width="17%">
    <p>Passwords can be a real hustle, especially when you have a thousand accounts for a gazillion different websites...<br>There are some great password generators out there, however how can you ever really trust such a service if it is not open sourced?<br />Stop worrying about your passwords today, with this Free, Open-Source Password Generator!<br>Password Generator is completely FREE and AD-FREE, it works 100% offline an creates you a password in seconds!</p>
    <p>The source code can be found on <a href="https://github.com/leolion3/App-Tutorial/tree/master/Password_Generator" target="_blank">Github <i class="fa fa-external-link"></i></a></p>
  </li>
</ul>

<hr/>

<h1 id="contact-section">Contact</h1>

You can contact me using my <a href="mailto:s_xsipo6@uni-bremen.de">email address <i class="fa fa-envelope"></i></a> or on Instagram <a target="_blank" rel="noopener noreferrer" href="https://www.instagram.com/xleolion3">@xleolion3 <i class="fa fa-external-link"></i></a>
