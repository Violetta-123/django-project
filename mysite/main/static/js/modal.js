$(document).ready(function($) {
	$('.popup-open').click(function() {
		$('.popup-login').fadeIn();
		return false;
	});	
	
	$('.popup-close').click(function() {
		$(this).parents('.popup-login').fadeOut();
		$(this).parents('.popup-signup').fadeOut();
		return false;
	});
	$('.ref').click(function() {
		$(this).parents('.popup-login').fadeOut();
		$('.popup-signup').fadeIn();
		return false;
	});
	$(document).keydown(function(e) {
		if (e.keyCode === 27) {
			e.stopPropagation();
			$('.popup-login').fadeOut();
		}
	});
	
	$('.popup-login').click(function(e) {
		if ($(e.target).closest('.popup').length == 0) {
			$(this).fadeOut();					
		}
	});
	$('.popup-signup').click(function(e) {
		if ($(e.target).closest('.popup').length == 0) {
			$(this).fadeOut();
		}
	});
});

var inputs=document.getElementsByTagName('input');
for(i=0;i<inputs.length;i++)
  if(inputs[i].type=='hidden') inputs[i].type='text';