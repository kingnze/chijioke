$('.slider-two')
.not(".slick-intialized")
.slick({
    prevArrow:".site-slider-two .prev",
    nextArrow:".site-slider-two .next",
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplayspeed: 1000,
    autoplay:true,
    // dots:true,

});

$('.move-up span').click(function(){
      $('html,body').animate({
          scrollTop: 0
      }, 1000);
})

const pwd = document.querySelector('#pwd');
const seepwd = document.querySelector('#see');

seepwd.addEventListener('click',()=>{

  if(pwd.type !=='password'){
  pwd.type = "password"
  seepwd.className+='fas fa-eye';
  }else{
    pwd.type ="text"
  seepwd.className+='fas fa-eye-slash';
  }
});