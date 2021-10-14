/* ========================================================================

Tale: theme.js
Main Theme JS file

@Author: Andrew ch 
@URL: http://andrewch.eu
 
=========================================================================
 */

'use strict';


jQuery(document).ready(function( $ ) {

	// Dropdown
	//===================

	( function( $ ) {

	$('#cssmenu ul  li:odd').addClass('odd');
	$('#cssmenu ul  li:even').addClass('even');
	$('#cssmenu > ul > li > a').click(function() {
	  $('#cssmenu li').removeClass('active');
	  $(this).closest('li').addClass('active'); 
	  var checkElement = $(this).next();
	  if((checkElement.is('ul')) && (checkElement.is(':visible'))) {
	    $(this).closest('li').removeClass('active');
	    checkElement.slideUp('normal');
	  }
	  if((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
	    $('#cssmenu ul ul:visible').slideUp('normal');
	    checkElement.slideDown('normal');
	  }
	  if($(this).closest('li').find('ul').children().length == 0) {
	    return true;
	  } else {
	    return false;   
	  }     
	});
	} )( jQuery ); 

	// Loader
	//===================

/*	$(window).load(function(){
		setTimeout(function(){
			$('.loading').addClass("hidden");
			$('.loader-logo').addClass("slideOutUp");
			$('.loader').addClass("slideOutUp");
			$('body').addClass("body-animated");
		}, 900);
	});*/

	// Search
	//===================

	$('.search-trigger').on('click', function () {
		var search = $('.search');
		$(search).toggleClass('search-open');
		//$('.search-trigger').find('.ion-ios-search-strong').css("opacity", "0");
	});
	
	// Full Height
	//===================

	var NavHeight = $('.main-navigation').outerHeight();
	$('.full-height').css({ 'max-height': 'calc(100vh - ' + NavHeight+ 'px)' });

	// Home Masonry
	//===================

	masonry: {
		selector: "ul.masonry-wrap"
		var base = this, container = $(base.selector);
		container.each(function() {
			var item = $(this);
			win.load(function() {
				item.isotope({
					layoutMode: "packery",
					itemSelector: ".masonry-item",
					transitionDuration: "0.5s",
					columnWidth: 25,
					resizesContainer: true,
					masonry: {
						columnWidth: ".masonry-item"
					}
				});
			});
		});
	}

	// Countdown
	//===================

	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});

	// Hamburger Icon Animation

	(function () {
		var active;
		active = true;
		$('#navicon').on('click', function () {
			if (active === true) {
				$('#navicon').removeClass('inactive').addClass('active');
				active = false;
			} else {
				$('#navicon').removeClass('active').addClass('inactive');
				active = true;
			}
		});
	}.call(this));

	//Navigation Menu
	//===================
	$('.toggle-menu').jPushMenu({
		closeOnClickLink: false
	});


	// Dropdown
	$('.mobile-dropdown').simpleexpand();

	// On Scroll Animations
	//===================

	function onScrollInit( items, trigger ) {
		items.each( function() {
			var osElement = $(this),
				osAnimationClass = osElement.attr('data-os-animation'),
				osAnimationDelay = osElement.attr('data-os-animation-delay');
		 
			osElement.css({
				'-webkit-animation-delay':  osAnimationDelay,
				'-moz-animation-delay':     osAnimationDelay,
				'animation-delay':          osAnimationDelay
			});
		 
			var osTrigger = ( trigger ) ? trigger : osElement;
		 
			osTrigger.waypoint(function() {
				osElement.addClass('animated').addClass(osAnimationClass);
			},{
				triggerOnce: true,
				offset: '90%'
			});
		});
	}

	setTimeout(function() {
		onScrollInit( $('.os-animation') );
		onScrollInit( $('.staggered-animation'), $('.staggered-animation-container') );
	}, 600);
	
	// Back to top button
	//===================

	$('.go-top').on('click', function (event) {
		event.preventDefault();
		{$('html, body').velocity('scroll',{duration: 1000, offset:0});}
	});
});
