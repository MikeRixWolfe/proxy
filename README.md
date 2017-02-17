## Goals
This is a simple web proxy powered by Flask and Breadability.

## Installation
Install python 2.7.x and then run the following

     git clone https://github.com/MikeRixWolfe/proxy.git
     sudo pip2 install -r requirements.txt

## Setup
Open `config.py` and enter desired information.

## Usage
#### Server
Run `./run` in a screen/tmux session or with nohup/wsgi/whatever.
#### Client
Browse to `http://yoursite.tld/proxy` for the web input form.

Browse/cUrl/whatever `http://yoursite.tld/proxy/<site_url>` to navigate directly to the proxied page.

## Requirements
* Python 2.7.x
* BeautifulSoup4
* Breadability
* Flask
* Flask-WTF
* Requests

## License
This software is licensed under the **GPL v3** license. The terms are as follows:
     
     proxy
     Copyright (C) 2015  Mike Rix Wolfe
     
     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     
     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.
     
     You should have received a copy of the GNU General Public License
     along with this program.  If not, see <http://www.gnu.org/licenses/>.
