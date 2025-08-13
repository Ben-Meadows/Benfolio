document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded!");

    document.querySelectorAll("a[href^='#']").forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href")).scrollIntoView({
                behavior: "smooth"
            });
        });
    });
});

document.addEventListener('scroll', () => {
  document
    .querySelector('.navbar')
    .classList.toggle('scrolled', window.scrollY > 50);
});

// Reveal animations for project rows using IntersectionObserver
document.addEventListener('DOMContentLoaded', () => {
  const rows = document.querySelectorAll('.project-row');
  if (!('IntersectionObserver' in window) || rows.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.15 });

  rows.forEach(row => observer.observe(row));
});