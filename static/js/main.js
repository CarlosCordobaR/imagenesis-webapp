// Imagénesis - JavaScript Principal con efectos del logo

document.addEventListener('DOMContentLoaded', function() {
    
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Efectos del logo y navbar
    initLogoEffects();
    
    // Animaciones de scroll
    initScrollAnimations();
    
    // Navegación suave
    initSmoothScroll();
    
    // Efectos del navbar
    initNavbarEffects();
    
    // Formularios
    initFormValidation();
});

// Efectos profesionales del logo
function initLogoEffects() {
    const navbar = document.querySelector('.navbar');
    const logo = document.querySelector('.navbar-logo');
    
    // Efecto de scroll en navbar
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Animación de carga del logo
    if (logo) {
        logo.addEventListener('load', function() {
            this.style.opacity = '0';
            this.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                this.style.transition = 'all 0.6s ease-out';
                this.style.opacity = '1';
                this.style.transform = 'translateY(0)';
            }, 100);
        });
    }
    
    // Efecto parallax sutil en el logo del footer
    const footerLogo = document.querySelector('.footer-logo');
    if (footerLogo) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.1;
            footerLogo.style.transform = `translateY(${rate}px)`;
        });
    }
}

// Animaciones de scroll
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observar elementos con clase fade-in
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });

    // Observar tarjetas y elementos
    document.querySelectorAll('.feature-card, .service-category, .info-card, .testimonial-card').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

// Navegación suave
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Efectos del navbar
function initNavbarEffects() {
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
}

// Validación de formularios
function initFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                e.stopPropagation();
            }
            this.classList.add('was-validated');
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            showFieldError(field, 'Este campo es obligatorio');
        } else {
            clearFieldError(field);
        }
    });
    
    // Validar email
    const emailFields = form.querySelectorAll('input[type="email"]');
    emailFields.forEach(field => {
        if (field.value && !isValidEmail(field.value)) {
            isValid = false;
            showFieldError(field, 'Ingresa un email válido');
        }
    });
    
    // Validar teléfono
    const phoneFields = form.querySelectorAll('input[type="tel"]');
    phoneFields.forEach(field => {
        if (field.value && !isValidPhone(field.value)) {
            isValid = false;
            showFieldError(field, 'Ingresa un número de teléfono válido');
        }
    });
    
    return isValid;
}

function showFieldError(field, message) {
    field.classList.add('is-invalid');
    
    let feedback = field.parentNode.querySelector('.invalid-feedback');
    if (!feedback) {
        feedback = document.createElement('div');
        feedback.className = 'invalid-feedback';
        field.parentNode.appendChild(feedback);
    }
    feedback.textContent = message;
}

function clearFieldError(field) {
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
    
    const feedback = field.parentNode.querySelector('.invalid-feedback');
    if (feedback) {
        feedback.remove();
    }
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phone) {
    const phoneRegex = /^[\+]?[\d\s\-\(\)]{10,}$/;
    return phoneRegex.test(phone);
}

// Utilidades para modales
function showModal(modalId) {
    const modal = new bootstrap.Modal(document.getElementById(modalId));
    modal.show();
}

function hideModal(modalId) {
    const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
    if (modal) {
        modal.hide();
    }
}

// Notificaciones toast
function showToast(message, type = 'info') {
    const toastContainer = getOrCreateToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Remover el toast después de que se oculte
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}

function getOrCreateToastContainer() {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        container.style.zIndex = '1055';
        document.body.appendChild(container);
    }
    return container;
}

// Funciones de utilidad para la IA de diagnóstico
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function isValidImageFile(file) {
    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'];
    const maxSize = 10 * 1024 * 1024; // 10MB
    
    if (!allowedTypes.includes(file.type)) {
        showToast('Tipo de archivo no válido. Solo se permiten JPEG y PNG.', 'danger');
        return false;
    }
    
    if (file.size > maxSize) {
        showToast('El archivo es demasiado grande. Máximo 10MB.', 'danger');
        return false;
    }
    
    return true;
}

// Funciones para reserva de citas
function setMinDate(inputId, daysFromNow = 1) {
    const input = document.getElementById(inputId);
    if (input) {
        const date = new Date();
        date.setDate(date.getDate() + daysFromNow);
        input.min = date.toISOString().split('T')[0];
    }
}

function formatDate(date) {
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    };
    return new Date(date).toLocaleDateString('es-ES', options);
}

// Funciones para integración con WhatsApp
function sendWhatsAppMessage(phone, message) {
    const cleanPhone = phone.replace(/\D/g, '');
    const encodedMessage = encodeURIComponent(message);
    const url = `https://wa.me/${cleanPhone}?text=${encodedMessage}`;
    window.open(url, '_blank');
}

// Función de utilidad para copiar texto al portapapeles
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showToast('Texto copiado al portapapeles', 'success');
    }, function(err) {
        console.error('Error al copiar: ', err);
        showToast('Error al copiar el texto', 'danger');
    });
}

// Analytics y tracking (placeholder para Google Analytics)
function trackEvent(eventName, parameters = {}) {
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, parameters);
    }
    console.log('Event tracked:', eventName, parameters);
}

// Funciones de accesibilidad
function initAccessibility() {
    // Navegación por teclado mejorada
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            document.body.classList.add('keyboard-navigation');
        }
    });
    
    document.addEventListener('mousedown', function() {
        document.body.classList.remove('keyboard-navigation');
    });
    
    // Soporte para lectores de pantalla
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link visually-hidden-focusable';
    skipLink.textContent = 'Saltar al contenido principal';
    document.body.insertBefore(skipLink, document.body.firstChild);
}

// Inicializar accesibilidad
initAccessibility();

// Exportar funciones para uso global
window.ImagenesisApp = {
    showToast,
    showModal,
    hideModal,
    trackEvent,
    sendWhatsAppMessage,
    copyToClipboard,
    formatFileSize,
    isValidImageFile,
    setMinDate,
    formatDate
};
