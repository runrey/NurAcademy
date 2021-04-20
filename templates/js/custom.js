$(document).ready(function(){
	$("#menu").on("click","a", function (event) {
		//отменяем стандартную обработку нажатия по ссылке
		event.preventDefault();
		//забираем идентификатор бока с атрибута href
		var id = $(this).attr('href'),
		//узнаем высоту от начала страницы до блока на который ссылается якорь
		top = $(id).offset().top;
		//анимируем переход на расстояние - top за 800 мс
		$('body,html').animate({scrollTop: top}, 800);
	});
});

$(document).ready(function(){
	$("#menum").on("click","a", function (event) {
		event.preventDefault();
		var id = $(this).attr('href'),
		top = $(id).offset().top;
		$('body,html').animate({scrollTop: top}, 800);
	});
});

$(document).ready(function(){
	$('.menu-toggle').click(function(){
		$('.header-mobile-left').toggleClass('active');
	})
	$('.menu-login').click(function(){
		$('.header-mobile-right').toggleClass('active');
	})
	$('.menu-loginm').click(function(){
		$('.header-mobile-right').toggleClass('active');
	})
})

window.onscroll = function() {
	if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
		document.querySelector(".header-mobile-left").style.top = "82px"; 
		document.querySelector(".header-mobile-right").style.top = "82px"; 
	    document.querySelector(".logo").style.fontSize = "3rem";
	    document.querySelector(".header-normal").style.backgroundColor = "#fff";
	    document.querySelector(".header-normal").style.boxShadow = "0 0 5px #000000";
	    document.querySelector(".logo").style.color = "#767676";
	    document.querySelector(".logo").style.textShadow = "none";
	    var x = document.getElementsByClassName("hlinks");
	    for (var i =0; i <x.length; i++) {
	      	x[i].style.color = "#000";
	    }
	    document.querySelector(".menu-toggle").style.color = "#000";
	    document.querySelector(".menu-login").style.color = "#000";
			       
	} 
	else {
	  	document.querySelector(".header-mobile-left").style.top = "120px";
	  	document.querySelector(".header-mobile-right").style.top = "120px"; 
	    document.querySelector(".logo").style.fontSize = "5rem";
	    document.querySelector(".header-normal").style.backgroundColor = "transparent";
	    document.querySelector(".header-normal").style.boxShadow = "0 0 5px transparent";
	    document.querySelector(".logo").style.color = "#ffd700";
	    document.querySelector(".logo").style.textShadow = "8px 2px black";
	    var x = document.getElementsByClassName("hlinks");
	    for (var i =0; i <x.length; i++) {
	       	x[i].style.color = "#555";
	    }
	    document.querySelector(".menu-toggle").style.color = "#555";
	    document.querySelector(".menu-login").style.color = "#555";
	}
}

AOS.init();