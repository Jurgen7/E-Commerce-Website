//SLIDER

let productContainer = document.querySelector('.cards-list');
let prevBtn = document.querySelector('.prev-btn');
let nextBtn = document.querySelector('.next-btn');

let currentProductIndex = 0;
let productWidth = 26;

prevBtn.disabled = true;

prevBtn.addEventListener('click', function() {
  currentProductIndex--;

  if (currentProductIndex <= 0) {
    prevBtn.disabled = true;
  } 
  
  nextBtn.disabled = false;

  if (window.innerWidth < 576) {
    productWidth = 22;
  }
  
  productContainer.style.transform = `translateX(-${currentProductIndex * productWidth}rem)`;
});


nextBtn.addEventListener('click', function() {
  currentProductIndex++;

  if (currentProductIndex >= productContainer.children.length - 1) {
    nextBtn.disabled = true;
  } 
  
  prevBtn.disabled = false;

  if (window.innerWidth < 576) {
    productWidth = 22;
  }
  
  productContainer.style.transform = `translateX(-${currentProductIndex * productWidth}rem)`;
});

// ANIMATION

document.addEventListener('scroll', function() {
  const videoContainer = document.querySelector('.video-container:last-child');
  const vidContainer = document.querySelector('.vid1-2');
  if (window.scrollY + window.innerHeight >= videoContainer.offsetTop) {
    vidContainer.style.visibility = 'visible';
    vidContainer.style.animation = 'slideFromRight 2.5s ease-in-out forwards';
  }
});


document.addEventListener('scroll', function() {
  const videoContainer = document.querySelector('.video-container:last-child');
  const textContainer = document.querySelector('#text2');
  if (window.scrollY + window.innerHeight >= videoContainer.offsetTop) {
    textContainer.style.visibility = 'visible';
    textContainer.style.animation = 'slideFromRight 1s ease-in-out forwards';
  }
});







