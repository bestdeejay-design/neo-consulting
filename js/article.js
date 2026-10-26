/* Материалы: оглавление и кнопка «наверх». Меню — в js/main.js. */
(function () {
  "use strict";
  var btn = document.getElementById("backToTop");
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  var sections = tocLinks.map(function (a) {
    var href = a.getAttribute("href");
    return href ? document.querySelector(href) : null;
  });

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    if (btn) {
      if (y > 400) btn.classList.add("show");
      else btn.classList.remove("show");
    }
    var pos = y + 120;
    var current = -1;
    for (var i = 0; i < sections.length; i++) {
      if (sections[i] && sections[i].offsetTop <= pos) current = i;
    }
    tocLinks.forEach(function (l, i) {
      l.classList.toggle("active", i === current);
    });
  }

  if (btn) {
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();
})();
