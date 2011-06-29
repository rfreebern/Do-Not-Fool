<?php

/*
	Do Not Fool
	Enabling responsible and respectful online April Fools jokes.
	Checks for the existence and value of the DNF request header.
	
	By Ryan N. Freebern <ryan@freebern.org>
	https://github.com/rfreebern/Do-Not-Fool
	License: CC-BY http://creativecommons.org/licenses/by/3.0
	Inspired by http://mozillalabs.com/blog/2011/04/protecting-users-from-an-age-old-threat/
	
	Usage:
	include_once('aprilfools.php');

	Show joke to all users who haven't opted out.
	if (AprilFools::okayToFool()) { <joke code goes here> }

	Show joke to only users who have opted in.
	if (AprilFools::userOptsIn()) { <joke code goes here> }

	Show explanation to users who have opted out.
	if (AprilFools::userOptsOut()) { <explanation code goes here> }
*/

class AprilFools {
	// okayToFool
	// Returns false if user has sent DNF header with value 0; true otherwise.
	public static function okayToFool () {
		$dnf = AprilFools::DNFHeaderValue();
		return !is_null($dnf) ? !$dnf : true;
	}
	
	// userOptsIn
	// Returns true only if user has sent DNF header with value 0 ("fool me"); false otherwise.
	public static function userOptsIn () {
		$dnf = AprilFools::DNFHeaderValue();
		return !is_null($dnf) and $dnf == 0;
	}
	
	// userOptsOut
	// Returns true only if user has sent DNF header wth value 1 ("do not fool me"); false otherwise.
	public static function userOptsOut () {
		$dnf = AprilFools::DNFHeaderValue();
		return !is_null($dnf) and $dnf == 1;
	}
	
	private static function DNFHeaderValue () {
		$requestHeaders = getallheaders();
		return isset($requestHeaders['DNF']) ? $requestHeaders['DNF']: null;
	}
}

?>
