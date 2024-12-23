let totalSlides = document.querySelectorAll('.slider-image').length;
let currentSlide = 0;

document.querySelector('.banner-slide .slider').style.width = `calc(100vw * ${totalSlides})`;
document.querySelector('.slider-controls').style.height = `${document.querySelector('.banner-slide').clientHeight}px`;

function back() {
    currentSlide--;
    if(currentSlide < 0) {
        currentSlide = totalSlides - 1;
    }
    updateMargin();
}

function next() {
    currentSlide++;
    if(currentSlide > (totalSlides-1)) {
        currentSlide = 0;
    }
    updateMargin();
}

function updateMargin() {
    let sliderWidth = document.querySelector('.slider-image').clientWidth;
    let newMargin = (currentSlide * sliderWidth);
    document.querySelector('.slider').style.marginLeft = `-${newMargin}px`;
}

setInterval(next, 5000);


