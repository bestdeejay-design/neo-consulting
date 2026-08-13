/* ООО «НЕО КОНСАЛТИНГ» — минимальный JS
   - переключение мобильного меню
   - текущий год в подвале
   - плавный скролл по якорям (с учётом высоты шапки через CSS scroll-padding) */
(function () {
  "use strict";

  // Текущий год
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  // Мобильное меню
  var toggle = document.getElementById("navToggle");
  var menu = document.getElementById("mobileNav");

  function closeMenu() {
    if (!menu || !toggle) return;
    menu.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Открыть меню");
  }

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Закрыть меню" : "Открыть меню");
    });

    // Закрытие при клике по ссылке
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeMenu();
    });

    // Закрытие по Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeMenu();
    });

    // Закрытие при уходе в десктоп (resize)
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 960) closeMenu();
    });
  }
})();
