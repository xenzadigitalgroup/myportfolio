document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.querySelector('.burger-menu');
    const dropdownMenu = document.querySelector('.dropdown');

    burgerMenu.addEventListener('click', function() {
        dropdownMenu.classList.toggle('show');
    });
});

// Fungsi untuk mengecek apakah elemen terlihat di viewport
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  // Fungsi untuk menambahkan kelas visible ke elemen yang terlihat
  function onScroll() {
    const elements = document.querySelectorAll('.scroll-animation');
    elements.forEach(element => {
      if (isElementInViewport(element)) {
        element.classList.add('visible');
      }
    });
  }

  // Tambahkan event listener untuk scroll dan muat
  window.addEventListener('scroll', onScroll);
  window.addEventListener('load', onScroll);