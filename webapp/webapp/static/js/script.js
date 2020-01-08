//ナビゲーションのスクロール設定
jQuery(function() {
	$('#menu').scrollFollow({
		topAdjust: 0,
		topOverrun: 0,
		bottomAdjust: 0,
		bottomOverrun: 0
	});
});

/*ロールオーバー
------------------------------*/

window.onload=function(){
rollovers( '_df' , '_ov' );
}

rollovers=function(off,on){
img=document.getElementsByTagName("img");p=[];
off_reg=new RegExp(off+"(\.[a-z]+$)","i");on_reg=new RegExp(on+"(\.[a-z]+$)","i");
for(var x=0,i;i=img[x];x++){ if(i.src.match(off_reg)){p[x]=new Image();p[x].src=i.src.replace(off_reg,on+"$1");
i.onmouseover=function(){this.src=this.src.replace(off_reg,on+"$1");};
i.onmouseout=function(){this.src=this.src.replace(on_reg,off+"$1");};};};};

/*ページ内スクロール
------------------------------*/
jQuery.easing.quart = function (x, t, b, c, d) {
    return -c * ((t=t/d-1)*t*t*t - 1) + b;
};
 

jQuery(document).ready(function(){
 

    jQuery('a[href*=#]').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
            var $target = jQuery(this.hash);
            $target = $target.length && $target || jQuery('[name=' + this.hash.slice(1) +']');
            if ($target.length) {
                var targetOffset = $target.offset().top;
                jQuery('html,body').animate({ scrollTop: targetOffset }, 1200, 'quart');
                return false;
            }
        }
    });
 
});


/*アコーディオン
------------------------------*/
var j$ = jQuery;

j$(function(){
	j$(".side_menu").each(function(){
		j$("li > a", this).each(function(index){
			var $this = j$(this);
			if(index > 0) $this.next().hide();

			$this.mousedown(function(){
				var params = {height:"toggle", opacity:"toggle"};
				j$(this).next().animate(params).parent().siblings()
				.children("ul:visible").animate(params);	

				return false;				

			});
		});
	});
});

$(function() {
    $('#jsnavi').droppy({speed: 200});
  });
  

/*プルダウン
------------------------------*/
/*
 * Droppy 0.1.2
 * (c) 2008 Jason Frame (jason@onehackoranother.com)
 */
$.fn.droppy = function(options) {
    
  options = $.extend({speed: 250}, options || {});
  
  this.each(function() {
    
    var root = this, zIndex = 1000;
    
    function getSubnav(ele) {
      if (ele.nodeName.toLowerCase() == 'li') {
        var subnav = $('> ul', ele);
        return subnav.length ? subnav[0] : null;
      } else {
        return ele;
      }
    }
    
    function getActuator(ele) {
      if (ele.nodeName.toLowerCase() == 'ul') {
        return $(ele).parents('li')[0];
      } else {
        return ele;
      }
    }
    
    function hide() {
      var subnav = getSubnav(this);
      if (!subnav) return;
      $.data(subnav, 'cancelHide', false);
      setTimeout(function() {
        if (!$.data(subnav, 'cancelHide')) {
          $(subnav).slideUp(options.speed);
        }
      }, 500);
    }
  
    function show() {
      var subnav = getSubnav(this);
      if (!subnav) return;
      $.data(subnav, 'cancelHide', true);
      $(subnav).css({zIndex: zIndex++}).slideDown(options.speed);
      if (this.nodeName.toLowerCase() == 'ul') {
        var li = getActuator(this);
        $(li).addClass('jshover');
        $('> a', li).addClass('jshover');
      }
    }
    
    $('ul, li', this).hover(show, hide);
    $('li', this).hover(
      function() { $(this).addClass('jshover'); $('> a', this).addClass('jshover'); },
      function() { $(this).removeClass('jshover'); $('> a', this).removeClass('jshover'); }
    );
    
  });
  
};
