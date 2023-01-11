<link rel="stylesheet" type="text/css" href="html/style.css"/>
<div class="tg-wrap"><table class="tg">
<thead>
  <tr>
    <th class="tg-5oyt"><a href="#welcome" style="color:#b5e853; text-decoration: none;">Welcome</a></th>
    <th class="tg-5oyt"><a href="#my-resume" style="color:#b5e853; text-decoration: none;">Resume</a></th>
    <th class="tg-5oyt"><a href="#my-tools" style="color:#b5e853; text-decoration: none;">Tools</a></th>
    <th class="tg-5oyt"><a href="#publications" style="color:#b5e853; text-decoration: none;">Publications</a></th>
    <th class="tg-5oyt"><a href="#me-etc" style="color:#b5e853; text-decoration: none;">More from me</a></th>
    <th class="tg-5oyt"><a href="#google-play" style="color:#b5e853; text-decoration: none;">Google Play</a></th>
    <th class="tg-5oyt"><a href="#contact-section" style="color:#b5e853; text-decoration: none;">Contact</a></th>
  </tr>
</thead>
</table></div><p></p>

<h2 id="welcome">Welcome, friend</h2>

On this website you can find a bunch of useful tools, both for your personal workstation, as well as for your professional life.
This website also serves as my Portfolio, so if you're looking to hire me, or are interested in filing a development request, don't hesitate to use the <a style="color:#b5e853; text-decoration: none;" href="#contact-section">contact section below</a>.

*For resources to help you with University subjects, check out my other <a style="color:#b5e853; text-decoration: none;" href="https://uni.leolion.tk/" target="_blank">website <i class="fa fa-external-link"></i></a>*

**All tools provided on this website are free to use and change, misuse however, is prohibited. Any damage caused by these tools, in addition to violations of local restrictions, are your own problem, not mine.** 

---

<h1 id="my-resume">Who am I?</h1>

{% capture p1 %}{% include_relative Etc/leolion3/README.md %}{% endcapture %}
{{ p1 | markdownify }}

