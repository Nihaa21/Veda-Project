

// ------------slider-----------
// $('#myCarousel').carousel({
//     interval: false
// })
//
// $('.carousel .carousel-item').each(function() {
//     var minPerSlide = 4;
//     var next = $(this).next();
//     if (!next.length) {
//         next = $(this).siblings(':first');
//     }
//     next.children(':first-child').clone().appendTo($(this));
//
//     for (var i = 0; i < minPerSlide; i++) {
//         next = next.next();
//         if (!next.length) {
//             next = $(this).siblings(':first');
//         }
//
//         next.children(':first-child').clone().appendTo($(this));
//     }
// });



function lockScroll() {
          document.body.classList.toggle('lock-scroll');
    }

/*  Carousel*/
$('#carousel-example').on('slide.bs.carousel', function (e) {
    /*
        CC 2.0 License Iatek LLC 2018 - Attribution required
    */
    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 5;
    var totalItems = $('.carousel-item').length;

    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.carousel-item').eq(i).appendTo('.carousel-inner');
            }
            else {
                $('.carousel-item').eq(0).appendTo('.carousel-inner');
            }
        }
    }
});

const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
  }
});


/*  Carousel model lightbox*/




function openModal() {
  document.getElementById("myModal").style.display ="block";
  document.body.classList.add('lock-scroll');

}


function closeModal() {
  document.getElementById("myModal").style.display = "none";
    document.body.classList.remove('lock-scroll');
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}


// ------------contact-----------
document.querySelector('#contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    e.target.elements.name.value = '';
    e.target.elements.email.value = '';
    e.target.elements.message.value = '';
  });


// ------------films-----------





//  $('.navbar-container ul li a').on('click', function() {
// 	// $('.active-link').removeClass('active-link');
// 	// $(this).addClass('active-link');
//   $( '.navbar-container ul' ).find( 'li.active' ).removeClass( 'active' );
// 	$( this ).parent( 'li' ).addClass( 'active' );
// });


// $(document).on('click','ul li',function() {
//   $(this).addClass('active').siblings().removeClass('active')
// })
