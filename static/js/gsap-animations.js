// GSAP Animations for Meghalaya Tourism Website
// Smooth scroll animations and page load effects

// Check if GSAP is available
if (typeof gsap === 'undefined') {
    console.warn('GSAP not loaded - animations disabled');
} else {
    // Register ScrollTrigger plugin
    gsap.registerPlugin(ScrollTrigger);
}

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Exit early if GSAP is not available
    if (typeof gsap === 'undefined') {
        console.warn('GSAP not available, skipping animations');
        return;
    }
    
    // ==================== SMOOTH SCROLL SETUP ====================
    // Add smooth scrolling behavior
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // ==================== NAVBAR ANIMATION ====================
    gsap.from('.navbar', {
        y: -100,
        opacity: 0,
        duration: 1,
        ease: 'power3.out'
    });
    
    gsap.from('.navbar-brand', {
        x: -50,
        opacity: 0,
        duration: 0.8,
        delay: 0.3,
        ease: 'power2.out'
    });
    
    gsap.from('.nav-item', {
        y: -30,
        opacity: 0,
        duration: 0.5,
        stagger: 0.1,
        delay: 0.5,
        ease: 'power2.out'
    });
    
    // ==================== HERO SLIDER ANIMATION ====================
    const sliderBox = document.querySelector('.slider-box');
    if (sliderBox) {
        gsap.from('.slider-box', {
            scale: 1.1,
            opacity: 0,
            duration: 1.5,
            ease: 'power2.out'
        });
        
        // Parallax effect on scroll
        gsap.to('.slider-video', {
            yPercent: 30,
            ease: 'none',
            scrollTrigger: {
                trigger: '.slider-box',
                start: 'top top',
                end: 'bottom top',
                scrub: true
            }
        });
    }
    
    // ==================== SECTION TITLE ANIMATIONS ====================
    gsap.utils.toArray('.section-title').forEach(title => {
        gsap.set(title, { opacity: 1, y: 0 });
        gsap.fromTo(title, 
            { y: 30, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: title,
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                y: 0,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
    });
    
    // ==================== PLACE HEADING ANIMATIONS ====================
    gsap.utils.toArray('.place-heading').forEach(heading => {
        gsap.set(heading, { opacity: 1, x: 0 });
        gsap.fromTo(heading, 
            { x: -30, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: heading,
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                x: 0,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
        
        // Animate the dot icon
        const dotIcon = heading.querySelector('.dot-icon');
        if (dotIcon) {
            gsap.set(dotIcon, { scale: 1 });
            gsap.fromTo(dotIcon, 
                { scale: 0.5 },
                {
                    scrollTrigger: {
                        trigger: heading,
                        start: 'top 90%',
                        toggleActions: 'play none none none'
                    },
                    scale: 1,
                    duration: 0.4,
                    delay: 0.2,
                    ease: 'back.out(1.7)'
                }
            );
        }
    });
    
    // ==================== SIDE SECTIONS (Video + Text) ====================
    gsap.utils.toArray('.side').forEach(section => {
        const video = section.querySelector('video');
        const text = section.querySelector('.cherr-text, .pb-text, .place-text');
        
        // Ensure elements are visible first
        if (video) gsap.set(video, { opacity: 1, x: 0 });
        if (text) gsap.set(text, { opacity: 1, x: 0 });
        
        if (video) {
            gsap.fromTo(video, 
                { x: -50, opacity: 0.8 },
                {
                    scrollTrigger: {
                        trigger: section,
                        start: 'top 85%',
                        toggleActions: 'play none none none'
                    },
                    x: 0,
                    opacity: 1,
                    duration: 0.8,
                    ease: 'power2.out'
                }
            );
        }
        
        if (text) {
            gsap.fromTo(text, 
                { x: 50, opacity: 0.8 },
                {
                    scrollTrigger: {
                        trigger: section,
                        start: 'top 85%',
                        toggleActions: 'play none none none'
                    },
                    x: 0,
                    opacity: 1,
                    duration: 0.8,
                    delay: 0.1,
                    ease: 'power2.out'
                }
            );
        }
    });
    
    // ==================== CARD ANIMATIONS ====================
    // Using 'to' instead of 'from' to avoid initial hidden state
    gsap.utils.toArray('.reveal-card').forEach((card, index) => {
        // Set initial state explicitly
        gsap.set(card, { opacity: 1, y: 0 });
        
        // Create animation that enhances visibility on scroll
        gsap.fromTo(card, 
            { y: 30, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: card,
                    start: 'top 95%',
                    toggleActions: 'play none none none'
                },
                y: 0,
                opacity: 1,
                duration: 0.6,
                delay: (index % 3) * 0.1,
                ease: 'power2.out'
            }
        );
    });
    
    // ==================== IMAGE CARD HOVER EFFECTS ====================
    gsap.utils.toArray('.image-card').forEach(card => {
        const img = card.querySelector('img');
        
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                y: -10,
                scale: 1.02,
                duration: 0.3,
                ease: 'power2.out'
            });
            if (img) {
                gsap.to(img, {
                    scale: 1.1,
                    duration: 0.4,
                    ease: 'power2.out'
                });
            }
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                y: 0,
                scale: 1,
                duration: 0.3,
                ease: 'power2.out'
            });
            if (img) {
                gsap.to(img, {
                    scale: 1,
                    duration: 0.4,
                    ease: 'power2.out'
                });
            }
        });
    });
    
    // ==================== MAP SECTION ANIMATIONS ====================
    gsap.utils.toArray('.map-container').forEach(map => {
        gsap.set(map, { opacity: 1, scale: 1 });
        gsap.fromTo(map, 
            { scale: 0.95, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: map,
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                scale: 1,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
    });
    
    gsap.utils.toArray('.icon-wrapper').forEach(wrapper => {
        gsap.set(wrapper, { opacity: 1, y: 0 });
        gsap.fromTo(wrapper, 
            { y: 20, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: wrapper,
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                y: 0,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
    });
    
    // ==================== 3D SLIDER SECTION ====================
    const divbody = document.querySelector('.divbody');
    if (divbody) {
        gsap.set('.text-card', { opacity: 1, x: 0 });
        gsap.set('.sliderd', { opacity: 1, x: 0, rotation: 0 });
        
        gsap.fromTo('.text-card', 
            { x: -50, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: '.divbody',
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                },
                x: 0,
                opacity: 1,
                duration: 0.8,
                ease: 'power2.out'
            }
        );
        
        gsap.fromTo('.sliderd', 
            { x: 50, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: '.divbody',
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                },
                x: 0,
                opacity: 1,
                duration: 0.8,
                ease: 'power2.out'
            }
        );
    }
    
    // ==================== GALLERY SECTION ====================
    const gallery = document.querySelector('.gallery');
    if (gallery) {
        gsap.set('.gallery-container', { opacity: 1, y: 0 });
        gsap.fromTo('.gallery-container', 
            { y: 30, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: '.gallery',
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                y: 0,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
    }
    
    // ==================== THREE SECTION (Regions, Travel, Festivals) ====================
    gsap.utils.toArray('.three-sec-div').forEach((div, index) => {
        gsap.set(div, { opacity: 1, y: 0 });
        gsap.fromTo(div, 
            { y: 30, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: div,
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                y: 0,
                opacity: 1,
                duration: 0.6,
                delay: index * 0.1,
                ease: 'power2.out'
            }
        );
    });
    
    // ==================== TRIP HEADING ANIMATION ====================
    const tripHeading = document.querySelector('.trip-heading');
    if (tripHeading) {
        gsap.set('.trip-heading', { opacity: 1, scale: 1 });
        gsap.fromTo('.trip-heading', 
            { scale: 0.9, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: '.trip-heading',
                    start: 'top 90%',
                    toggleActions: 'play none none none'
                },
                scale: 1,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
        
        // Animate arrow icon continuously
        gsap.to('.arrow-icon', {
            y: 10,
            duration: 0.6,
            repeat: -1,
            yoyo: true,
            ease: 'power1.inOut'
        });
    }
    
    // ==================== FOOTER ANIMATIONS ====================
    const footer = document.querySelector('.footer');
    if (footer) {
        gsap.set('.footer', { opacity: 1, y: 0 });
        gsap.fromTo('.footer', 
            { y: 20, opacity: 0.8 },
            {
                scrollTrigger: {
                    trigger: '.footer',
                    start: 'top 95%',
                    toggleActions: 'play none none none'
                },
                y: 0,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out'
            }
        );
    }
    
    gsap.utils.toArray('.social-media a').forEach(link => {
        gsap.set(link, { opacity: 1, scale: 1 });
    });
    
    // ==================== SCROLL PROGRESS INDICATOR ====================
    gsap.to('body', {
        scrollTrigger: {
            trigger: 'body',
            start: 'top top',
            end: 'bottom bottom',
            scrub: true
        }
    });
    
    // ==================== SMOOTH REVEAL FOR ALL CONTAINERS ====================
    gsap.utils.toArray('.container').forEach(container => {
        gsap.from(container, {
            scrollTrigger: {
                trigger: container,
                start: 'top 90%',
                toggleActions: 'play none none none'
            },
            opacity: 0,
            y: 30,
            duration: 0.6,
            ease: 'power2.out'
        });
    });
    
    // ==================== STAGGER ANIMATION FOR LIST ITEMS ====================
    gsap.utils.toArray('.styled-list').forEach(list => {
        const items = list.querySelectorAll('li');
        gsap.from(items, {
            scrollTrigger: {
                trigger: list,
                start: 'top 85%',
                toggleActions: 'play none none reverse'
            },
            x: -30,
            opacity: 0,
            duration: 0.5,
            stagger: 0.1,
            ease: 'power2.out'
        });
    });
    
    // ==================== MAGNETIC BUTTON EFFECT ====================
    gsap.utils.toArray('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', (e) => {
            gsap.to(btn, {
                scale: 1.05,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
        
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, {
                scale: 1,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
    });
    
    // ==================== REFRESH SCROLLTRIGGER ON RESIZE ====================
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            ScrollTrigger.refresh();
        }, 250);
    });
    
});

// ==================== CUSTOM CURSOR TRAIL (Optional Enhancement) ====================
// Uncomment below for a custom cursor effect
/*
const cursor = document.createElement('div');
cursor.className = 'custom-cursor';
document.body.appendChild(cursor);

document.addEventListener('mousemove', (e) => {
    gsap.to(cursor, {
        x: e.clientX,
        y: e.clientY,
        duration: 0.3,
        ease: 'power2.out'
    });
});
*/
