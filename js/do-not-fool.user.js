// ==UserScript==
// @name          Do Not Fool
// @namespace     https://github.com/rfreebern/Do-Not-Fool
// @description	  Sets a window-level variable for other scripts to read, telling them that this user doesn't want to be fooled.
// @include       *
// ==/UserScript==

unsafeWindow.__DNF = 1;
