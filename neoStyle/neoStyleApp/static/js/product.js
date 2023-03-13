const img = document.querySelectorAll('.img-select a');
const imgBtn = [...img];
let imgId = 1;

imgBtn.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-show img:first-child').clientWidth;

    document.querySelector('.img-show').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);


// Size

const sizeButton = document.querySelectorAll('.size-button');

sizeButton.forEach(button => {
  button.addEventListener('click', () => {
    sizeButton.forEach(b => b.classList.remove('active'));
    button.classList.add('active');
  });
});


// function selectSize(size) {
//     localStorage.setItem('selectedSize', size);
// }






