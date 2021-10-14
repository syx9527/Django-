/* ========================================================================

Tale: slider-initialization.js

Slider Initialization File.

We use a second file to init revolution slider, since we don't need to load all the revolution-slider
files on all pages, for the sake of speed.

---

@Author: Andrew ch 
@URL: http://andrewch.eu
 
=========================================================================
 */

'use strict';

jQuery(document).ready(function( $ ) {

	$('.home-slider').slick({
	centerMode: true,
	centerPadding: '60px',
	autoplay: true,
	autoplaySpeed: 2500,
	slidesToShow: 1,
	responsive: [
	{
	  breakpoint: 768,
	  settings: {
	    arrows: false,
	    centerMode: true,
	    centerPadding: '0px',
	    slidesToShow: 1
	  }
	},
	{
	  breakpoint: 480,
	  settings: {
	    arrows: false,
	    centerMode: true,
	    centerPadding: '0px',
	    slidesToShow: 1
	  }
	}
	]
	});
});
