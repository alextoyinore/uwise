const initSlider = () => {
        const sliderButtons = document.querySelectorAll('.slider-btn')
        const carouselWrapper = document.querySelector('.carousel-wrapper')
        const carouselItems = document.querySelector('.carousel-items')
        const carouselSectionNav = document.querySelector('.carousel-section-navs')
        const sliderWrapper = document.querySelector('.slider-wrapper')
        const sliderThumb = document.querySelector('.slider-thumb')

        const maxScrollLeft = carouselWrapper.scrollWidth - carouselWrapper.clientWidth

        if(carouselItems.getBoundingClientRect().width < carouselWrapper.getBoundingClientRect().width){
            carouselSectionNav.style.display = 'none'
        }else {
            var carouselWidthPercentage = (carouselWrapper.clientWidth / carouselItems.clientWidth)
            var sliderWidth = sliderWrapper.clientWidth * carouselWidthPercentage
            sliderThumb.style.width = sliderWidth + 'px'
        }


        sliderButtons.forEach(button => {
            button.addEventListener('click', ()=>{
                const direction = button.id === 'prev' ? -1 : 1
                const scrollAmount = carouselWrapper.clientWidth * direction
                carouselWrapper.scrollBy({left: scrollAmount, behavior: "smooth"})
            })
        })


        const updateSliderPosition = () => {
            const scrollPosition = carouselWrapper.scrollLeft
            const thumbPosition = (scrollPosition / maxScrollLeft) * (sliderWrapper.clientWidth - sliderThumb.offsetWidth)
            sliderThumb.style.left = `${thumbPosition}px`
        }

        carouselWrapper.addEventListener('scroll', ()=>{
            updateSliderPosition()
        })

    }

    window.addEventListener('load', initSlider)

    // window.addEventListener('load', ()=>{
    //     const bigInfoImage = document.querySelectorAll('.biginfo-image img')
    //     for (let i = 0; i < bigInfoImage.length; i++) {
    //         bigInfoImage[i].style.transform = `rotate(-${10*i}deg)`
    //     }
    // })