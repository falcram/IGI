
class Slider {
    constructor(sliderElement, options) {
        this.sliderElement = sliderElement;
        this.slides = sliderElement.querySelectorAll('.slide');
        this.currentIndex = 0;
        this.loop = options.loop || false;
        this.navs = options.navs || false;
        this.pags = options.pags || false;
        this.auto = options.auto || false;
        this.stopMouseHover = options.stopMouseHover || false;
        this.delay = options.delay || 5;

        this.init();
    }

    init() {
        this.updateSlides();
        this.updatePagination();
        this.updateSlideNumber();
        this.bindEvents();
        if (this.auto) {
            this.startAutoRotate();
        }
    }

    bindEvents() {
        if (this.navs) {
            this.sliderElement.querySelector('.next').addEventListener('click', () => this.next());
            this.sliderElement.querySelector('.prev').addEventListener('click', () => this.prev());
        } else {
            this.sliderElement.querySelector('.next').style.display = 'none';
            this.sliderElement.querySelector('.prev').style.display = 'none';
        }

        if (this.stopMouseHover && this.auto) {
            this.sliderElement.addEventListener('mouseenter', () => this.stopAutoRotate());
            this.sliderElement.addEventListener('mouseleave', () => this.startAutoRotate());
        }

        if (this.pags) {
            this.slides.forEach((slide, index) => {
                const paginationButton = document.createElement('button');
                paginationButton.textContent = index + 1;
                paginationButton.addEventListener('click', () => this.goToSlide(index));
                this.sliderElement.querySelector('.pagination').appendChild(paginationButton);
                slide.querySelector('img').addEventListener('click', () => {
                    window.location.href = slide.dataset.link; // Переход по ссылке только при клике на изображение
                });
            });
        } else {
            this.sliderElement.querySelector('.pagination').style.display = 'none';
        }

        
    }

    next() {
        this.goToSlide(this.currentIndex + 1);
    }

    prev() {
        this.goToSlide(this.currentIndex - 1);
    }

    goToSlide(index) {
        if (this.loop) {
            this.currentIndex = (index + this.slides.length) % this.slides.length;
        } else {
            this.currentIndex = Math.max(0, Math.min(index, this.slides.length - 1));
        }
        this.updateSlides();
        this.updatePagination();
        this.updateSlideNumber();
    }

    updateSlides() {
        this.slides.forEach((slide, index) => {
            slide.classList.remove('active');
            if (index === this.currentIndex) {
                slide.classList.add('active');
            }
        });
    }

    updatePagination() {
        if (this.pags) {
            const paginationButtons = this.sliderElement.querySelector('.pagination').children;
            Array.from(paginationButtons).forEach((button, index) => {
                button.classList.toggle('active', index === this.currentIndex);
            });
        }
    }

    updateSlideNumber() {
        const slideNumberElement = this.sliderElement.querySelector('.slide-number');
        slideNumberElement.textContent = `${this.currentIndex + 1}/${this.slides.length}`;
    }

    startAutoRotate() {
        this.interval = setInterval(() => this.next(), this.delay * 1000);
    }

    stopAutoRotate() {
        clearInterval(this.interval);
    }
}

// Инициализация слайдера
document.addEventListener('DOMContentLoaded', () => {
    const sliderElement = document.querySelector('.slider');
    const slider = new Slider(sliderElement, {
        loop: true,
        navs: true,
        pags: true,
        auto: true,
        stopMouseHover: true,
        delay: 5
    });
});