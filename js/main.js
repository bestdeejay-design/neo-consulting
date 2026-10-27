/* ООО «НЕО КОНСАЛТИНГ» — минимальный JS
   - переключение мобильного меню
   - текущий год в подвале
   - якоря: один скролл с посадкой от реальной высоты шапки */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia
    && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Высота sticky-шапки замеряется в момент скролла, посадка встык —
  // без зазора: на стыках секций с чередующимися фонами зазор показывал
  // полоску предыдущего блока под шапкой. Должно совпадать с
  // scroll-margin-top в main.css.
  function headerOffset() {
    var header = document.querySelector(".site-header");
    return header ? Math.ceil(header.getBoundingClientRect().height) : 64;
  }

  function scrollToId(id, smooth) {
    if (!id) return false;
    var el = document.getElementById(id);
    if (!el) return false;
    var y = el.getBoundingClientRect().top + window.pageYOffset - headerOffset();
    var max = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
    window.scrollTo({
      top: Math.max(0, Math.min(y, max)),
      behavior: smooth && !reduceMotion ? "smooth" : "auto"
    });
    return true;
  }

  function hashId() {
    if (!location.hash || location.hash.length < 2) return "";
    try {
      return decodeURIComponent(location.hash.slice(1));
    } catch (e) {
      return location.hash.slice(1);
    }
  }

  // Посадка после захода на /#id (в т.ч. переходом с /materials/):
  // нативный прыжок Chrome игнорирует scroll-padding, поэтому пересаживаем
  // мгновенно и ровно один раз — без второго видимого рывка.
  window.addEventListener("load", function () {
    var id = hashId();
    if (id) window.setTimeout(function () { scrollToId(id, false); }, 0);
  });
  window.addEventListener("hashchange", function () {
    scrollToId(hashId(), true);
  });

  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "?" || href.indexOf("mailto:") === 0 || href.indexOf("tel:") === 0) return;
    var url;
    try { url = new URL(a.href, location.href); } catch (err) { return; }
    if (url.origin !== location.origin) return;
    if (url.pathname !== location.pathname) return;
    if (!url.hash || url.hash.length < 2) return;
    var id = decodeURIComponent(url.hash.slice(1));
    if (!document.getElementById(id)) return;
    e.preventDefault();
    if (menu && menu.classList.contains("is-open")) closeMenu();
    if (history.pushState) history.pushState(null, "", url.hash);
    else location.hash = url.hash;
    scrollToId(id, true);
  });

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

  // Форма обратной связи: mailto-письмо из почтового клиента пользователя
  var form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      var name = document.getElementById("f-name").value.trim();
      var contact = document.getElementById("f-contact").value.trim();
      var comment = document.getElementById("f-comment").value.trim();
      var subject = "Заявка с сайта НЕО КОНСАЛТИНГ — " + name;
      var body = "Имя: " + name + "\nТелефон или e-mail: " + contact +
        (comment ? "\nКомментарий: " + comment : "");

      window.location.href = "mailto:zh_nadi@mail.ru?subject=" +
        encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
