## Description
This is a simple readability proxy powered by Flask. Note: this does not work well with dynamic content or flash/flash-like sites.

## Installation
Install python 2.7.x and then run the following

     git clone https://github.com/MikeRixWolfe/proxy.git
     sudo pip2 install -r requirements.txt

## Setup
Rename app.cfg.default to app.cfg and enter desired information.

## Usage
#### Server
Run `wsgi.py` wsgi/whattever.
#### Client
Browse to `http://yoursite.tld/proxy` for the web input form.

Browse to `http://yoursite.tld/proxy/<site_url>` to navigate directly to the proxied page.

## Requirements
* Python 2.7.x
* Flask
* Flask-WTF
* Requests

## License
This software is licensed under the **GPL v3** license. The terms are as follows:
     
     proxy
     Copyright (C) 2017  Mike Rix Wolfe
     
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
