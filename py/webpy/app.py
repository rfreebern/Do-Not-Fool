#!/usr/bin/env python

"""
	Example web.py app using Do-Not-Fool detection
	Requires web.py framework -- http://webpy.org
	
	By Ryan N. Freebern <ryan@freebern.org>
	https://github.com/rfreebern/Do-Not-Fool
	License: CC-BY http://creativecommons.org/licenses/by/3.0
	Inspired by http://mozillalabs.com/blog/2011/04/protecting-users-from-an-age-old-threat/
	
	Usage:
	sudo easy_install web.py
	python app.py
"""

import web
from donotfool import AprilFools
urls = ('/', 'index')

app = web.application(urls, globals())

class index:
	def GET(self):
		if AprilFools.okayToFool():
			return "April Fools!"
		else:
			return "Greetings, gentle visitor."

if __name__ == "__main__": app.run()

