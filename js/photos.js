(function () {
  'use strict';

  var PHOTOS = [
    'assets/img/photos/photo-01.webp',
    'assets/img/photos/photo-02.webp',
    'assets/img/photos/photo-04.webp',
    'assets/img/photos/photo-05.webp',
    'assets/img/photos/photo-06.webp',
    'assets/img/photos/photo-07.webp',
    'assets/img/photos/photo-08.webp',
    'assets/img/photos/photo-09.webp',
    'assets/img/photos/photo-10.webp',
    'assets/img/photos/photo-11.webp',
    'assets/img/photos/photo-12.webp'
  ];

  var HERO_INDEXES = [0, 6, 7];
  var SLOTS = ['hero', 'about-1', 'about-2', 'team-1', 'team-2', 'gallery-1', 'gallery-2', 'gallery-3'];
  var LS_KEY = 'neo-photo-rotation';

  function shuffle(list) {
    for (var i = list.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = list[i];
      list[i] = list[j];
      list[j] = tmp;
    }
    return list;
  }

  function readLastHero() {
    try {
      return localStorage.getItem(LS_KEY);
    } catch (e) {
      return null;
    }
  }

  function storeLastHero(index) {
    try {
      localStorage.setItem(LS_KEY, String(index));
    } catch (e) {}
  }

  function pickHeroIndex() {
    var last = readLastHero();
    var pool = HERO_INDEXES.filter(function (i) { return String(i) !== last; });
    if (pool.length === 0) {
      pool = HERO_INDEXES.slice();
    }
    var index = pool[Math.floor(Math.random() * pool.length)];
    storeLastHero(index);
    return index;
  }

  function assignPhotos() {
    var heroIndex = pickHeroIndex();
    var rest = [];
    PHOTOS.forEach(function (_, i) {
      if (i !== heroIndex) {
        rest.push(i);
      }
    });
    rest = shuffle(rest);

    var order = [heroIndex].concat(rest.slice(0, SLOTS.length - 1));

    var images = document.querySelectorAll('img[data-slot]');
    images.forEach(function (img) {
      var slotIndex = SLOTS.indexOf(img.getAttribute('data-slot'));
      if (slotIndex === -1 || order[slotIndex] === undefined) {
        return;
      }
      img.src = PHOTOS[order[slotIndex]];
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', assignPhotos);
  } else {
    assignPhotos();
  }
})();