import '../css/main.css';
import htmx from 'htmx.org';
import Alpine from 'alpinejs';

// Make Alpine globally accessible
window.Alpine = Alpine;
Alpine.start();

// Make HTMX globally accessible
window.htmx = htmx;