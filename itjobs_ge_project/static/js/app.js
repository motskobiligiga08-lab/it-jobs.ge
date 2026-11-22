const toggle = document.querySelector('[data-menu-toggle]');
const menu = document.querySelector('[data-menu]');
if (toggle && menu) toggle.addEventListener('click', () => menu.classList.toggle('open'));

const cards = document.querySelectorAll('.job-card, .feature-card, .mini-job');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('reveal'); io.unobserve(entry.target); }
  }), { threshold: .08 });
  cards.forEach(card => { card.classList.add('will-reveal'); io.observe(card); });
}
