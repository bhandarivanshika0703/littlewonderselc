// Mobile menu toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
const menuIcon = document.getElementById('menu-icon');
const closeIcon = document.getElementById('close-icon');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('show');
        menuIcon.classList.toggle('hidden');
        closeIcon.classList.toggle('hidden');
    });
}

// Desktop Dropdown Navigation
document.addEventListener('DOMContentLoaded', function() {
    const navDropdowns = document.querySelectorAll('.nav-dropdown');

    navDropdowns.forEach(dropdown => {
        dropdown.addEventListener('mouseenter', () => dropdown.classList.add('open'));
        dropdown.addEventListener('mouseleave', () => dropdown.classList.remove('open'));

        const dropdownToggle = dropdown.querySelector('.nav-button');
        if (dropdownToggle) {
            dropdownToggle.addEventListener('click', function(e) {
                if (window.innerWidth <= 1024) {
                    e.preventDefault();
                    dropdown.classList.toggle('open');
                }
            });
        }
    });

    document.addEventListener('click', function(e) {
        if (!e.target.closest('.nav-dropdown')) {
            navDropdowns.forEach(d => d.classList.remove('open'));
        }
    });
});

// Email validation
function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ✅ CONTACT FORM (kept JS)
// const contactForm = document.getElementById('contact-form');
// if (contactForm) {
//     contactForm.addEventListener('submit', function(e) {
//         e.preventDefault();

//         const name = document.getElementById('name')?.value.trim();
//         const email = document.getElementById('email')?.value.trim();
//         const phone = document.getElementById('phone')?.value.trim();
//         const message = document.getElementById('message')?.value.trim();

//         if (!name || !email || !phone || !message) {
//             alert('Please fill all fields');
//             return;
//         }

//         if (!validateEmail(email)) {
//             alert('Invalid email');
//             return;
//         }

//         alert('Thank you! We will contact you.');
//         contactForm.reset();
//     });
// }

// // ✅ ENROL FORM (IMPORTANT FIX)
// const enrolForm = document.getElementById('enrol-form');
// if (enrolForm) {
//     enrolForm.addEventListener('submit', function() {
//         // 🚫 NO preventDefault
//         console.log("Form submitting to Django...");
//     });
// }

// // ✅ SAFE BUTTON LOADING (NO BLOCKING)
// document.querySelectorAll('button[type="submit"]').forEach(button => {
//     button.addEventListener('click', function() {
//         const form = this.closest('form');
//         if (form && form.checkValidity()) {
//             this.innerHTML = 'Sending...';
//             // ❌ DO NOT disable button
//         }
//     });
// });

// Scroll to top button
let btn = document.createElement('button');
btn.innerHTML = '↑';
btn.style.cssText = `
    position:fixed;bottom:30px;right:30px;width:50px;height:50px;
    border-radius:50%;background:#58C7F3;color:white;border:none;
    font-size:24px;display:none;cursor:pointer;
`;
document.body.appendChild(btn);

window.addEventListener('scroll', () => {
    btn.style.display = window.pageYOffset > 300 ? 'block' : 'none';
});

btn.onclick = () => window.scrollTo({top:0, behavior:'smooth'});

// Console message
console.log("✅ JS Loaded Successfully");