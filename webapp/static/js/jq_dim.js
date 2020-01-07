/**
 * jquery.scrollFollow.js
 * Copyright (c) 2008 Net Perspective (http://kitchen.net-perspective.com/)
 * Licensed under the MIT License (http://www.opensource.org/licenses/mit-license.php)
 * 
 * @author R.A. Ray
 *
 * @projectDescription	jQuery plugin for allowing an element to animate down as the user scrolls the page.
 * 
 * @version 0.4.0
 * 
 * @requires jquery.js (tested with 1.2.6)
 * @requires ui.core.js (tested with 1.5.2)
 * 
 * @optional jquery.cookie.js (http://www.stilbuero.de/2006/09/17/cookie-plugin-for-jquery/)
 * @optional jquery.easing.js (http://gsgd.co.uk/sandbox/jquery/easing/ - tested with 1.3)
 * 
 * @param speed		int - Duration of animation (in milliseconds)
 * 								default: 500
 * @param offset			int - Number of pixels box should remain from top of viewport
 * 								default: 0
 * @param easing		string - Any one of the easing options from the easing plugin - Requires jQuery Easing Plugin < http://gsgd.co.uk/sandbox/jquery/easing/ >
 * 								default: 'linear'
 * @param container	string - ID of the containing div
 * 								default: box's immediate parent
 * @param killSwitch	string - ID of the On/Off toggle element
 * 								default: 'killSwitch'
 * @param onText		string - killSwitch text to be displayed if sliding is enabled
 * 								default: 'Turn Slide Off'
 * @param offText		string - killSwitch text to be displayed if sliding is disabled
 * 								default: 'Turn Slide On'
 * @param relativeTo	string - Scroll animation can be relative to either the 'top' or 'bottom' of the viewport
 * 								default: 'top'
 * @param delay			int - Time between the end of the scroll and the beginning of the animation in milliseconds
 * 								default: 0
 * 
 * 
 * ��L�͖{��jquery scroll follow�̐����ł��B
 * �ȉ��͂�������ɍ����jquery scroll follow plus�ɂ��Ăł��B
 * 
 * Copyright (c) 2011 �L�S��-roheisen net(http://roheisen.net/), �� 2nd Season(http://h2s.roheisen.net/)
 * Licensed under the MIT License (http://www.opensource.org/licenses/mit-license.php)
 * 
 * @���ύ��					�L�S�v��(roheisen projekt) - MMZK, ���� ��
 * 
 * @�K�{�A�I�v�V�������C�u����	�ύX����܂���
 * 
 * @param ralativeTo			string	- �t�H���[�{�b�N�X����ʂ̏㉺�ǂ���Ƀt�B�b�g���邩�̃I�v�V�����ł��B 'both'�A'top'�A'bottom'�̎O������܂��B
 * 											default: 'both'
 * @param topAdjust				int		- ��ʏ�[�t�B�b�g���Ƀt�H���[�{�b�N�X�Ƃ��̒��g�̉��I�u�W�F�N�g�̊Ԃɋ󂢂Ă��錄�Ԃ����s�N�Z���l�߂邩�Ƃ����I�v�V�����ł��B
 * 											default: 0
 * @param topOverrun			int		- �t�H���[�{�b�N�X�����̐e�{�b�N�X�̏�[��艽�s�N�Z���͂ݏo�����Ƃ���܂ňړ��ł��邩�Ƃ����I�v�V�����ł��B
 * 											default: 0
 * @param bottomAdjust			int		- ��ʉ��[�t�B�b�g���Ƀt�H���[�{�b�N�X�Ƃ��̒��g�̉��I�u�W�F�N�g�̊Ԃɋ󂢂Ă��錄�Ԃ����s�N�Z���l�߂邩�Ƃ����I�v�V�����ł��B
 * 											default: 0
 * @param bottomOverrun			int		- �t�H���[�{�b�N�X�����̐e�{�b�N�X�̉��[��艽�s�N�Z���͂ݏo�����Ƃ���܂ňړ��ł��邩�Ƃ����I�v�V�����ł��B
 * 											default: 0
 * @param offset				��L4�ɍו����������߁A�����Ȃ�܂����B
 */

