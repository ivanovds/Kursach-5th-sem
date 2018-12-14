"use strict";
jQuery(document).ready(function ($) {

    /*---------------------------------------------*
     * Mobile menu
//     ---------------------------------------------*/
//    $('#navbar-menu').find('a[href*=#]:not([href=#])').click(function () {
//        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
//            var target = $(this.hash);
//            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
//            if (target.length) {
//                $('html,body').animate({
//                    scrollTop: (target.offset().top - 70)
//                }, 1000);
//                if ($('.navbar-toggle').css('display') != 'none') {
//                    $(this).parents('.container').find(".navbar-toggle").trigger("click");
//                }
//                return false;
//            }
//        }
//    });



    /*---------------------------------------------*
     * WOW
     ---------------------------------------------*/

//    var wow = new WOW({
//        mobile: false // trigger animations on mobile devices (default is true)
//    });
//    wow.init();


//---------------------------------------------
// Scroll Up 
//---------------------------------------------

    $('.scrollup').click(function () {
        $("html, body").animate({scrollTop: 0}, 1000);
        return false;
    });





//Team Skillbar active js



 
    
    // Timer
    var now = new Date();
    function countDown(second,endMinute,endHour,endDay,endMonth,endYear) {
second = (arguments.length == 1) ? second + now.getSeconds() : second;
endYear =  typeof(endYear) != 'undefined' ?  endYear : now.getFullYear();            
endMonth = endMonth ? endMonth - 1 : now.getMonth();  //номер месяца начинается с 0   
endDay = typeof(endDay) != 'undefined' ? endDay :  now.getDate();    
endHour = typeof(endHour) != 'undefined' ?  endHour : now.getHours();
endMinute = typeof(endMinute) != 'undefined' ? endMinute : now.getMinutes();   
//добавляем секунду к конечной дате (таймер показывает время уже спустя 1с.) 
var endDate = new Date(endYear,endMonth,endDay,endHour,endMinute,second+1); 
var interval = setInterval(function() { //запускаем таймер с интервалом 1 секунду
    var time = endDate.getTime() - now.getTime();
    if (time < 0) {                      //если конечная дата меньше текущей
        clearInterval(interval);
                   
    } else {            
        var days = Math.floor(time / 864e5);
        var hours = Math.floor(time / 36e5) % 24; 
        var minutes = Math.floor(time / 6e4) % 60;
        var seconds = Math.floor(time / 1e3) % 60;  
        var digit='<div style="width:70px;float:left;text-align:center">'+
        '<div style="font-family:Stencil;font-size:65px;">';
        var text='</div><div>'
        var end='</div>'
        document.getElementById('days').innerHTML =  days;
        document.getElementById('hours').innerHTML = hours;
        document.getElementById('minutes').innerHTML = minutes;
        document.getElementById('seconds').innerHTML = seconds;
        if (!seconds && !minutes && !days && !hours) {              
            clearInterval(interval);
                   
        }           
    }
    now.setSeconds(now.getSeconds() + 1); //увеличиваем текущее время на 1 секунду
}, 1000);
}
    var last_day = now.getDate()+1, last_month = now.getMonth()+1;
    if((now.getHours() == 0)&&(now.getMinutes() < 10)){
        $(".hide_discount_end").css("display", "none");
        $(".myButton").html("Заказать");
        var discount_end = ' <div style="color:white; font-size: 1.5rem;">Действие акции закончилось</div>';
        document.getElementById('discount_end').innerHTML = discount_end;
         }

    countDown(0,0,0,last_day,last_month,2018); 



    // End of timer
     
//    responsive :
    
//function ImgChange(mql){
//    if (mql.matches) {
//    // размер окна 992px или меньше
//      document.getElementById("main-img").src = "images/main-img-sm2.png";
//      document.getElementById("features-img").src = "images/222(2).png";
//} else {
//    // нет, размер окна более 992px 
//    document.getElementById("main-img").src = "images/main-img-lg2.png";
//    document.getElementById("features-img").src = "images/222(1).png";
//}
//    }
//var mql = window.matchMedia('all and (max-width: 992px)');
//    ImgChange(mql);
//    mql.addListener(ImgChange); // режим реального времени(чтоб не нужно было обновлять стр для смены картинки)
    
    
    // email:
    $(document).ready(function() {

	//E-mail Ajax Send
	$("form").submit(function() { //Change
		var th = $(this);
		$.ajax({
			type: "POST",
			url: "mail.php", //Change
			data: th.serialize()
		}).done(function() {
       $('#parent_popup').fadeIn(500);
         
            setTimeout(function() {
				// Done Functions
				th.trigger("reset");
			}, 500);
		});
		return false;
	});

});
    //end of email
      
        
        
    //End
});





