# Meraki Captive Portals in Python

Create Custom Meraki Captive Portals in Python.

![Sample Custom Captive Portal](https://github.com/Procellis-Technology-Inc/MCPiP/blob/33658cc2f60886c011f88790c7056d72c0b46274/sample_portal.png)
 
## Use Case Description
MCPiP is a basic getting-started repository with the elements needed to create a simple Meraki Captive Portal using Python and Flask.

The intended use case for this software is a learning resource and base code for creating original captive portals for a business.  Captive Portals themselves are an important security, marketing and outreach tool for businesses of all sizes.

Features
Customizable Jinja2 template based splashscreen<br>
Redirection to any website upon connection


## Installation

Requirements
Python >= 3.7
Flask >= 2.0.3
Flask-Session >= 0.4.0
os

On the server where you want to host the Captive Portal:
1. Clone the repository
2. pip install -r requirements.txt
3. Configure the port in line 34 of app.py

33 if __name__ == '__main__':
34     app.run(host='0.0.0.0', port=5050)

4. Configure the redirect website in line 29

29        return redirect('https://www.example.com/')

5. python3 app.py

In the Meraki dashboard:
1. Navigate to Wireless > Configure > SSIDs
2. Beneath the SSID to be used, click edit settings.
3. In the Splash page section, select Click-through.
4. In the Security settings section
a) Set Captive portal strength to Block all access until sign-on is complete
b) Set Walled garden to Walled garden is enabled
c) Set Walled garden ranges to the address of the server where the Captive Portal application is running
5. Save changes
6. Next navigate to Wireless > Configure > Splash page
7. Select the SSID to be used
8. Under Custom splash page URL
a) Select Or provide a URL where users will be redirected
b) Enter the server address and port where the Captive Portal application is running
9. Save changes

## Configuration

In the templates/base.html file:
1. Enter appropriate values in the metatags to match business requirements.
2. Enter a title in line 11 between the <title> and </title> tags.

In the templates/captive_portal.html file:
1. Include the link and image to the company logo and website url in line 5 between the <a> tag and the </a> tag.
2. Change the header in line 6 to the desired text
3. Change the paragraph in line 7 to the desired text.

In the static/images folder:
1. Replace the background.jpeg file with your desired background image
2. Replace the logo.png file with the logo file of your choosing
3. Replace favicon.png with the desired favicon for the site

## Usage

When users attempt to use the SSID they will be unable to access any sites outside the walled garden specified in the Meraki dashboard until they have clicked the connect button on the captive portal site.

Ideas to deploy and otherwise improve this code:
1. Containerize the server application and run it in docker or a docker swarm for redundancy
2. Get the application production-ready by replacing the Flask built-in WSGI server with Gunicorn or a similar package
3. Secure the Captive Portal site using HTTPS
4. Investigate other varieies of captive portal such as username and password login

## How to test the software

Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. 
If the repo includes automated tests, detail how to run those tests.
If the repo is instrumented with a continuous testing framework, that is even better.


## Known issues

End-users who attempt to access an HTTPS site before connecting to the Captive Portal will not be redirected.  Instead the browser will attempt to authenticate the SSL/TLS certificate for the website and fail if the site is not in the walled garden.  The end-user will see a browser timeout message, or their device will likely switch back to using mobile data to access the site.
Meraki can not perform HTTPS inspection outside of the 15.X Beta program.  As a result it is not possible to actively redirect HTTPS requests to the captive portal page before they attempt to authenticate.

## Getting help

There are a wealth of resources out there about Captive Portals in Meraki.

For Flask issues, please refer to the official Flask documentation at https://flask.palletsprojects.com/en/2.0.x/ .  The authors would also recommend Miguel Grinberg's Flask Mega-Tutorial at https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world .

If you find a bug, have a question or a concern about the content of this repository, or would like to reach one of the authors, please create an issue within this repository or reach out to us by email.

## Getting involved

This repository was created for mass consumption and we would love to have people get involved and improve the code, add features, or provide sample customizations.  Feel free to clone the repository as you wish, but please follow the rules included in the license.


## License
This code is copyright 2022 Procellis Technology, Inc.
It is distributed under the 3-Clause BSD License.

See LICENSE for the full text.

## Author(s)

This project was written and is maintained by the following individuals:

* Nathan Haleen <nathan.haleen@procellis.com>
* Julia Ha
* Shouayee Vue (shouayee.vue@procellis.com)
* Ruben Dedman (rubend@synnex.com)
* Halley Paulson
* Beth Taylor