<p>Wanna know if you should hire me or need a software developed? Check out my interactive digital resume below (or <a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/blob/master/CV/' target='_blank' id='digital-resume'>here</a>).</p>

<details>
  <summary>
  	<b style="color: purple;">Show Resume</b>
  </summary>
  <div>
  	{% capture p21 %}{% include_relative CV/README.md %}{% endcapture %}
	  {{ p21 | markdownify }}
  </div>
</details>

---

<h1 id="my-tools">Ok, so what's on the menu?</h1>

Well you can stick around and take a look at the list below, or you can go browse the repository!

<details>
  <summary>
  	<b style="color: limegreen;">Python</b>
  	<hr/>
  </summary>
<!---
	Python MiniHTTP Server
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/MiniHTTPServer' target='_blank' id='mini-http-server'>MiniHTTPServer (Minimal HTTP Server) <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p21 %}{% include_relative Python/MiniHTTPServer/README.md %}{% endcapture %}
	  {{ p21 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#mini-http-server">Back to Top</a>
</details>

<hr/>
<!---
	Yearly Investment Yield Calculator
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/YearlyYieldCalculator' target='_blank' id='investment-yield-ref'>Investment Yield Calculator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p13 %}{% include_relative Python/YearlyYieldCalculator/README.md %}{% endcapture %}
	  {{ p13 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#investment-yield-ref">Back to Top</a>
</details>

<hr/>
<!---
	Bank Balance Calculator
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/NetworthCalculator' target='_blank' id='bank-balance-ref'>Bank-Balance Calculator <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p1 %}{% include_relative Python/NetworthCalculator/README.md %}{% endcapture %}
	  {{ p1 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#bank-balance-ref">Back to Top</a>
</details>

<hr/>
<!---
	Password Vault
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/PasswordVault" target="_blank" id='password-vault-ref'>Password Vault <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p2 %}{% include_relative Python/PasswordVault/README.md %}{% endcapture %}
	  {{ p2 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#password-vault-ref">Back to Top</a>
</details>

<hr/>

<!---
	File Transfer Tool
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/FileSender' target='_blank' id='file-transfer-ref'>File Transfer Tool <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p3 %}{% include_relative Python/FileSender/README.md %}{% endcapture %}
	  {{ p3 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#file-transfer-ref">Back to Top</a>
</details>

<hr/>

<!---
	Password Transfer Tool
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/PasswordUtils' target='_blank' id='password-transfer-ref'>Password Transfer Tool <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p20 %}{% include_relative Python/PasswordUtils/README.md %}{% endcapture %}
	  {{ p20 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#password-transfer-ref">Back to Top</a>
</details>

<hr/>

<!---
	Spotify Module
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/SpotifyAPI' target='_blank' id='spotify-api-ref'>Spotify API Modules <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p20 %}{% include_relative Python/SpotifyAPI/README.md %}{% endcapture %}
	  {{ p20 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#spotify-api-ref">Back to Top</a>
</details>

<hr/>

<!---
	Python Ethermine Ticker
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/Ethermine' target='_blank' id='ethermine-ticker-ref'>Ethermine Ticker <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p4 %}{% include_relative Python/Ethermine/README.md %}{% endcapture %}
	  {{ p4 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#ethermine-ticker-ref">Back to Top</a>
</details>

<hr/>
<!---
	Monoalphabetic Decypherer
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/MonoalphabeticDecypherer" target="_blank" id='monoalphabetic-decypherer-ref'>Monoalphabetic Decypherer <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p5 %}{% include_relative Python/MonoalphabeticDecypherer/README.md %}{% endcapture %}
	  {{ p5 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#monoalphabetic-decypherer-ref">Back to Top</a>
</details>

<hr/>
<!---
	Reverse Shell
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/PythonReverseShell" target="_blank" id='py-revshell-ref'>Reverse Shell <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p6 %}{% include_relative Python/PythonReverseShell/README.md %}{% endcapture %}
	  {{ p6 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#py-revshell-ref">Back to Top</a>
</details>

<hr/>
<!---
	Markdown Text Editor
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/Markdown" target="_blank" id='py-texteditor-ref'>Markdown/Text Editor <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p7 %}{% include_relative Python/Markdown/README.md %}{% endcapture %}
	  {{ p7 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#py-texteditor-ref">Back to Top</a>
</details>

<hr/>
<!---
	Youtube to MP3
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/YouTube" target="_blank" id='yt-downloader-ref'>YouTube MP3 Downloader <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p8 %}{% include_relative Python/YouTube/README.md %}{% endcapture %}
	  {{ p8 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#yt-downloader-ref">Back to Top</a>
</details>

<hr/>
<!---
	Revshell Payload Generator
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/ShellGenerator" target="_blank" id='powershell-revshell-ref'>Powershell TCP Reverse Shell Generator <i class="fa fa-external-link"></i></a>
</h3>
	
<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p9 %}{% include_relative Python/ShellGenerator/README.md %}{% endcapture %}
	  {{ p9 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#powershell-revshell-ref">Back to Top</a>
</details>
<hr/>

<!---
	Chat spammer
-->
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/ChatSpammer" target="_blank" id='py-chatspammer-ref'>Chat Spammer <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p16 %}{% include_relative Python/ChatSpammer/README.md %}{% endcapture %}
	  {{ p16 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#py-chatspammer-ref">Back to Top</a>
</details>

<hr/>

<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Python/Introduction" target="_blank" id='python-introduction-ref'>Python Introduction <i class="fa fa-external-link"></i></a>
</h3>

<details>
  <summary>
  	<b style="color: purple;">Click to view Details</b>
  </summary>
  <div>
  	{% capture p10 %}{% include_relative Python/Introduction/README.md %}{% endcapture %}
	  {{ p10 | markdownify }}
  </div>
  <a style="color:#b5e853; text-decoration: none;" href="#python-introduction-ref">Back to Top</a>
</details>
<hr/>
</details>

<details>
  <summary>
  	<b style="color: cyan;">Windows Terminal/Batchfile</b>
  	<hr/>
  </summary>
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Powershell/Customization" target="_blank" id='wt-customization'>Windows Terminal Customization <i class="fa fa-external-link"></i></a>
</h3>
	<details>
		<summary>
			<b style="color: purple;">Click to view Details</b>
		</summary>
		<div>
			{% capture p11 %}{% include_relative Powershell/Customization/README.md %}{% endcapture %}
			{{ p11 | markdownify }}
		</div>
		<a style="color:#b5e853; text-decoration: none;" href="#wt-customization">Back to Top</a>
	</details>
<hr/>
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/CustomCommands" target="_blank" id='custom-commands'>Custom Windows Commands and Git Shortcuts <i class="fa fa-external-link"></i></a>
</h3>
<details>
		<summary>
			<b style="color: purple;">Click to view Details</b>
		</summary>
		<div>
			{% capture p12 %}{% include_relative CustomCommands/README.md %}{% endcapture %}
			{{ p12 | markdownify }}
		</div>
		<a style="color:#b5e853; text-decoration: none;" href="#custom-commands">Back to Top</a>
	</details>
<hr/>

</details>

<details>
  <summary>
  	<b style="color: orange;">Linux/Bash</b>
  	<hr/>
  </summary>
  <h3>
		<a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/Portfolio/tree/master/Linux/Customization/Oh-My-Zsh" target="_blank" id='terminal-customization'>Customize Terminal with Oh-My-Zsh <i class="fa fa-external-link"></i></a>
	</h3>
	<details>
	<summary>
		<b style="color: purple;">Click to view Details</b>
	</summary>
		<div>
			{% capture p10 %}{% include_relative Linux/Customization/Oh-My-Zsh/README.md %}{% endcapture %}
			{{ p10 | markdownify }}
		</div>
		<a style="color:#b5e853; text-decoration: none;" href="#terminal-customization">Back to Top</a>
	</details>
	<hr/>

</details>

<details>
  <summary>
  	<b style="color: yellow;">Etc</b>
  	<hr/>
  </summary>
<h3>
	<a style="color:#b5e853; text-decoration: none;" href="https://gist.github.com/leolion3/ccf654ab60c8e110c65ef948da6af461" target="_blank" id="dlu">DLU Lego Universe Server Setup <i class="fa fa-external-link"></i></a>
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
  <a style="color:#b5e853; text-decoration: none;" href="#dlu">Back to Top</a>
</details>
<hr/>
</details>

<h1 id="publications">Publications</h1>

<h2 id="bachelor-robots">B-More-Human: Dynamic Cheering Reactions for humanoid Football-Robots (Bachelor Thesis)</h2>

<img src="html/b-human.jpg"/>

The B-Human football robots were incapable of showing emotions during RoboCup games. This has been changed. The process of doing so required various tweaks dozens of code-fragments throughout the B-Human framework and the introduction of various new mechanisms. 

**The thesis can be found <a style="color:#b5e853; text-decoration: none;" href="https://leolion3.github.io/University_Stuff/Publications/BA_B-More-Human_leonard_haddad_SoSe22.pdf">here <i class="fa fa-external-link"></i></a>**

**The thesis was graded with a 1.3 (an A if an A+ is the highest possible grade).**

**\* The professors' assessments can be provided upon request. Long live upon source and free access to information!**

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
  <a style="color:#b5e853; text-decoration: none;" href="#dancing-robots">Back to Top</a>
</details>

<br>

<h2 id="iug">Cyberbullying - Causes, Appearances and Prevention</h2>

<img src="https://github.com/leolion3/University_Stuff/raw/master/Publications/data/cyberbullying.png"/>

Cyberbullying is one of the 21st century's new demons, where due to technology it is easier than ever to bully someone without being within their physical vicinity.

In this homework for the "Informatik und Gesellschaft" (literally translated "IT and Society") we dive into the topic of cyberbullying, display some of its root causes and manifestations and then describe ways of preventing it.

This publication can be found <a style="color:#b5e853; text-decoration: none;" href="https://leolion3.github.io/University_Stuff/Publications/IuG.pdf">here <i class="fa fa-external-link"></i></a>

It was graded with a 1.3 and the assessment can be provided upon request.

*If you are suffering from cyberbullying, reach out to either an adult who is close to you, or to your national cyberbullying helpline! If you know someone suffering from cyberbullying, reach out and offer help and/or contact the local authorities!*

---

<h1 id="me-etc">More from Me</h1>

### Teespring Merch

<a style="color:#b5e853; text-decoration: none;" href='https://leolions-merch.creator-spring.com/' target='_blank'>
	<img src='html/teespring.png' width='100%'/>
</a>

Check out the various cool merch on my <a style="color:#b5e853; text-decoration: none;" href='https://leolions-merch.creator-spring.com/' target='_blank'>Teespring store <i class="fa fa-external-link"></i></a>

---

<!-- Google Play -->
<h1 id="google-play">
  <img src="https://www.gstatic.com/android/market_images/web/play_prism_hlock_2x.png" width="168" height="35"/>
</h1>

Check out my Google Play Apps!

<ul>
<!-- File transfer tool -->
  <li>
    <h2>
      <img src="https://play-lh.googleusercontent.com/jGpeo-N4WzHxnvzVhauN7eagBU5vTiZPvnLLNgpP7xtVkjlFFV8BJquUdLsXfjGhnQ=w240-h480-rw" width="24" height="24"> Open Source Easy File Transfer <a style="color:#b5e853; text-decoration: none;" href="https://play.google.com/store/apps/details?id=software.isratech.filetransferos" target="_blank">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
    <img src="https://play-lh.googleusercontent.com/iHuddteA7OHsEr9jMnzo15gXJbZaAOHeEBDGZ_cv1u1MF6mOJGNhSMnETmQMnQlc1nI=w526-h296-rw" width="17%">
    <img src="https://play-lh.googleusercontent.com/SG7YI3_F70NN1pWVLh4AJXPycm2YC9XSNjCwigQB6N7Q64leSXaZXaDoPxC4uTPebu5z=w526-h296-rw" width="17%">
    <img src="https://play-lh.googleusercontent.com/AR9QsUbVkMCtYRkU_MVl8jDhLWcjWvQIWtftM-4l1OxbuZ9LmGpsh6k3m2B4uMCK_ZBW=w526-h296-rw" width="17%">
    <img src="https://play-lh.googleusercontent.com/9mJW796gIMOoZ3HULnPw9pOxOhhjfhPLp9veOMIw-FBtW1ZVWTByD3t49aLNbCHOyVhI=w526-h296-rw" width="17%">
    <p>Tired of sending files back and forth through Whatsapp, just to transfer them from your PC to your Phone and vice versa? Would you like an AirDrop equivalent for Android and Windows? Well, this is it! Simply pick the file you want to send, and let the receiving device connect to your device and viola!</p>
    <p>This is a companion app for the <a style="color:#b5e853; text-decoration: none;" href='https://github.com/leolion3/Portfolio/tree/master/Python/FileSender' target='_blank'>Python File Transfer Tool <i class="fa fa-external-link"></i></a> found <a style="color:#b5e853; text-decoration: none;" href="#file-transfer-ref">above</a>. A Java graphical variant is pending release and will soon be available on Github!</p>
  </li>
<!-- Sharky -->
  <li>
    <h2>
      <img src="https://lh3.googleusercontent.com/iwBywQJPRV8Rk-uuHzMzSspSaTO8AHjgBgeqovw8SlWpdej_vcU68LPLaRa9jptfHlk=s180-rw" width="24" height="24"> Sharky the hungry Sharkfish Game <a style="color:#b5e853; text-decoration: none;" target="_blank" href="https://play.google.com/store/apps/details?id=com.SpaceAhoy.Sharky">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
    <img src="https://lh3.googleusercontent.com/O04pRpbIiKpY2r_QRSajjbVJ0cxDMSwJhoHZuXFl6fTBdlJUFj6oSbgS1nTyJghnz7E=w720-h310-rw" width="85%">
    <p>Sharky is very Hungry! Help by feeding him as many fish as you can, but watch out for those nasty harpoons!<br>Sharky is a family-friendly game designed for all ages. Furthermore it is completely FREE<br> and AD-FREE. Collect coins to unlock powerups and new skins, and get that highscore!<br>Sharky is a great time killer for your free time as well!<br /> Be it while waiting at the airport, or in the subway, sharky can played anywhere at any given time!<br /> What are you still waiting for? Get Sharky today!
    </p>
  </li>
<!-- Semesterplaner -->
  <li>
    <h2>
      <img src="https://lh3.googleusercontent.com/asPozAuGQpJqNz-PB0yesBw9wRGkLDuquGqCf0p47rqBSvhxU5pdNHS27O5fuSF_RyY=s180-rw" width="24" height="24"> SemesterPlaner - Plan your Schedule! <a style="color:#b5e853; text-decoration: none;" target="_blank" href="https://play.google.com/store/apps/details?id=com.spaceahoy.semesterplaner">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
      <img src="https://lh3.googleusercontent.com/7VQlwaGV-Btk3i9eHY-unfSE1El_0YdQxBfO8yCXA_h4qVnpycARmJgWVFGvnavCuw=w720-h310-rw" width="17%">
      <img src="https://lh3.googleusercontent.com/7vt1bGzJIL-Pk_uBpK5hXMpATIz9thDZc0m6LmaNn4gdaKkqvnxuE-q4IvZXAUXxiDbc=w720-h310-rw" width="17%">
      <img src="https://lh3.googleusercontent.com/Dri_kxSxbTtZj5vPwaAgBcjHYk9ICKFnsz52YkFK-V0Y9HEDO4dQ-yBHipLJpQLOksw=w720-h310-rw" width="17%">
      <img src="https://lh3.googleusercontent.com/jBKn8CFZGN5S1iTFMFcjZJ4ZcbAf668fpEZxE8FHthfntdCOAIEJmE-umYJbYAK-e80=w720-h310-rw" width="17%">
      <p>Tired of using the same old photoshop template for your semester schedule?<br>Why not automate your schedule creation today using Semester Planer!<br>Just select your work days, how long you work per day and hit that button!<br>Semester Planer will automatically create you a schedule table that can be filled,<br />edited and exported to PNG at any given time!<br> Stop wasting your time and use Semester Planer today!</p>
  </li>
<!-- Password Generator -->
  <li>
    <h2>
      <img src="https://lh3.googleusercontent.com/w_qN0qkMH9B-XmVHDn4GDEFfaISZ3ItJuwahMIqq0BfqW-3_GtLsETiG6URyOy_vKA=s180-rw" width="24" height="24"> Open-Source Password Generator App <a style="color:#b5e853; text-decoration: none;" target="_blank" href="https://play.google.com/store/apps/details?id=processing.test.password_generator">(Google Play <i class="fa fa-external-link"></i>)</a>
    </h2>
    <img src="https://lh3.googleusercontent.com/XVku5gPbTFGz4LMZX9N8PnA-ptAwuMck9XifV_vJ3XIFe9pAS-debgjAPU0nlq5ZbZU=w720-h310-rw" width="17%">
    <img src="https://lh3.googleusercontent.com/F2CGan-SO4JPkvI7RxjksN97mC5EerzL-rKvzuMvwIOji1COJS_-2Bk59p4tXLd8bsQ=w720-h310-rw" width="17%">
    <img src="https://lh3.googleusercontent.com/Ebmg4CAn755JETg3MU2DIOVTVZLZUvJdVINBK2n6PykKf4f_i0coL_gEQObh_VCIA0Y=w720-h310-rw" width="17%">
    <img src="https://lh3.googleusercontent.com/AZq9XFuuxM06D02eTipgmsPg7UO7iIZL2OiMvayBcOLDG8j3VbrKWBr7gdd1rCt-Aw=w720-h310-rw" width="17%">
    <p>Passwords can be a real hustle, especially when you have a thousand accounts for a gazillion different websites...<br>There are some great password generators out there, however how can you ever really trust such a service if it is not open sourced?<br />Stop worrying about your passwords today, with this Free, Open-Source Password Generator!<br>Password Generator is completely FREE and AD-FREE, it works 100% offline an creates you a password in seconds!<br>The source code can be found on <a style="color:#b5e853; text-decoration: none;" href="https://github.com/leolion3/App-Tutorial/tree/master/Password_Generator" target="_blank">Github <i class="fa fa-external-link"></i></a>
    </p>
  </li>
</ul>

<hr/>

<h1 id="contact-section">Contact</h1>

You can contact me using my <a style="color:#b5e853; text-decoration: none;" href="mailto:s_xsipo6@uni-bremen.de">email address <i class="fa fa-external-link"></i></a> or on Instagram <a style="color:#b5e853; text-decoration: none;" target="_blank" href="https://www.instagram.com/xleolion3">@xleolion3 <i class="fa fa-external-link"></i></a>
