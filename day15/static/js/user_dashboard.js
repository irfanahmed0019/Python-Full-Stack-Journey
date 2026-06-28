<script>
        // Simple micro-interaction for hover states on sidebar
        document.querySelectorAll('aside nav a').forEach(link => {
            link.addEventListener('mouseenter', () => {
                if (!link.classList.contains('bg-primary-container')) {
                    link.style.transform = 'translateX(4px)';
                }
            });
            link.addEventListener('mouseleave', () => {
                link.style.transform = 'translateX(0)';
            });
        });
    </script>