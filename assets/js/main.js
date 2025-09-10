// Mobile nav toggle
const nav = document.querySelector('.nav');
const menuBtn = document.querySelector('.menu-btn');
if (menuBtn) {
  menuBtn.addEventListener('click', () => nav.classList.toggle('open'));
}

// Close nav when clicking a link (mobile)
document.addEventListener('click', (e) => {
  if (e.target.matches('.nav-links a')) nav.classList.remove('open');
});

// Contact form fake-submit
const form = document.querySelector('#contact-form');
const toast = document.querySelector('#contact-toast');
if (form) {
  // Add link inputs dynamically
  const linkList = document.querySelector('#link-list');
  const addLinkBtn = document.querySelector('#add-link-btn');
  if (addLinkBtn && linkList) {
    addLinkBtn.addEventListener('click', () => {
      const input = document.createElement('input');
      input.name = 'links[]';
      input.type = 'url';
      input.placeholder = 'https://...';
      input.inputMode = 'url';
      input.style.marginTop = '8px';
      linkList.appendChild(input);
    });
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const name = data.get('name') || 'Neighbor';
    const links = data.getAll('links[]').filter((v) => (v || '').trim().length > 0);
    if (toast) {
      const linkMsg = links.length ? ` Received ${links.length} link${links.length>1?'s':''}.` : '';
      toast.textContent = `Thanks, ${name}! We’ll get you moving.${linkMsg}`;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 4000);
    }
    form.reset();
  });
}
