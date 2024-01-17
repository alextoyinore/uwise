const prevButton = document.querySelector('.slider-btn-prev')
        const nextButton = document.querySelector('.slider-btn-next')
        const carouselItems = document.querySelector('.carousel-items')
        const courseCard = document.querySelector('.course-card')
        const lastCard = document.querySelector('.course-card:last-child')
        const carouselWrapper = document.querySelector('.carousel-wrapper')

        var currentX = carouselItems.style.left

        var carouselRight = carouselItems.getBoundingClientRect().right
        var carouselLeft = carouselItems.getBoundingClientRect().left

        var wrapperRight = carouselWrapper.getBoundingClientRect().right
        var wrapperLeft = carouselWrapper.getBoundingClientRect().left

        const courseCardWidth = courseCard.getBoundingClientRect().width
        const marginSize = 20

        const carouselSectionNavs = document.querySelector('.carousel-section-navs')
        const sliderWrapper = document.querySelector('.slider-wrapper')
        const slider = document.querySelector('.slider')

        const carouselItemsWidth = carouselItems.getBoundingClientRect().width
        const wrapperWidth = carouselWrapper.getBoundingClientRect().width

        const sliderWrapperWidth = sliderWrapper.getBoundingClientRect().width

        window.addEventListener('load', function(){
            if(carouselItemsWidth < wrapperWidth){
                carouselSectionNavs.style.display = 'none'
            }
            var sliderWidthPercentage = (wrapperWidth / carouselItemsWidth)
            var sliderWidth = sliderWrapperWidth * sliderWidthPercentage
            slider.style.width = sliderWidth + 'px'
        })

        const courseCardPercentOfCarouselItems = (courseCardWidth + marginSize) / carouselItemsWidth
        var sliderCurrentX = slider.getBoundingClientRect().left

        nextButton.addEventListener('click', function (){
            if(carouselRight > (wrapperRight)){
                const newX = currentX - (courseCardWidth + marginSize)
                carouselItems.style.translate = newX + 'px'
                const newSliderX = sliderCurrentX + courseCardPercentOfCarouselItems * 100
                slider.style.translate = newSliderX  + 'px'
                carouselItems.style.transition = '.5s ease-in-out'
                currentX = newX
                sliderCurrentX = newSliderX
                carouselRight = carouselItems.getBoundingClientRect().right
                carouselLeft = carouselItems.getBoundingClientRect().left
            }
        })

        prevButton.addEventListener('click', function (){
            if(carouselLeft < (wrapperLeft)){
                const newX = currentX + (courseCardWidth + marginSize)
                carouselItems.style.translate = newX + 'px'
                carouselItems.style.transition = '.5s ease-in-out'
                currentX = newX
                carouselLeft = carouselItems.getBoundingClientRect().left
                carouselRight = carouselItems.getBoundingClientRect().right
            }
        })