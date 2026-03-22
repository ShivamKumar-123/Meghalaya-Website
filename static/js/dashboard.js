// Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Theme Toggle
    const themeToggle = document.getElementById('themeToggle');
    const sunIcon = document.querySelector('.sun-icon');
    const moonIcon = document.querySelector('.moon-icon');
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('dashboard-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcons(savedTheme);
    
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('dashboard-theme', newTheme);
            updateThemeIcons(newTheme);
        });
    }
    
    function updateThemeIcons(theme) {
        if (sunIcon && moonIcon) {
            if (theme === 'dark') {
                sunIcon.style.display = 'none';
                moonIcon.style.display = 'block';
            } else {
                sunIcon.style.display = 'block';
                moonIcon.style.display = 'none';
            }
        }
    }
    
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const sidebar = document.querySelector('.sidebar');
    let sidebarOverlay = document.querySelector('.sidebar-overlay');
    
    if (!sidebarOverlay) {
        sidebarOverlay = document.createElement('div');
        sidebarOverlay.className = 'sidebar-overlay';
        document.body.appendChild(sidebarOverlay);
    }
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            sidebar.classList.toggle('active');
            sidebarOverlay.classList.toggle('active');
        });
    }
    
    sidebarOverlay.addEventListener('click', function() {
        sidebar.classList.remove('active');
        sidebarOverlay.classList.remove('active');
    });
    
    // Alert Close Buttons
    const alertCloseButtons = document.querySelectorAll('.alert-close');
    alertCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const alert = this.closest('.alert');
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(20px)';
            setTimeout(() => alert.remove(), 300);
        });
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(20px)';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
    
    // File Upload Preview
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                const previewContainer = this.closest('.form-group').querySelector('.image-preview-container');
                
                reader.onload = function(e) {
                    if (previewContainer) {
                        let preview = previewContainer.querySelector('.image-preview');
                        if (!preview) {
                            preview = document.createElement('img');
                            preview.className = 'image-preview';
                            previewContainer.appendChild(preview);
                        }
                        preview.src = e.target.result;
                    }
                };
                
                if (file.type.startsWith('image/')) {
                    reader.readAsDataURL(file);
                }
                
                // Update file name display
                const fileNameDisplay = this.closest('.file-upload').querySelector('.file-name');
                if (fileNameDisplay) {
                    fileNameDisplay.textContent = file.name;
                }
            }
        });
    });
    
    // Delete Confirmation Modal
    const deleteButtons = document.querySelectorAll('[data-delete]');
    const deleteModal = document.getElementById('deleteModal');
    const deleteForm = document.getElementById('deleteForm');
    const cancelDelete = document.getElementById('cancelDelete');
    const modalOverlay = document.querySelector('.modal-overlay');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const deleteUrl = this.getAttribute('data-delete');
            const itemName = this.getAttribute('data-name') || 'this item';
            
            if (deleteForm) {
                deleteForm.action = deleteUrl;
            }
            
            const modalItemName = document.getElementById('deleteItemName');
            if (modalItemName) {
                modalItemName.textContent = itemName;
            }
            
            if (modalOverlay) {
                modalOverlay.classList.add('active');
            }
        });
    });
    
    if (cancelDelete) {
        cancelDelete.addEventListener('click', function() {
            if (modalOverlay) {
                modalOverlay.classList.remove('active');
            }
        });
    }
    
    if (modalOverlay) {
        modalOverlay.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('active');
            }
        });
    }
    
    // Search functionality
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const tableRows = document.querySelectorAll('.data-table tbody tr');
            
            tableRows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    }
    
    // Form validation
    const forms = document.querySelectorAll('form[data-validate]');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    
                    // Remove error class on input
                    field.addEventListener('input', function() {
                        this.classList.remove('error');
                    }, { once: true });
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
    
    // Cascade animation for cards
    const cascadeElements = document.querySelectorAll('.cascade-in');
    cascadeElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
    });
});