( function( $ ) {
	
	$.scrollFollow = function ( box, options )
	{ 
		// Convert box into a jQuery object
		box = $( box );
		
		// 'box' is the object to be animated
		var position = box.css( 'position' );
		
		function ani()
		{		
			// The script runs on every scroll which really means many times during a scroll.
			// We don't want multiple slides to queue up.
			box.queue( [ ] );
		
			// A bunch of values we need to determine where to animate to
			var viewportHeight = parseInt( $( window ).height() );	
			var pageScroll =  parseInt( $( document ).scrollTop() );
			var parentTop =  parseInt( box.cont.offset().top );
			var parentHeight = parseInt( box.cont.attr( 'offsetHeight' ) );
			var boxHeight = parseInt( box.attr( 'offsetHeight' ) );
			var innerHeight = boxHeight - options.topAdjust - options.bottomAdjust;
			var aniTop;
			var animateflag = 0;
			var topoverflag = 0;
			var bottomoverflag = 0;
			var fitTo;
			var currentTop = parseInt( box.css( 'top' ) );
			if (!currentTop) { currentTop = 0; }
			
			// Make sure the user wants the animation to happen
			if ( isActive )
			{
				//�t�B�b�g��������
				switch (options.relativeTo)
				{
					case 'top':
						fitTo = 'top';
						animateflag = 1;
						break;
					case 'bottom':
						fitTo = 'bottom';
						animateflag = 1;
						break;
					default:
						//both
						if (innerHeight < viewportHeight)
						{
							//�t�H���[�{�b�N�X�̒��g�̑S�����E�B���h�E������菬�����ꍇtop�Ƃ��ď���
							fitTo = 'top';
							animateflag = 1;
						}
						else
						{
							//��[��ʊO�t���O����
							if ((box.initialOffsetTop + currentTop + options.topAdjust) < pageScroll)
							{	topoverflag = 1;	}
							//���[��ʊO�t���O����
							if ((box.initialOffsetTop + currentTop + boxHeight - options.bottomAdjust) > (pageScroll + viewportHeight))
							{	bottomoverflag = 1;	}
							
							// �{�b�N�X�̏�[�E���[���ǂ������ʓ��ɓ����Ă��Ȃ��ꍇ�͓����Ȃ�
							if ((topoverflag) && (bottomoverflag))
							{
								fitTo = 'free';
								animateflag = 0;	
							}
							//�{�b�N�X�̉��[��������ʊO�̏ꍇ�Atop�Ƃ��ď���
							else if (bottomoverflag) {
								fitTo = 'top';
								animateflag = 1;
							}
							//�{�b�N�X�̏�[��������ʊO�̏ꍇ�Abottom�Ƃ��ď���
							else if (topoverflag)
							{
								fitTo = 'bottom';
								animateflag = 1;
							}
							//��ɃT�C�Y�𑪂��Ă��邽�ߏ㉺������ʓ��͂��蓾�Ȃ����A�O�̂��ߓ����Ȃ��t���O�𗧂Ă�
							else
							{
								fitTo = 'free';
								animateflag = 0;
							}
						}
						break;
				}
				// ��[�t�B�b�g
				if (fitTo == 'top')
				{
					aniTop = Math.max( ( -options.topOverrun ) ,  Math.min( ( pageScroll - box.initialOffsetTop - options.topAdjust ), ( parentHeight - boxHeight + options.bottomOverrun ) ) );
				}
				// ���[�t�B�b�g
				if (fitTo == 'bottom')
				{
					aniTop = Math.max( ( -options.topOverrun ) ,  Math.min( ( pageScroll + viewportHeight - box.initialOffsetTop - boxHeight + options.bottomAdjust), ( parentHeight - boxHeight + options.bottomOverrun ) ) );
				}
				
				// Checks to see if the relevant scroll was the last one
				// "-20" is to account for inaccuracy in the timeout
				if (animateflag)
				{
					if ( ( new Date().getTime() - box.lastScroll ) >= ( options.delay - 20 ) )
					{
						box.animate(
							{
								top: aniTop
							}, options.speed, options.easing
						);
					}
				}
			}
		};
		
		// For user-initiated stopping of the slide
		var isActive = true;
		
		if ( $.cookie != undefined )
		{
			if( $.cookie( 'scrollFollowSetting' + box.attr( 'id' ) ) == 'false' )
			{
				var isActive = false;
				
				$( '#' + options.killSwitch ).text( options.offText )
					.toggle( 
						function ()
						{
							isActive = true;
							
							$( this ).text( options.onText );
							
							$.cookie( 'scrollFollowSetting' + box.attr( 'id' ), true, { expires: 365, path: '/'} );
							
							ani();
						},
						function ()
						{
							isActive = false;
							
							$( this ).text( options.offText );
							
							box.animate(
								{
									top: box.initialTop
								}, options.speed, options.easing
							);	
							
							$.cookie( 'scrollFollowSetting' + box.attr( 'id' ), false, { expires: 365, path: '/'} );
						}
					);
			}
			else
			{
				$( '#' + options.killSwitch ).text( options.onText )
					.toggle( 
						function ()
						{
							isActive = false;
							
							$( this ).text( options.offText );
							
							box.animate(
								{
									top: box.initialTop
								}, 0
							);	
							
							$.cookie( 'scrollFollowSetting' + box.attr( 'id' ), false, { expires: 365, path: '/'} );
						},
						function ()
						{
							isActive = true;
							
							$( this ).text( options.onText );
							
							$.cookie( 'scrollFollowSetting' + box.attr( 'id' ), true, { expires: 365, path: '/'} );
							
							ani();
						}
					);
			}
		}
		
		// If no parent ID was specified, and the immediate parent does not have an ID
		// options.container will be undefined. So we need to figure out the parent element.
		if ( options.container == '')
		{
			box.cont = box.parent();
		}
		else
		{
			box.cont = $( '#' + options.container );
		}
		
		// Finds the default positioning of the box.
		box.initialOffsetTop =  parseInt( box.offset().top );
		box.initialTop = parseInt( box.css( 'top' ) ) || 0;
		
		// Hack to fix different treatment of boxes positioned 'absolute' and 'relative'
		if ( box.css( 'position' ) == 'relative' )
		{
			box.paddingAdjustment = parseInt( box.cont.css( 'paddingTop' ) ) + parseInt( box.cont.css( 'paddingBottom' ) );
		}
		else
		{
			box.paddingAdjustment = 0;
		}
		
		// Animate the box when the page is scrolled
		$( window ).scroll( function ()
			{
				// Sets up the delay of the animation
				$.fn.scrollFollow.interval = setTimeout( function(){ ani();} , options.delay );
				
				// To check against right before setting the animation
				box.lastScroll = new Date().getTime();
			}
		);
		
		// Animate the box when the page is resized
		$( window ).resize( function ()
			{
				// Sets up the delay of the animation
				$.fn.scrollFollow.interval = setTimeout( function(){ ani();} , options.delay );
				
				// To check against right before setting the animation
				box.lastScroll = new Date().getTime();
			}
		);

		// Run an initial animation on page load
		box.lastScroll = 0;
		
		ani();
	};
	
	$.fn.scrollFollow = function ( options )
	{
		options = options || {};
		options.relativeTo = options.relativeTo || 'both';
		options.speed = options.speed || 500;
		options.topAdjust = options.topAdjust || 0;
		options.topOverrun = options.topOverrun || 0;
		options.bottomAdjust = options.bottomAdjust || 0;
		options.bottomOverrun = options.bottomOverrun || 0;
		options.easing = options.easing || 'swing';
		options.container = options.container || this.parent().attr( 'id' );
		options.killSwitch = options.killSwitch || 'killSwitch';
		options.onText = options.onText || 'Turn Slide Off';
		options.offText = options.offText || 'Turn Slide On';
		options.delay = options.delay || 0;
		
		this.each( function() 
			{
				new $.scrollFollow( this, options );
			}
		);
		
		return this;
	};
})( jQuery );
