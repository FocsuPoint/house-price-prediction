/* ==========================================
   AI House Price Prediction
   JavaScript
========================================== */

// ===============================
// Navbar Scroll Effect
// ===============================

window.addEventListener("scroll", () => {

    const nav = document.querySelector("nav");

    if (window.scrollY > 60) {

        nav.classList.add("scrolled");

    } else {

        nav.classList.remove("scrolled");

    }

});

// ===============================
// Smooth Scroll
// ===============================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});

// ===============================
// Counter Animation
// ===============================

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    counter.innerText = "0";

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const current = +counter.innerText;

        const increment = target / 100;

        if (current < target) {

            counter.innerText = `${Math.ceil(current + increment)}`;

            setTimeout(updateCounter, 20);

        } else {

            counter.innerText = target;

        }

    };

    updateCounter();

});

// ===============================
// Reveal Animation
// ===============================

const reveals = document.querySelectorAll(".reveal");

window.addEventListener("scroll", () => {

    reveals.forEach(item => {

        const windowHeight = window.innerHeight;

        const revealTop = item.getBoundingClientRect().top;

        if (revealTop < windowHeight - 100) {

            item.classList.add("active");

        }

    });

});
// ===============================
// Prediction Form
// Submit to Flask so the real machine-learning model makes the prediction.
// ===============================
const predictionForm = document.getElementById("predictionForm");
if (predictionForm) {
    predictionForm.addEventListener("submit", function (event) {
        const inputs = predictionForm.querySelectorAll("input, select");
        let valid = true;
        inputs.forEach((input) => {
            if (!input.value) {
                input.style.borderColor = "red";
                valid = false;
            } else {
                input.style.borderColor = "#d1d5db";
            }
        });
        if (!valid) {
            event.preventDefault();
            alert("Please fill all the fields.");
        }
    });
}

// ===============================
// Indian Currency Format
// ===============================

function formatIndianCurrency(number) {

    return "₹ " + new Intl.NumberFormat("en-IN").format(number);

}
