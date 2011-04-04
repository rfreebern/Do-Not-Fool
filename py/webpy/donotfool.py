#!/usr/bin/env python

"""
	Do Not Fool
	Enabling responsible and respectful online April Fools jokes.
	Checks for the existence and value of the DNF request header.

	By Ryan N. Freebern <ryan@freebern.org>
	https://github.com/rfreebern/Do-Not-Fool
	License: CC-BY http://creativecommons.org/licenses/by/3.0
	Inspired by http://mozillalabs.com/blog/2011/04/protecting-users-from-an-age-old-threat/

	Usage:
	from donotfool import AprilFools

	# Show joke to all users who haven't opted out.
	if AprilFools.okayToFool():
		<joke code goes here>
	
	# Show joke to only users who have opted in.
	if AprilFools.userOptsIn():
		<joke code goes here>
	
	# Show explanation to users who have opted out.
	if AprilFools.userOptsOut():
		<explanation code goes here>
"""

import web

class AprilFools():
	@staticmethod
	def okayToFool():
		dnf = web.ctx.env.get('HTTP_DNF')
		return dnf in [None, 0]

	@staticmethod
	def userOptsIn():
		dnf = web.ctx.env.get('HTTP_DNF')
		return dnf == 1

	@staticmethod
	def userOptsOut():
		dnf = web.ctx.env.get('HTTP_DNF')
		return dnf == 0
		
